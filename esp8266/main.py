# main.py -- put your code here!

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'minecraftbaracek' and msg == b'svetloon':
    print('Svetlo zapnute')

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