import firebase_admin
from firebase_admin import credentials, db
import time

# Carga la clave JSON descargada desde Firebase Console
cred = credentials.Certificate("clave.json")

# Inicializa Firebase con la URL de tu base de datos
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://semaforo-a10b9-default-rtdb.firebaseio.com/'
})

ref = db.reference('semaforo/estado')

def cambiar_color(color):
    print(f"Encendiendo {color.upper()}")
    try:
        ref.set({
            'color': color,
            'timestamp': int(time.time() * 1000)
        })
    except Exception as e:
        print("❌ Error al actualizar estado:", e)

# Ciclo infinito cambiando el color cada 3 segundos
while True:
    cambiar_color("rojo")
    time.sleep(3)
    cambiar_color("amarillo")
    time.sleep(2)
    cambiar_color("verde")
    time.sleep(3)
