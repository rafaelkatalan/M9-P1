import time
import random
import paho.mqtt.client as mqtt
import json

# MQTT Broker settings
broker_address = "localhost"
port = 1891
topic = "data"

# Function to simulate sensor readings
def generate_sensor_data():
    temp_freezer = round(random.uniform(-30, -10),2)
    temp_geladeira = round(random.uniform(-3, 15), 2)

    return {
        "temp_freezer": temp_freezer,
        "temp_geladeira": temp_geladeira
    }

# Function to publish sensor data to MQTT
def publish_sensor_data(client):
    while True:
        sensor_data = generate_sensor_data()
        loja = (random.choice([1,2,3]))
        msg1 = {"id": f'lj0{loja}', "tipo": "freezer", "temperatura": sensor_data["temp_freezer"], "timestamp": f"{time.strftime('%d/%m/%Y %H:%M:%S')}"}
        msg2 = {"id": f'lj0{loja}', "tipo": "geladeira", "temperatura": sensor_data["temp_geladeira"], "timestamp": f"{time.strftime('%d/%m/%Y %H:%M:%S')}"}
        client.publish(topic, json.dumps(msg1), qos=1)
        print(f"Published: {sensor_data}")
        client.publish(topic, json.dumps(msg2), qos=1)
        time.sleep(3)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(broker_address, port, 60)

try:
    publish_sensor_data(client)
except KeyboardInterrupt:
    client.disconnect()
    print("Simulation stopped.")
