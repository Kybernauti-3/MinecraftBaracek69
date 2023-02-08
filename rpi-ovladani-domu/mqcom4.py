import network
import time
from machine import Pin
import uasyncio as asyncio
import umqtt.simple as simple

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

jmenowifi = "kokot"
heslowifi = "minecraft69"

broker = "broker.hivemq.com"
port = 80
topic = "minecraftbaracek"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(jmenowifi, heslowifi)

while not wlan.isconnected():
    time.sleep(1)

print("Connected to {} IP: {}".format(jmenowifi, wlan.ifconfig()[0]))

async def on_message(topic, msg):
    print("Received message on topic: {}, with payload: {}".format(topic, msg))
    if msg == b"opendoor":
        print("xd")
    elif msg == b"closedoor":
        print("lol")

async def connect_and_subscribe(client, topic):
    client.connect()
    client.subscribe(topic)
    print("Connected to MQTT and subscribed to topic: {}".format(topic))

client = simple.MQTTClient("picomqttclient", broker, port=port)
try:
    asyncio.run(connect_and_subscribe(client, topic))
finally:
    client.disconnect()