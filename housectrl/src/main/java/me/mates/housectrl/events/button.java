package me.mates.housectrl.events;

import me.mates.housectrl.Housectrl;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.block.Block;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerInteractEvent;

import java.util.Objects;

public class button implements Listener {


    private final Housectrl plugin;

    public button(Housectrl plugin) {
        this.plugin = plugin;
    }

    @EventHandler
    public void onButton(PlayerInteractEvent e) {
        Block clicked = e.getClickedBlock();
        if (clicked == null) return;
        World world = clicked.getWorld();
        if (Objects.equals(clicked.getLocation(), new Location(world, 0, 4, -2))) {
            Block block = world.getBlockAt(1, 1, -1);
            if (block.getType().equals(Material.REDSTONE_TORCH)) {
                plugin.getCallback().SEND("closedoor");
            }
            if (block.getType().equals(Material.AIR)) {
                plugin.getCallback().SEND("opendoor");
            }

            e.setCancelled(true);
        }
    }
}
