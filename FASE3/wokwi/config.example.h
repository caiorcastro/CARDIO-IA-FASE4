#pragma once

// Ative o uso do HiveMQ Cloud (TLS na porta 8883)
#define USE_HIVEMQ_CLOUD 1

// Host/porta do seu cluster HiveMQ Cloud
#define MQTT_HOST_CLOUD "817c2430152f460ba0cb75228198eb57.s1.eu.hivemq.cloud"
#define MQTT_PORT_CLOUD 8883

// Credenciais (preencha com seu usuário/senha do HiveMQ Cloud)
#define MQTT_USERNAME ""
#define MQTT_PASSWORD ""

// TLS: 1 para habilitar cliente seguro
#define MQTT_USE_TLS 1

// Para protótipo: 1 = não verificar certificado (setInsecure)
// Para produção: 0 e forneça a ROOT_CA abaixo
#define TLS_INSECURE 0

// Opcional: raiz CA (quando TLS_INSECURE = 0). Cole o PEM completo aqui.
static const char* ROOT_CA = R"EOF(
-----BEGIN CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFGTCCBAGgAwIBAgISBY3q/k62gY9zzCKBwXeVZmRDMA0GCSqGSIb3DQEBCwUA
MDMxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQwwCgYDVQQD
EwNSMTIwHhcNMjUxMDE5MTgxNDI5WhcNMjYwMTE3MTgxNDI4WjAfMR0wGwYDVQQD
DBQqLnMxLmV1LmhpdmVtcS5jbG91ZDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
AQoCggEBAKVuz2sMPmxx2w/f81/YAEKTbNZMJPk2+ooLFg5hxXvReF+AwIT4XvZ+
MLhSKvFxmghJF+BB9WyhqrcJLGDCP4s6SOLWTYixEoTcaLUviqqn+06kYqDJ6E83
NGsc7T42DlPnzqcZZjPRed9rt4CP3RgeZlWyYZgiD8FoJG9gie8ytihF/FkGZT8T
N4Vkl2vQa3mfBWeeKrcuhcLPxqIWDz/30iYfLtEe5JYYScoCKTXcP9SUStjpR8pD
vfOWdvasOAuBy7yBbx01/4lcQt50hfbhTR/K14/D4rNkuuvU7ktSQnoxVXC8YDwG
zkny10DFt65mVYLNZcBQtOLHHOZGV30CAwEAAaOCAjkwggI1MA4GA1UdDwEB/wQE
AwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIw
ADAdBgNVHQ4EFgQUgsEjDU35+EWJKBsFxJ0lM0PXMi4wHwYDVR0jBBgwFoAUALUp
8i2ObzHom0yteD763OkM0dIwMwYIKwYBBQUHAQEEJzAlMCMGCCsGAQUFBzAChhdo
dHRwOi8vcjEyLmkubGVuY3Iub3JnLzAzBgNVHREELDAqghQqLnMxLmV1LmhpdmVt
cS5jbG91ZIISczEuZXUuaGl2ZW1xLmNsb3VkMBMGA1UdIAQMMAowCAYGZ4EMAQIB
MC4GA1UdHwQnMCUwI6AhoB+GHWh0dHA6Ly9yMTIuYy5sZW5jci5vcmcvNjguY3Js
MIIBBQYKKwYBBAHWeQIEAgSB9gSB8wDxAHcASZybad4dfOz8Nt7Nh2SmuFuvCoeA
GdFVUvvp6ynd+MMAAAGZ/eOokwAABAMASDBGAiEA5hLq4ze/NeLDJKSPI1IOnSpr
gWKanwFSky61clsLVtECIQDy35kv5Z20DEZaTUTRs0LTwOBtt4hCcsKfDGzfViY4
rQB2AJaXZL9VWJet90OHaDcIQnfp8DrV9qTzNm5GpD8PyqnGAAABmf3jqNEAAAQD
AEcwRQIgRXQhl7dwoxjkx7NWAR678ubZaB3fFXLAKdt1Yt3AxXYCIQDKyEyxTyRf
u54cglCG+XUyMDH3Sgyfqv6uK5OUWOAfbjANBgkqhkiG9w0BAQsFAAOCAQEAlcxa
UU01drpj2WUmbxkD076YtgR10JXLk0Lxy8K5dPd5DFFDcw5EiF8oDXGZtvQ91KEl
Ei+lqi7+oifj/lS7u15pMdg5n/EnCIHFysPixmLObRYNjJXpBgKHrVQspVReYxNe
ZwvtJKglvrvmHzLTLUHDeON9q9CkfUwJLHesI3R3fjlSxgpWwoJOnyQv+Csv1zHE
Nb/7JUJVk/vkWwZo/B/cnUc4WBmTD0RUeFKzKZzmy1gCtuAMeT+cPLraJU5zsKXt
pnpIucEvTexYuDbeuvnYckh2pqAALUKo23HJqAh1//HvxR7vkS87+xq/my4chgW+
UVH0XBkbReDupQk2xQ==
-----END CERTIFICATE-----
-----END CERTIFICATE-----
)EOF";

// Fallback público (sem TLS) caso USE_HIVEMQ_CLOUD seja 0
#define MQTT_HOST_FALLBACK "broker.hivemq.com"
#define MQTT_PORT_FALLBACK 1883



// Simulação de período offline (ms) após o boot para evidências de resiliência/flush
#ifndef OFFLINE_SIM_MS
#define OFFLINE_SIM_MS 6000
#endif
