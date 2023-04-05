# main.py -- put your code here!

import time
print('waiting 5s...')
time.sleep(5)


from machine import Pin, PWM
red = Pin(14, Pin.OUT)
green = Pin(4, Pin.OUT)
blue = Pin(2, Pin.OUT)

tlacitko = Pin(9, Pin.IN, Pin.PULL_UP)
stav = 0

servo = PWM(Pin(13),freq=50)

def dvere_otevrit():
  print("pohyb servem 1")
  servo.duty(90)

def dvere_zavrit():
  print("pohyb servem 2")
  servo.duty(40)

def door_switch(stav):
    if(stav == 1):
      client.publish(topic_pub, b'closedoor')
    else:
      client.publish(topic_pub, b'opendoor')
    return not stav

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
  if topic == b'minecraftbaracek' and msg == b'opendoor':
    dvere_otevrit()
  if topic == b'minecraftbaracek' and msg == b'closedoor':
    dvere_zavrit()

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
    if not tlacitko.value():
      stav = door_switch(stav)
      time.sleep(0.1)
      while not tlacitko.value():
        pass
    
  except OSError as e:
    restart_and_reconnect()