from umqtt.simple import MQTTClient

# MQTT broker information
broker = 'broker.hivemq.com'
PORT = 1883


# Create MQTT client
client = MQTTClient("mates", broker, PORT)

# Connect to MQTT broker
if client.connect():
    print("Successfully connected to MQTT broker.")
else:
    print("Failed to connect to MQTT broker.")
    # Exit script
    import sys
    sys.exit()

# Publish a message
if client.publish("minecraftbaracek", "opendoor"):
    print("Successfully published message.")
else:
    print("Failed to publish message.")

# Disconnect from MQTT broker
client.disconnect()