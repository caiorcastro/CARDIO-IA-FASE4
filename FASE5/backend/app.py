
from flask import Flask, request, jsonify, render_template
from watson_service import WatsonService
import os

app = Flask(__name__, static_folder="../app", template_folder="../app")

# Armazenamento simples de sessão em memória (para protótipo)
# Em produção, usaria Redis ou banco de dados
user_sessions = {}

try:
    watson = WatsonService()
    print("Conectado ao IBM Watson com sucesso.")
except Exception as e:
    print(f"Erro ao conectar com Watson: {e}")
    watson = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def message():
    data = request.json
    user_msg = data.get('message')
    user_id = data.get('user_id', 'default_user')

    if not user_msg:
        return jsonify({"error": "Mensagem vazia"}), 400

    if not watson:
        return jsonify({"response": "Erro: Watson não configurado. Verifique o .env"}), 500

    # Recupera ou cria sessão para o usuário
    if user_id not in user_sessions:
        session_id = watson.create_session()
        if session_id:
            user_sessions[user_id] = session_id
        else:
            return jsonify({"response": "Erro ao criar sessão com Watson."}), 500
    
    session_id = user_sessions[user_id]

    # Envia para o Watson
    response_data = watson.send_message(session_id, user_msg)
    
    return jsonify({
        "response": response_data['text'],
        "intents": response_data.get('intents'),
        "entities": response_data.get('entities')
    })

if __name__ == '__main__':
    print("Iniciando servidor Flask na porta 5000...")
    app.run(debug=True, port=5000)
