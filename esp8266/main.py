# main.py -- put your code here!


print('jsem v mainu')
import time
print('spim 5s')
time.sleep(5)
print('vyspano')


from machine import Pin
blue = Pin(5, Pin.OUT)
green = Pin(4, Pin.OUT)
red = Pin(2, Pin.OUT)

def rozni():
  blue.value(1)
  green.value(1)
  red.value(1)

def zhasni():
  blue.value(0)
  green.value(0)
  red.value(0)

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'minecraftbaracek' and msg == b'svetloon':
    print('Svetlo zapnute')
    rozni()
  if topic == b'minecraftbaracek' and msg == b'svetlooff':
    print('Svetlo vypnute')
    zhasni()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub, topic_pub
  client = MQTTClient(client_id, mqtt_server, port=80, keepalive=3600)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  client.publish(topic_pub, b'ESP8266 connected to MQTT broker')
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(2)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()