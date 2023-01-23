package me.mates.housectrl;

import org.bukkit.Bukkit;
import org.eclipse.paho.client.mqttv3.*;

public class MQTT implements MqttCallback {
    private static Housectrl plugin;

    public MQTT(Housectrl housectrl) {
        plugin = housectrl;
    }

    public static void SEND(String content) {
        if (content == null) return;

        String topic = plugin.getConfig().getString("mqtt.topic");

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

    @Override
    public void connectionLost(Throwable cause) {

    }

    @Override
    public void messageArrived(String topic, MqttMessage message) {
        System.out.println("topic " + topic);
        System.out.println("message " + message);
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken token) {
        System.out.println("token" + token);
    }
}
