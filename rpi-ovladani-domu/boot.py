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

ssid = "Jirankovi_O2_2,4GHz"
password = "jirankovi7475"
#ssid = "D31-lab"
#password = "IoT.SPSE.lab22"

mqtt_server = '147.228.121.4'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.1.144'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'minecraftbaracek'
topic_pub = b'minecraftbaracek'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('\nConnection successful')
print(station.ifconfig())
