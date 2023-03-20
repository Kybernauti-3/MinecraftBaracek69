#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "D31-lab";
const char* password = "IoT.SPSE.lab22";
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
const char* mqtt_topic = "minecraftbaracek";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  Serial.begin(115200);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
 
  Serial.println("Connected to WiFi");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, mqtt_port);
  client.setCallback(callback);
};

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
};

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Received message on topic: ");
  Serial.print(topic);
  Serial.print(", with payload: ");
  Serial.write(payload, length);
  Serial.println();

  if (strcmp((char*)payload, "opendoor") == 0) {
    Serial.println("xd");
  }
  else if (strcmp((char*)payload, "closedoor") == 0) {
    Serial.println("lol");
  }
};

void reconnect() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT broker...");
    if (client.connect("esp8266client")) {
      Serial.println("Successfully connected to MQTT broker.");
      client.subscribe(mqtt_topic);
      client.publish(mqtt_topic, "hello");
    } else {
      Serial.print("Failed to connect to MQTT broker, rc=");
      Serial.print(client.state());
      Serial.println(" retrying in 5 seconds");
      delay(5000);
    }
  }
};
