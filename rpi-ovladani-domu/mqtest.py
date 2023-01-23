from umqtt.simple import MQTTClient

# MQTT broker information
SERVER = "147.228.121.4"
PORT = 80


# Create MQTT client
client = MQTTClient("mates", SERVER, PORT)

# Connect to MQTT broker
if client.connect():
    print("Successfully connected to MQTT broker.")
else:
    print("Failed to connect to MQTT broker.")
    # Exit script
    import sys
    sys.exit()

# Publish a message
if client.publish("topic", "message"):
    print("Successfully published message.")
else:
    print("Failed to publish message.")

# Disconnect from MQTT broker
client.disconnect()