import network
import time
from machine import Pin
import uasyncio as asyncio
import umqtt.simple as simple

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

jmenowifi = "D31-lab"
heslowifi = "IoT.SPSE.lab22"

broker = "broker.hivemq.com"
port = 1883
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


client = simple.MQTTClient("picomqttclient", broker, port=port)

if client.connect():
    print("Successfully connected to MQTT broker.")
    client.set_callback(on_message)
    client.publish(topic, "hello")
    client.subscribe(topic)
else:
    print("Failed to connect to MQTT broker.")

while True:
    client.loop()