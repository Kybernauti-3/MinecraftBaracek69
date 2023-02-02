import network
import time
from machine import Pin
import uasyncio as asyncio
from mqtt_as import MQTTClient

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

jmenowifi = "kokot"
heslowifi = "minecraft69"

broker = "147.228.121.4"
port = 80
topic = "minecraftbaracek"

async def on_message(topic, msg):
    print("Received message on topic: {}, with payload: {}".format(topic, msg))
    if msg == b"opendoor":
        print("xd")
    elif msg == b"closedoor":
        print("lol")

async def main(client):
    # Connect to Wi-Fi
    print("Connecting to WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(jmenowifi, heslowifi)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('Waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        s = 3
        while s > 0:
            s -= 1
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.5)

        status = wlan.ifconfig()
        print('Connected to ' + jmenowifi + ' ' + 'IP: ' + status[0] )

    # Connect to MQTT broker
    await client.connect()
    print("Connected to MQTT")

    await client.publish(topic, b"Pico connected")
    await client.subscribe(topic, on_message)

loop = asyncio.get_event_loop()
client = MQTTClient(config={
    "broker": broker,
    "port": port,
})
loop.run_until_complete(main(client))
loop.run_forever()