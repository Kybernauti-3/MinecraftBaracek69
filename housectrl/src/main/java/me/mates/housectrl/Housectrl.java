package me.mates.housectrl;

import me.mates.housectrl.commands.send;
import me.mates.housectrl.events.button;
import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import java.util.logging.Level;

public final class Housectrl extends JavaPlugin {
    private MqttClient client;
    private MQTT callback;
    private String topic;

    @Override
    public void onEnable() {
        getConfig().options().copyDefaults();
        saveDefaultConfig();

        String broker = getConfig().getString("mqtt.broker");
        String clientId = getConfig().getString("mqtt.clientID");
        topic = getConfig().getString("mqtt.topic");
        try {
            getLogger().log(Level.INFO,"Connecting to broker: " + broker);
            client = new MqttClient(broker, clientId, new MemoryPersistence());
            MqttConnectOptions connOpts = new MqttConnectOptions();
            connOpts.setCleanSession(true);
            client.connect(connOpts);
            callback = new MQTT(this);
            client.setCallback(callback);
            client.subscribe(topic, 1);
            getLogger().log(Level.INFO,"Connected");
        } catch (MqttException me) {
            Bukkit.getPluginManager().disablePlugin(this);
            me.printStackTrace();
        }

        getCommand("send").setExecutor(new send(this));

        Bukkit.getPluginManager().registerEvents(new button(this), this);
    }

    @Override
    public void onDisable() {
        try {
            client.disconnect();
        } catch (MqttException me) {
            me.printStackTrace();
        }
        getLogger().log(Level.INFO,"Disconnected");
    }

    public MqttClient getClient() {
        return client;
    }

    public MQTT getCallback() {
        return callback;
    }

    public String getTopic() {
        return topic;
    }
}
