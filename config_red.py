from config_red import conectar_wifi, REDES
import urequests
import time
from machine import Pin
import ujson

# Pines LEDs
led_rojo = Pin(15, Pin.OUT)
led_amarillo = Pin(14, Pin.OUT)
led_verde = Pin(13, Pin.OUT)

# Config Firebase (usa tu SECRET_KEY real o deja vacío si base es pública)
FIREBASE_URL = "https://semaforo-a10b9-default-rtdb.firebaseio.com"
SECRET_KEY = ""  # Deja vacío si base es pública o pon tu clave real

def apagar_todos():
    led_rojo.value(0)
    led_amarillo.value(0)
    led_verde.value(0)

def encender_led(color):
    apagar_todos()
    if color == "rojo":
        led_rojo.value(1)
        print("LED ROJO encendido")
    elif color == "amarillo":
        led_amarillo.value(1)
        print("LED AMARILLO encendido")
    elif color == "verde":
        led_verde.value(1)
        print("LED VERDE encendido")
    else:
        print("Color desconocido:", color)

def actualizar_estado_semaforo(color):
    try:
        url = f"{FIREBASE_URL}/semaforo/estado.json"
        if SECRET_KEY:
            url += f"?auth={SECRET_KEY}"
        data = ujson.dumps({"color": color, "timestamp": time.time()})
        print("Enviando datos a Firebase:", data)
        response = urequests.put(url, data=data)
        print("HTTP status:", response.status_code)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error al actualizar estado en Firebase:", e)

def ciclo_semaforo():
    secuencia = [
        ("rojo", 3),
        ("amarillo", 1),
        ("verde", 3),
        ("amarillo", 1)
    ]
    for color, duracion in secuencia:
        encender_led(color)
        actualizar_estado_semaforo(color)
        time.sleep(duracion)

if conectar_wifi(REDES):
    print("✅ Conectado a WiFi - Iniciando ciclo del semáforo")
    try:
        while True:
            ciclo_semaforo()
    except KeyboardInterrupt:
        print("🛑 Programa detenido")
else:
    print("⚠️ Sin conexión WiFi - Ejecutando ciclo sin actualizar Firebase")
    while True:
        ciclo_semaforo()



