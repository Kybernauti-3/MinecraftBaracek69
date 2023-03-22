# boot.py -- run on boot-up

ssid = "D31-lab"
key = "IoT.SPSE.lab22"


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()