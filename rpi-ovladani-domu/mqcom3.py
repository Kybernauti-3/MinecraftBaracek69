
from machine import Pin
import uasyncio as asyncio
from mqtt_as import MQTTClient, config

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

jmenowifi = "kokot"
heslowifi = "minecraft69"

broker = "broker.hivemq.com"
port = 1883
topic = "minecraftbaracek"

config['server'] = broker
config['port'] = port
config['ssid'] = jmenowifi
config['wifi_pw'] = heslowifi

async def on_message(topic, msg):
    print("Received message on topic: {}, with payload: {}".format(topic, msg))
    if msg == b"opendoor":
        print("xd")
    elif msg == b"closedoor":
        print("lol")

async def main(client):
   

    # Connect to MQTT broker
    await client.connect()
    print("Connected to MQTT")

    await client.publish(topic, b"Pico connected")
    await client.subscribe(topic, on_message)

client = MQTTClient(config)
try:
    asyncio.run(main(client))
finally:
    client.close()