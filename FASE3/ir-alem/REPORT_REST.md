# Relatório: Comunicação Automatizada com REST e E-mail

## 1. Visão Geral

Este relatório detalha a implementação do componente "IR ALÉM 1" do projeto CardioIA, focado em criar um serviço de monitoramento de saúde que utiliza uma API REST para receber dados de sinais vitais, processá-los para identificar riscos e disparar alertas automatizados por e-mail.

O sistema foi desenvolvido em Python utilizando o framework **FastAPI** para a criação da API e a biblioteca **requests** para o cliente de teste.

## 2. Arquitetura e Fluxo de Dados

O fluxo de operação é composto por três etapas principais:

1.  **Coleta e Envio (Client):** O `client.py` simula um dispositivo de monitoramento (como o ESP32) que coleta sinais vitais (temperatura e BPM) em intervalos regulares. Ele envia esses dados via requisição `POST` para o endpoint `/vitals` da nossa API REST.

2.  **Processamento e Análise (API Server):** O servidor, implementado em `rest_alerts.py`, recebe os dados no endpoint `/vitals`. A API realiza as seguintes ações:
    *   **Validação:** Utiliza Pydantic para garantir que os dados recebidos estão no formato correto.
    *   **Análise de Risco:** A função `risk_check` avalia os dados com base em regras pré-definidas (e.g., BPM > 120 para taquicardia, Temperatura > 38°C para febre).
    *   **Acionamento de Alerta:** Se um risco "alto" é detectado, o sistema formata uma mensagem de alerta.

3.  **Notificação (E-mail):**
    *   Ao detectar um risco alto, a função `send_email` é chamada.
    *   Ela se conecta a um servidor SMTP (configurado via variáveis de ambiente) para enviar um e-mail detalhando o alerta para um destinatário pré-definido.
    *   **Modo Simulado:** Caso as credenciais SMTP não estejam configuradas, o sistema opera em modo simulado, imprimindo o conteúdo do e-mail no console. Isso garante a funcionalidade do fluxo de alerta mesmo em ambiente de desenvolvimento sem um servidor de e-mail.

## 3. Implementação

### `rest_alerts.py`

-   **Framework:** FastAPI.
-   **Modelo de Dados:** A classe `Vitals` (Pydantic) define a estrutura dos dados de entrada.
-   **Lógica de Risco:** A função `risk_check` contém a lógica de negócio para identificar anomalias.
-   **Envio de E-mail:** A função `send_email` abstrai a comunicação com o servidor SMTP, usando a biblioteca `smtplib` do Python. A configuração é feita de forma segura através de variáveis de ambiente, evitando credenciais no código-fonte.

### `client.py`

-   **Funcionalidade:** Gera dados de sinais vitais aleatórios, com uma chance de gerar valores anômalos para simular eventos de risco.
-   **Comunicação:** Utiliza a biblioteca `requests` para enviar os dados para a API, demonstrando como um cliente consumiria o serviço.

## 4. Como Executar

1.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Executar o servidor:**
    ```bash
    uvicorn rest_alerts:app --reload
    ```
3.  **Executar o cliente (em outro terminal):**
    ```bash
    python client.py
    ```

O terminal do servidor exibirá os resultados da análise de risco e os alertas de e-mail (reais ou simulados).
