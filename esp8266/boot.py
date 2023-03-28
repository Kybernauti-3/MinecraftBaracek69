# boot.py -- run on boot-up

# Complete project details at https://RandomNerdTutorials.com

import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

time.sleep(5)

def connect_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    while True:
        user_input = input("\n[1] - wifi ve skole\n[2] - wifi mates home\n[3] - neco jineho\n")
        if user_input == '1':
            ssid = "D31-lab"
            password = "IoT.SPSE.lab22"
            break
        if user_input == '2':
            ssid = "Jirankovi_O2_2,4GHz"
            password = "jirankovi7475"
            break
        elif user_input == '3':
            ssid = input("Enter SSID: ")
            password = input("Enter password: ")
            break
        else:
            print("Invalid input. Please try again.")

    station = network.WLAN(network.STA_IF)

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print('\nConnection successful')
    print(station.ifconfig())

connect_wifi()

mqtt_server = '147.228.121.4'

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'minecraftbaracek'
topic_pub = b'minecraftbaracek'

