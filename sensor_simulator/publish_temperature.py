import ssl
import json
import time
import random
from datetime import datetime

import paho.mqtt.client as mqtt

# AWS IoT Endpoint
ENDPOINT = "a1e0rfe04pcac-ats.iot.us-east-1.amazonaws.com"

# Sertifika yolları
PATH_TO_CERT = "../certificates/39d8bcbc07caf30ece378072d0f8ab1977fed6de4f52ff6cb72bbd1ab22cbe16-certificate.pem.crt"

PATH_TO_KEY = "../certificates/39d8bcbc07caf30ece378072d0f8ab1977fed6de4f52ff6cb72bbd1ab22cbe16-private.pem.key"

PATH_TO_ROOT = "../certificates/AmazonRootCA1.pem"

# MQTT Topic
TOPIC = "smartcity/temperature"

# MQTT Client
client = mqtt.Client()

# TLS/SSL Ayarları
client.tls_set(
    ca_certs=PATH_TO_ROOT,
    certfile=PATH_TO_CERT,
    keyfile=PATH_TO_KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

print("AWS IoT Core bağlantısı kuruluyor...")

client.connect(ENDPOINT, 8883)

print("Bağlantı başarılı!")

locations = [
    "Merkez",
    "Universite",
    "Park",
    "Sanayi",
    "OtobusDuragi"
]

while True:
    data = {
        "device_id": f"sensor_{random.randint(1,5)}",
        "location": random.choice(locations),
        "temperature": round(random.uniform(20, 40), 2),
        "timestamp": datetime.now().isoformat()
    }

    message = json.dumps(data)

    client.publish(TOPIC, message)

    print(f"Gonderildi: {message}")

    time.sleep(5)