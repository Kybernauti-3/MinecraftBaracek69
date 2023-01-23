package me.mates.housectrl;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MQTT {
    private static Housectrl plugin;

    public MQTT(Housectrl housectrl) {
        plugin = housectrl;
    }

    public static void SEND(String content) {
        if (content == null) return;
        String topic        = "minecraftbaracek";

        try {
            MqttClient sampleClient = plugin.getClient();
            System.out.println("Publishing message: "+content);
            MqttMessage message = new MqttMessage(content.getBytes());
            message.setQos(2);
            sampleClient.publish(topic, message);
            System.out.println("Message published");
        } catch(MqttException me) {
            System.out.println("reason "+me.getReasonCode());
            System.out.println("msg "+me.getMessage());
            System.out.println("loc "+me.getLocalizedMessage());
            System.out.println("cause "+me.getCause());
            System.out.println("excep "+me);
            me.printStackTrace();
        }
    }
}
