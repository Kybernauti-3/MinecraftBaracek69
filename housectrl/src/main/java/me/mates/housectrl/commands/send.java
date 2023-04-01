package me.mates.housectrl.commands;

import me.mates.housectrl.Housectrl;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.command.TabExecutor;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.util.List;

public class send implements CommandExecutor, TabExecutor {
    private final Housectrl plugin;
    public send(Housectrl plugin) {
        this.plugin = plugin;
    }
    @Override
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) {

        Player player = (Player) sender;

        if (args.length == 1) {
            plugin.getCallback().SEND(args[0]);
            player.sendMessage("Posilam zpravu: " + args[0]);
            return true;
        }
        System.out.println("provide args pls");
        return true;
    }

    @Override
    public @Nullable List<String> onTabComplete(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) {
        return null;
    }
}
