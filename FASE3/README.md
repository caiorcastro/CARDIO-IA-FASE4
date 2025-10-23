# CardioIA — Fase 3: Monitoramento Contínuo (IoT)

Este diretório contém os artefatos para a entrega da Fase 3:

- Wokwi (ESP32) com DHT22 + Botão (simulação de BPM), armazenamento SPIFFS, resiliência offline, envio MQTT.
- Fluxo Node-RED (dashboard com gráfico, gauge e alerta automático).
- IR ALÉM 1: Script REST em Python com lógica de risco e disparo de e‑mail (simulado ou SMTP real via env vars).
- IR ALÉM 2: Notebook de séries temporais (detecção de anomalias simples e baseline comparativo).

## Estrutura

- `wokwi/` — Projeto ESP32 (Arduino)
- `node-red/flow.json` — Fluxo importável no Node‑RED
- `ir-alem/` — Scripts REST + README
- `reports/` — Relatórios solicitados (Parte 1 e Parte 2)
- `notebooks/phase3_time_series.ipynb` — Notebook de séries temporais

## Tópicos e limites

- Tópico MQTT: `cardioia/grupo1/vitals`
- Broker: `broker.hivemq.com:1883` (público, sem autenticação, para prototipagem)
- Limites de alerta (exemplo): BPM > 120 ou Temperatura > 38°C

---

## Como executar — Wokwi (ESP32)

1) Abra `wokwi/` no https://wokwi.com (importando os arquivos `diagram.json`, `wokwi.toml` e `sketch.ino`).
2) Clique em "Start the simulation".
3) O botão físico incrementa batimentos; o DHT22 fornece temperatura/umidade.
4) Quando online, o dispositivo publica dados no MQTT; offline, armazena no SPIFFS e sincroniza ao voltar.

Observação: a simulação usa `Wokwi-GUEST` como SSID. Para Wi‑Fi real, ajuste `WIFI_SSID/WIFI_PASS` no código.

### Usar HiveMQ Cloud (TLS 8883)

1) Edite `FASE3/wokwi/config.h` e preencha `MQTT_USERNAME` e `MQTT_PASSWORD` com seu usuário e senha do HiveMQ Cloud.
2) O host e porta já estão configurados: `817c2430152f460ba0cb75228198eb57.s1.eu.hivemq.cloud:8883`.
3) Por padrão, usamos `TLS_INSECURE 1` (protótipo, sem validação do certificado). Para validação completa, defina `TLS_INSECURE 0` e cole o `ROOT_CA` do seu endpoint.
4) Compile e rode no Wokwi. O dispositivo passará a publicar no HiveMQ Cloud.

## Como executar — Node‑RED

1) Inicie seu Node‑RED local (ou em nuvem) com `node-red-dashboard` instalado.
2) Para HiveMQ Cloud, importe `node-red/flow-hivemq-cloud.json` e, após importar, abra o nó do broker "HiveMQ Cloud" e preencha Usuário/Senha (Node‑RED não exporta credenciais). TLS já vem habilitado (porta 8883).
3) Alternativamente, para broker público sem TLS, importe `node-red/flow.json`.
4) Acesse o Dashboard para ver o gráfico (BPM), gauge (Temperatura) e o alerta visual.

## IR ALÉM 1 — REST + E‑mail

- Servidor/cliente em `ir-alem/`.
- Requerimentos: `pip install -r ir-alem/requirements.txt`
- Executar servidor: `uvicorn ir-alem.rest_alerts:app --reload`
- Executar cliente: `python ir-alem/client.py`
- E‑mail: configure as variáveis de ambiente para SMTP (veja `ir-alem/README.md`) ou use modo simulado.

## IR ALÉM 2 — Notebook

- Abra `notebooks/phase3_time_series.ipynb` no Jupyter e execute as células.

## Relatórios

- `reports/REPORT_EDGE.md` — Parte 1 (Edge + SPIFFS + resiliência)
- `reports/REPORT_MQTT_DASH.md` — Parte 2 (MQTT + Dashboard)
