# Evidência de Conectividade MQTT

Este arquivo registra o resultado bem-sucedido do teste de conexão e publicação de dados no broker HiveMQ Cloud, executado em 23/10/2025.

O teste foi realizado utilizando o script `tools/test_mqtt_publish.py` com as credenciais fornecidas.

## Log de Execução

```
> python FASE3/tools/test_mqtt_publish.py --host 817c2430152f460ba0cb75228198eb57.s1.eu.hivemq.cloud --username cardioia-client --password [REDACTED]

Connected rc= 0
Publish cardioia/grupo1/vitals {"ts": 1761260443, "temp": 36.65, "hum": 56.0, "bpm": 125}
Publish cardioia/grupo1/vitals {"ts": 1761260445, "temp": 38.08, "hum": 57.9, "bpm": 80}
Publish cardioia/grupo1/vitals {"ts": 1761260446, "temp": 36.7, "hum": 58.3, "bpm": 75}
Publish cardioia/grupo1/vitals {"ts": 1761260448, "temp": 36.65, "hum": 57.5, "bpm": 72}
Publish cardioia/grupo1/vitals {"ts": 1761260449, "temp": 37.61, "hum": 56.1, "bpm": 125}
```

O resultado `Connected rc= 0` confirma que a conexão TLS com o broker foi estabelecida com sucesso e as mensagens foram publicadas no tópico `cardioia/grupo1/vitals`.
