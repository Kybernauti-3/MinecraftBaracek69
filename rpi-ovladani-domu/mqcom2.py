import network
import paho.mqtt.client as mqtt
from machine import Pin
import time

led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

jmenowifi = "Jirankovi_O2_2,4GHz"
heslowifi = "jirankovi7475"

broker = "147.228.121.4"
port = 80
topic = "minecraftbaracek"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print("Received message on topic: {}, with payload: {}".format(msg.topic, msg.payload))
    if msg.payload == b"opendoor":
        print("xd")
    elif msg.payload == b"closedoor":
        print("lol")

def main():
    # Connect to Wi-Fi
    print("Pripojuji k WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(jmenowifi, heslowifi)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('Cekam na pripojeni...')
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
        print( 'Pripojeno k ' + jmenowifi + ' ' + 'IP: ' + status[0] )

    # Connect to MQTT broker
    client = mqtt.Client("pico")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.loop_start()

    client.publish(topic, "Pico connected")

    while True:
        pass

main()