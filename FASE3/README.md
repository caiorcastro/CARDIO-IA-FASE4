# CardioIA - Fase 3: Monitoramento Contínuo de Saúde com IoT

## Visão Geral do Projeto

Este projeto implementa um protótipo funcional de um sistema de monitoramento de saúde, integrando conceitos de Edge, Fog e Cloud Computing. A solução simula a coleta de sinais vitais de um paciente, o processamento local, a transmissão para a nuvem, a visualização em um dashboard e o disparo de alertas automatizados.

O projeto abrange desde a programação de um microcontrolador simulado (ESP32) até a criação de uma API REST e a análise de dados com modelos de Machine Learning.

## Estrutura de Diretórios

```
FASE3/
├── ir-alem/              # IR ALÉM 1: API REST e cliente
│   ├── client.py
│   ├── rest_alerts.py
│   ├── requirements.txt
│   └── REPORT_REST.md
├── node-red/             # Fluxos do Node-RED
│   ├── flow-hivemq-cloud.json
│   └── flow.json
├── notebooks/            # IR ALÉM 2: Análise de Séries Temporais
│   ├── phase3_time_series.ipynb
│   └── REPORT_TIMESERIES.md
├── reports/              # Relatórios principais (Parte 1 e 2)
│   ├── REPORT_EDGE.md
│   └── REPORT_MQTT_DASH.md
├── tools/                # Scripts de teste
│   └── test_mqtt_publish.py
└── wokwi/                # PARTE 1: Projeto do ESP32
    ├── sketch.ino
    ├── diagram.json
    └── config.example.h
```

## Checklist de Entregáveis (Avaliação)

Esta seção mapeia todos os requisitos da atividade para seus respectivos artefatos no projeto, garantindo que todos os critérios foram atendidos.

| Requisito                                      | Status      | Artefato(s) Correspondente(s)                                                                                             |
| ---------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Parte 1: Edge Computing**                    |             |                                                                                                                           |
| App Wokwi com ESP32 e 2 sensores               | ✅ Completo | `wokwi/sketch.ino`, `wokwi/diagram.json`                                                                                  |
| Armazenamento local em SPIFFS                  | ✅ Completo | `wokwi/sketch.ino` (funções `appendQueue`, `ensureSPIFFS`)                                                                |
| Resiliência offline e sincronização            | ✅ Completo | `wokwi/sketch.ino` (funções `publishOrQueue`, `flushQueue`)                                                               |
| Código C++ comentado                           | ✅ Completo | `wokwi/sketch.ino`                                                                                                        |
| Relatório de fluxo e resiliência (1 pág. min)  | ✅ Completo | `reports/REPORT_EDGE.md`                                                                                                  |
| **Parte 2: Cloud/Fog Computing**               |             |                                                                                                                           |
| Envio de dados via MQTT para broker na nuvem   | ✅ Completo | `wokwi/sketch.ino` (integrado com HiveMQ Cloud)                                                                           |
| Dashboard em Node-RED                          | ✅ Completo | `node-red/flow-hivemq-cloud.json`                                                                                           |
| Gráfico de sinal vital (BPM)                   | ✅ Completo | Node-RED: Nó `ui_chart`                                                                                                   |
| Medidor/gauge (Temperatura)                    | ✅ Completo | Node-RED: Nó `ui_gauge`                                                                                                   |
| Alerta visual para valores anômalos            | ✅ Completo | Node-RED: Nós `switch` e `ui_text`                                                                                        |
| Relatório de comunicação MQTT (2 pág. min)     | ✅ Completo | `reports/REPORT_MQTT_DASH.md`                                                                                             |
| **Ir Além 1: API REST e Alertas**              |             |                                                                                                                           |
| Cliente e Servidor REST em Python              | ✅ Completo | `ir-alem/client.py`, `ir-alem/rest_alerts.py`                                                                             |
| Lógica de verificação de risco                 | ✅ Completo | `ir-alem/rest_alerts.py` (função `risk_check`)                                                                            |
| Simulação de disparo de e-mail                 | ✅ Completo | `ir-alem/rest_alerts.py` (função `send_email` com modo simulado)                                                          |
| Relatório do fluxo implementado (1-2 pág.)     | ✅ Completo | `ir-alem/REPORT_REST.md`                                                                                                  |
| **Ir Além 2: Análise de Séries Temporais**     |             |                                                                                                                           |
| Notebook Python comentado                      | ✅ Completo | `notebooks/phase3_time_series.ipynb`                                                                                      |
| Comparação de métodos (Z-score vs MAD)         | ✅ Completo | `notebooks/phase3_time_series.ipynb`                                                                                      |
| Relatório comparativo (2 pág.)                 | ✅ Completo | `notebooks/REPORT_TIMESERIES.md`                                                                                          |
| Vídeo de 4 min apresentando resultados         | ⚠️ **Pendente** | **Ação manual necessária.** O vídeo deve ser gravado e o link inserido neste README.                                      |

---

## Como Executar o Projeto

### Pré-requisitos

- Acesso à internet
- Conta no [Wokwi](https://wokwi.com/)
- Conta no [HiveMQ Cloud](https://www.hivemq.com/cloud/) (plano gratuito)
- [Node.js](https://nodejs.org/en/) e [Node-RED](https://nodered.org/docs/getting-started/local) instalados
- [Python 3](https://www.python.org/downloads/) e `pip`

### 1. Simulação do Dispositivo (Wokwi)

1.  **Configurar Credenciais:**
    -   Crie o arquivo `FASE3/wokwi/config.h` a partir do exemplo `FASE3/wokwi/config.example.h`.
    -   Preencha `MQTT_USERNAME` e `MQTT_PASSWORD` com suas credenciais do HiveMQ Cloud.
2.  **Abrir no Wokwi:**
    -   Vá para [wokwi.com](https://wokwi.com/) e crie um novo projeto ESP32.
    -   Arraste os arquivos `sketch.ino`, `diagram.json` e o `config.h` que você criou para dentro do editor do Wokwi.
3.  **Iniciar Simulação:** Clique em "Start the simulation". O log na serial mostrará a conexão e o envio de dados.

### 2. Dashboard de Monitoramento (Node-RED)

1.  **Instalar o Dashboard:** Se for a primeira vez, instale o painel com o comando: `npm install node-red-dashboard`.
2.  **Iniciar Node-RED:** Execute `node-red` no seu terminal.
3.  **Importar o Fluxo:**
    -   Abra o editor (normalmente `http://127.0.0.1:1880`).
    -   Vá em `Menu > Import` e cole o conteúdo do arquivo `node-red/flow-hivemq-cloud.json`.
4.  **Configurar Credenciais:**
    -   Dê um duplo clique no nó MQTT de entrada (`Vitals`).
    -   Clique no ícone de lápis para editar o broker.
    -   Na aba "Security", preencha seu `Username` e `Password` do HiveMQ Cloud.
5.  **Acessar o Dashboard:** Abra a URL do dashboard (geralmente `http://127.0.0.1:1880/ui`).

### 3. API de Alertas (Python REST API)

1.  **Navegar para o diretório:** `cd FASE3/ir-alem`
2.  **Instalar dependências:** `pip install -r requirements.txt`
3.  **Executar o servidor:** `uvicorn rest_alerts:app --reload`
4.  **Executar o cliente (em outro terminal):** `python client.py`

O servidor irá processar os dados e imprimir alertas no console (em modo simulado).

### 4. Análise de Dados (Jupyter Notebook)

1.  **Instalar dependências:** `pip install jupyter pandas numpy matplotlib`
2.  **Iniciar Jupyter:** `jupyter notebook`
3.  **Abrir o Notebook:** Navegue e abra o arquivo `FASE3/notebooks/phase3_time_series.ipynb` e execute as células.

---

## Link para o Projeto Wokwi

- **Link Público:** **[COLE AQUI O LINK PÚBLICO DO SEU PROJETO WOKWI APÓS SALVÁ-LO]**
