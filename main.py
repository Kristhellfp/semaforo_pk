# config_red.py
REDES = {
    "CLARO_qazxJ2": "498EFD922D",
    "iPhone Daniaa": "luna1907!!"
}

def conectar_wifi(redes):
    import network
    import time
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    for ssid, password in redes.items():
        print(f"Intentando conectar a {ssid}...")
        wlan.connect(ssid, password)
        for _ in range(15):
            if wlan.isconnected():
                print(f"Conectado a {ssid}")
                print("IP:", wlan.ifconfig()[0])
                return True
            time.sleep(1)
        print(f"No se pudo conectar a {ssid}")
    return False


