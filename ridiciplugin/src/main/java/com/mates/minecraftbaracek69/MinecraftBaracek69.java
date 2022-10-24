package com.mates.minecraftbaracek69;

import org.bukkit.ChatColor;
import org.bukkit.plugin.java.JavaPlugin;

public final class MinecraftBaracek69 extends JavaPlugin {

    @Override
    public void onEnable() {
        System.out.println(ChatColor.GREEN + "Plugin zapnut");

    }

    @Override
    public void onDisable() {
        System.out.println(ChatColor.YELLOW + "Plugin vypnut");

    }
}
