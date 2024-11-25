import threading
import time
import random

# Clase que hereda de Thread para procesar archivos
class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre_archivo, num_lineas):
        super().__init__()
        self.nombre_archivo = nombre_archivo
        self.num_lineas = num_lineas

    def run(self):
        for i in range(1, self.num_lineas + 1):
            # Simular el procesamiento de una línea con una pausa aleatoria
            time.sleep(random.uniform(0.1, 0.5))
            print(f"Procesando {self.nombre_archivo} - Línea {i}")

# Lista de nombres de archivos
archivos = [
    ("archivo1.txt", 3),
    ("archivo2.txt", 4),
    ("archivo3.txt", 2),
    ("archivo4.txt", 5),
    ("archivo5.txt", 3),
]

# Lista para almacenar los hilos
hilos = []

# Crear e iniciar un hilo por cada archivo
for nombre_archivo, num_lineas in archivos:
    hilo = ProcesadorArchivo(nombre_archivo, num_lineas)
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Mensaje final
print("Todos los archivos han sido procesados.")
