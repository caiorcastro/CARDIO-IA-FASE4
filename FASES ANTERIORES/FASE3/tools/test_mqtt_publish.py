import os
import ssl
import time
import json
import random
import argparse
from paho.mqtt import client as mqtt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default=os.getenv("MQTT_HOST", "817c2430152f460ba0cb75228198eb57.s1.eu.hivemq.cloud"))
    ap.add_argument("--port", type=int, default=int(os.getenv("MQTT_PORT", "8883")))
    ap.add_argument("--username", default=os.getenv("MQTT_USERNAME"))
    ap.add_argument("--password", default=os.getenv("MQTT_PASSWORD"))
    ap.add_argument("--topic", default=os.getenv("MQTT_TOPIC", "cardioia/grupo1/vitals"))
    ap.add_argument("--count", type=int, default=5)
    args = ap.parse_args()

    if not args.username or not args.password:
        raise SystemExit("Defina --username/--password ou variáveis MQTT_USERNAME/MQTT_PASSWORD")

    cid = f"cardioia-test-{int(time.time())}"
    client = mqtt.Client(client_id=cid, protocol=mqtt.MQTTv311)
    client.username_pw_set(args.username, args.password)
    ctx = ssl.create_default_context()
    client.tls_set_context(ctx)

    def on_connect(c, u, flags, rc):
        print("Connected rc=", rc)

    client.on_connect = on_connect
    client.connect(args.host, args.port, keepalive=60)
    client.loop_start()
    time.sleep(1)
    for i in range(args.count):
        payload = {
            "ts": int(time.time()),
            "temp": round(36.5 + random.random() * 2.0, 2),
            "hum": round(55 + random.random() * 5, 1),
            "bpm": random.choice([72, 75, 80, 125])
        }
        j = json.dumps(payload, ensure_ascii=False)
        print("Publish", args.topic, j)
        client.publish(args.topic, j, qos=0)
        time.sleep(1.5)
    client.loop_stop()
    client.disconnect()


if __name__ == "__main__":
    main()

