import paho.mqtt.client as mqtt
import json

# MQTT Broker settings
broker_address = "localhost"
port = 1891
topic = "data"

# Callback when a message is received
def on_message(client, userdata, msg):
     msg_data = json.loads(msg.payload.decode())
     alerta = ""
     if msg_data["tipo"] == "freezer":
         if msg_data["temperatura"] > -15:
             alerta = "Temperatura muito alta"
         if msg_data["temperatura"] < -25:
             alerta = "Temperatura muito baixa"    
     if msg_data["tipo"] == "geladeira":
         if msg_data["temperatura"] > 10:
             alerta = "Temperatura muito alta"
         if msg_data["temperatura"] < 2:
             alerta = "Temperatura muito baixa"      
     print(f"Loja {str(msg_data['id'])[-2:]}: {msg_data['tipo']}; Temperatura = {msg_data['temperatura']}°C - Timestamp: {msg_data['timestamp']} || {alerta}")

# MQTT setup and connection
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.on_message = on_message
client.connect(broker_address, port, 60)

# Subscribe to the topic
client.subscribe(topic)

# Start the MQTT loop to receive messages
try:
    print(f"Subscribed to topic {topic}")
    client.loop_forever()
except KeyboardInterrupt:
    # Gracefully handle interrupt (Ctrl+C) to disconnect from MQTT broker
    client.disconnect()
    print("\nSubscriber stopped.")
