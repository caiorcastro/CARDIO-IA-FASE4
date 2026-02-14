
import os
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

class WatsonService:
    def __init__(self):
        api_key = os.getenv("WATSON_API_KEY")
        url = os.getenv("WATSON_URL")
        self.assistant_id = os.getenv("ASSISTANT_ID")
        
        if not api_key or not url or not self.assistant_id:
            raise ValueError("As chaves do Watson (API_KEY, URL, ASSISTANT_ID) não estão configuradas no .env")

        authenticator = IAMAuthenticator(api_key)
        self.assistant = AssistantV2(
            version='2021-06-14',
            authenticator=authenticator
        )
        self.assistant.set_service_url(url)

    def create_session(self):
        """Cria uma nova sessão com o assistente."""
        try:
            session = self.assistant.create_session(
                assistant_id=self.assistant_id
            ).get_result()
            return session['session_id']
        except Exception as e:
            print(f"Erro ao criar sessão: {e}")
            return None


    def local_response(self, message_text):
        """Simula a inteligência do Watson localmente (Fallback)."""
        msg = message_text.lower()
        
        # Lógica de Emergência
        if any(w in msg for w in ['dor', 'peito', 'infarto', 'ponta', 'coração']):
            return {
                "text": "🔴 **ALERTA DE EMERGÊNCIA** 🔴\nA dor irradia para o braço esquerdo ou mandíbula? Você sente náusea?",
                "intents": [{"intent": "dor_no_peito", "confidence": 1.0}],
                "entities": []
            }
        
        if any(w in msg for w in ['sim', 'irradia', 'formig', 'náusea']):
            return {
                "text": "🚨 **AÇÃO IMEDIATA NECESSÁRIA** 🚨\n\n1. Pare tudo e sente-se.\n2. Mastigue uma aspirina.\n3. **LIGUE 192 (SAMU) AGORA.**",
                "intents": [{"intent": "sim", "confidence": 1.0}],
                "entities": []
            }

        if any(w in msg for w in ['agendar', 'marcar', 'consulta', 'médico']):
            return {
                "text": "Para qual data você gostaria de agendar a consulta?",
                "intents": [{"intent": "agendar_consulta", "confidence": 1.0}],
                "entities": []
            }

        # Detecção básica de data (ex: 'dia 20', 'amanhã')
        if any(w in msg for w in ['dia', 'amanhã', 'segunda', 'terça', '/']):
            return {
                "text": f"Perfeito. Pré-agendamento realizado para: {message_text}. Você receberá a confirmação por e-mail.",
                "intents": [{"intent": "informar_data", "confidence": 1.0}],
                "entities": [{"entity": "sys-date", "value": message_text}]
            }

        if any(w in msg for w in ['oi', 'olá', 'bom dia', 'boa tarde']):
            return {
                "text": "Olá! Sou o **Assistente CardioIA**. 🫀\nPosso ajudar com agendamento ou emergências.",
                "intents": [{"intent": "saudacao", "confidence": 1.0}],
                "entities": []
            }

        return {
            "text": "Desculpe, não entendi. Tente 'Quero agendar' ou 'Dor no peito'.",
            "intents": [],
            "entities": []
        }

    def send_message(self, session_id, message_text):
        """Envia mensagem do usuário para o Watson e retorna a resposta."""
        # Se não tiver ID configurado ou der erro de conexão, usa Fallback
        if not self.assistant_id or self.assistant_id == "PREENCHA_COM_ENVIRONMENT_ID":
             print("⚠️  Watson ID não configurado. Usando Fallback Local.")
             return self.local_response(message_text)

        try:
            response = self.assistant.message(
                assistant_id=self.assistant_id,
                session_id=session_id,
                input={
                    'message_type': 'text',
                    'text': message_text,
                    'options': {
                        'return_context': True
                    }
                }
            ).get_result()

            if response['output']['generic']:
                text_response = response['output']['generic'][0]['text']
            else:
                text_response = "Desculpe, não entendi. Pode repetir?"

            return {
                "text": text_response,
                "intents": response['output'].get('intents', []),
                "entities": response['output'].get('entities', [])
            }

        except Exception as e:
            print(f"Erro na nuvem Watson: {e}. Ativando Fallback.")
            return self.local_response(message_text)

# Teste rápido se executado diretamente
if __name__ == "__main__":
    try:
        watDiv = WatsonService()
        sess_id = watDiv.create_session()
        print(f"Sessão criada: {sess_id}")
        resp = watDiv.send_message(sess_id, "Olá")
        print(f"Bot: {resp['text']}")
    except Exception as e:
        print(f"Erro no teste: {e}")
