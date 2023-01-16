#from housectrl import dvere_otevrit,dvere_zavrit

import network
from umqtt.simple import MQTTClient

# 147.228.121.4:80

broker = 'broker.hivemq.com'
topic = "minecraftbaracek"

def on_message(topic, msg):
    print("Received message on topic: {}, with payload: {}".format(topic, msg))


def main():
    # Connect to Wi-Fi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("kokot", "minecraft69")
    print("pripojuji wajfaj")
    while not wlan.isconnected():
        pass
    print("pripojeno wajfaj")
    # Connect to MQTT broker
    client = MQTTClient("Pico", "147.228.121.4", port = 80)
    client.connect()
    print("pripojeno mqtt")

    # Publish a message to an MQTT topic
    client.publish(topic, b"Hello, MQTT!")
    #client.disconnect()

    while True:
        # Check for incoming messages
        #client.check_msg()
        pass

main()