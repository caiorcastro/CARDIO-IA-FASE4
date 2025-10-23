#pragma once

// Ative o uso do HiveMQ Cloud (TLS na porta 8883)
#define USE_HIVEMQ_CLOUD 1

// Host/porta do seu cluster HiveMQ Cloud
#define MQTT_HOST_CLOUD "817c2430152f460ba0cb75228198eb57.s1.eu.hivemq.cloud"
#define MQTT_PORT_CLOUD 8883

// Credenciais (preencha com seu usuário/senha do HiveMQ Cloud)
#define MQTT_USERNAME "tool_context7_user"
#define MQTT_PASSWORD "tool_context7_pass"

// TLS: 1 para habilitar cliente seguro
#define MQTT_USE_TLS 1

// Para protótipo: 1 = não verificar certificado (setInsecure)
// Para produção: 0 e forneça a ROOT_CA abaixo
#define TLS_INSECURE 1

// Opcional: raiz CA (quando TLS_INSECURE = 0). Cole o PEM completo aqui.
static const char* ROOT_CA = R"EOF(
-----BEGIN CERTIFICATE-----
<PASTE_ROOT_CA_CERTIFICATE_HERE>
-----END CERTIFICATE-----
)EOF";

// Fallback público (sem TLS) caso USE_HIVEMQ_CLOUD seja 0
#define MQTT_HOST_FALLBACK "broker.hivemq.com"
#define MQTT_PORT_FALLBACK 1883

