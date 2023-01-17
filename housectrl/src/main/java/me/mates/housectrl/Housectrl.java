package me.mates.housectrl;

import me.mates.housectrl.commands.svetlo;
import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public final class Housectrl extends JavaPlugin {
    MqttClient sampleClient = null;
    private Housectrl plugin;

    @Override
    public void onEnable() {
        plugin = this;
        String broker       = "tcp://147.228.121.4:80";
        String clientId     = "minecraftplugin";
        try {
            System.out.println("Connecting to broker: " + broker);
            sampleClient = new MqttClient(broker, clientId, new MemoryPersistence());
            System.out.println("Connected");
        } catch (MqttException me) {
            Bukkit.getPluginManager().disablePlugin(this);
            me.printStackTrace();
        }
        new MQTT(this);

        getCommand("svetlo").setExecutor(new svetlo());

    }

    @Override
    public void onDisable() {
        try {
            sampleClient.disconnect();
        } catch (MqttException me) {
            me.printStackTrace();
        }
        System.out.println("Disconnected");
    }

    public MqttClient getClient() {
        return sampleClient;
    }
}
