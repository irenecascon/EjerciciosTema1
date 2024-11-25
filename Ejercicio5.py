import threading
import time
import random

# Capacidad máxima del estacionamiento
capacidad = 3
semaforo = threading.Semaphore(capacidad)

def acceder_estacionamiento(id_vehiculo):
    # Intentar acceder al estacionamiento
    print(f"Vehículo {id_vehiculo} está intentando acceder al estacionamiento.")
    semaforo.acquire()
    try:
        # Una vez dentro
        print(f"Vehículo {id_vehiculo} ha entrado al estacionamiento.")
        tiempo_estacionamiento = random.uniform(1, 3)
        time.sleep(tiempo_estacionamiento)  # Simular tiempo dentro del estacionamiento
        print(f"Vehículo {id_vehiculo} ha salido del estacionamiento.")
    finally:
        # Liberar el espacio
        semaforo.release()

# Número total de vehículos
total_vehiculos = 10
hilos = []

# Crear e iniciar un hilo por cada vehículo
for id_vehiculo in range(total_vehiculos):
    hilo = threading.Thread(target=acceder_estacionamiento, args=(id_vehiculo,))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

# Mensaje final
print("Todos los vehículos han pasado por el estacionamiento.")
