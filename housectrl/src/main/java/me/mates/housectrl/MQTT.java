package me.mates.housectrl;

import org.bukkit.Bukkit;
import org.bukkit.Material;
import org.bukkit.World;
import org.eclipse.paho.client.mqttv3.*;

import java.util.logging.Level;
import java.util.logging.Logger;

public class MQTT implements MqttCallback {
    private final Housectrl plugin;
    private final MqttClient client;
    private final World world = Bukkit.getWorld("World");
    private final Logger logger;

    public MQTT(Housectrl plugin) {
        this.plugin = plugin;
        logger = plugin.getLogger();
        client = plugin.getClient();
    }

    public void SEND(String content) {
        if (content == null) return;
        try {
            logger.log(Level.INFO,"Publishing message: " + content);
            MqttMessage message = new MqttMessage(content.getBytes());
            message.setQos(2);
            client.publish(plugin.getTopic(), message);
            logger.log(Level.INFO,"Message published");
        } catch (MqttException me) {
            logger.log(Level.INFO,"reason " + me.getReasonCode());
            logger.log(Level.INFO,"msg " + me.getMessage());
            logger.log(Level.INFO,"loc " + me.getLocalizedMessage());
            logger.log(Level.INFO,"cause " + me.getCause());
            logger.log(Level.INFO,"excep " + me);
            me.printStackTrace();
        }
    }

    @Override
    public void connectionLost(Throwable cause) {

    }

    @Override
    public void messageArrived(String topic, MqttMessage message) {
        Bukkit.getScheduler().runTask(plugin, () -> {
            switch (message.toString().toLowerCase()) {
                case "opendoor" -> world.getBlockAt(1,1,-1).setType(Material.REDSTONE_TORCH);
                case "closedoor" -> world.getBlockAt(1,1,-1).setType(Material.AIR);
                case "svetloon" -> world.getBlockAt(1,7,1).setType(Material.REDSTONE_BLOCK);
                case "svetlooff" -> world.getBlockAt(1,7,1).setType(Material.AIR);

                default -> {
                }
            }
        });

        logger.log(Level.INFO,"topic " + topic);
        logger.log(Level.INFO,"message " + message);
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken token) {
        logger.log(Level.INFO,"token" + token);
    }
}
