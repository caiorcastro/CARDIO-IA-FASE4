# CardioIA - Fase 5: Assistente Cardiológico Inteligente

Esta fase foca na criação de uma interface conversacional inteligente para apoio ao paciente cardiológico, integrando **IBM Watson Assistant**, **Google Gemini** e **Automação RPA**.

## 🚀 Estrutura do Projeto

- **app/**: Frontend da aplicação (HTML/CSS/JS). Interface de chat moderna.
- **backend/**: Servidor Flask em Python.
    - `app.py`: Roteamento e API.
    - `watson_service.py`: Integração com SDK oficial do IBM Watson Assistant.
- **automation/**: Scripts de Automação (Ir Além 2).
    - `database_setup.py`: Cria banco SQLite com pacientes fictícios.
    - `rpa_monitor.py`: Robô que monitora sinais vitais, detecta anomalias e usa Gemini para gerar logs clínicos.
- **notebooks/**: Notebooks Jupyter (Ir Além 1).
    - `genai_extraction.ipynb`: Demonstração de extração de dados clínicos de texto desestruturado usando Gemini Pro.
- `WATSON_ACTIONS_GUIDE.md`: Guia passo-a-passo para criar as Actions no IBM Watson.
- `watson_skill_DEPRECATED.json`: (Evidência Acadêmica) Skill original em formato JSON.


## 🛠️ Configuração Inicial

1. **Dependências:**
   Instale as bibliotecas necessárias:
   ```bash
   pip install flask ibm-watson google-generativeai python-dotenv pandas
   ```

2. **Configuração de Chaves (.env):**
   Crie um arquivo `.env` na pasta `FASE5/` com o seguinte conteúdo (NUNCA suba este arquivo para o GitHub):
   ```env
   WATSON_API_KEY=SUA_CHAVE_AQUI
   WATSON_URL=SUA_URL_AQUI
   ASSISTANT_ID=SEU_ID_AQUI  <-- IMPORTANTE: Pegue este ID no painel da IBM após importar o skill
   GEMINI_API_KEY=SUA_CHAVE_AQUI
   ```

   > 🔒 **Segurança:** O arquivo `.env` contém credenciais sensíveis e já está configurado no `.gitignore` para não ser vazado.


3. **IBM Watson (NOVO - Actions):**
   - As novas instâncias do Watson utilizam **Actions**.
   - Siga o guia detalhado em `FASE5/WATSON_ACTIONS_GUIDE.md` para criar as ações de Saudação, Emergência e Agendamento manualmente (leva ~5 minutos).
   - Após criar e publicar, vá em **Environment Settings** -> **API Details**.
   - Copie o **Environment ID** e atualize o `.env` no campo `ASSISTANT_ID`.

   > ⚠️ **MUDANÇA IMPORTANTE: SKILLS DEPRECATED**
   > A IBM descontinuou o uso de *Dialog Skills* (JSON clássico) para novas instâncias do Watson Assistant.
   > **Não é mais possível importar o arquivo `watson_skill.json`.**
   >
   > Agora, toda a configuração deve ser feita via **Actions**.
   > O arquivo `watson_skill_DEPRECATED.json` foi mantido apenas como registro histórico.
   >
   > **Siga rigorosamente o `WATSON_ACTIONS_GUIDE.md` para configurar o chatbot.**
   >
   > **Alta Disponibilidade:** O sistema conta com um **Modo Híbrido**. Caso a conexão com o Watson falhe (ou não seja configurada), um motor local em Python assume o atendimento, garantindo que o chatbot **sempre funcione** para demonstrações.



## ▶️ Como Executar

### 1. Chatbot (Backend + Frontend)
Navegue até a pasta `backend` e rode:
```bash
python app.py
```
Acesse no navegador: `http://localhost:5000`

### 2. Automação RPA (Ir Além 2)
Navegue até a pasta `automation` e rode:
```bash
# Primeiro, crie o banco
python database_setup.py

# Depois, rode o monitor
python rpa_monitor.py
```
Verifique o arquivo gerado `automation/data/logs.json`.

### 3. Notebook GenAI (Ir Além 1)
Abra o Jupyter Notebook na pasta `notebooks`:
```bash
jupyter notebook notebooks/genai_extraction.ipynb
```
Execute as células para ver a extração de dados em ação.
