document.addEventListener("DOMContentLoaded", () => {
    const inputField = document.getElementById("user-input");
    
    // Envia mensagem ao pressionar Enter
    inputField.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });
});

async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");
    const messageText = inputField.value.trim();

    if (!messageText) return;

    // Adiciona mensagem do usuário na tela
    appendMessage(messageText, 'user');
    inputField.value = "";

    // Mostra indicador de digitação (opcional, simplificado aqui)
    const loadingId = appendMessage("Digitando...", 'bot', true);

    try {
        const response = await fetch('/api/message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: messageText, user_id: 'user_123' }) // ID fixo para teste
        });

        const data = await response.json();
        
        // Remove indicador e adiciona resposta real
        document.getElementById(loadingId).remove();
        
        // Formata a resposta (quebras de linha vindas do Watson)
        const formattedResponse = data.response ? data.response.replace(/\n/g, '<br>') : "Sem resposta do servidor.";
        appendMessage(formattedResponse, 'bot');

    } catch (error) {
        document.getElementById(loadingId).remove();
        appendMessage("Erro ao conectar com o assistente.", 'bot');
        console.error("Erro:", error);
    }
}

function appendMessage(text, sender, isLoading = false) {
    const chatWindow = document.getElementById("chat-window");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", sender === 'user' ? 'user-message' : 'bot-message');
    
    if (isLoading) {
        messageDiv.id = "loading-" + Date.now();
        messageDiv.style.fontStyle = "italic";
        messageDiv.style.opacity = "0.7";
    }

    const content = document.createElement("p");
    content.innerHTML = text; // Permite HTML simples como <br> e <b>
    messageDiv.appendChild(content);

    const time = document.createElement("span");
    time.classList.add("timestamp");
    time.innerText = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    messageDiv.appendChild(time);

    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Auto-scroll para o final

    return messageDiv.id;
}
