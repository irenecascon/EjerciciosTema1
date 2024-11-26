import threading
import time
import random

capacidad = 3
semaforo = threading.Semaphore(capacidad)

def acceder_estacionamiento(id_vehiculo):
    print(f"Vehículo {id_vehiculo} está intentando acceder al estacionamiento.")
    semaforo.acquire()
    try:
        print(f"Vehículo {id_vehiculo} ha entrado al estacionamiento.")
        tiempo_estacionamiento = random.uniform(1, 3)
        time.sleep(tiempo_estacionamiento)  # Simular tiempo dentro del estacionamiento
        print(f"Vehículo {id_vehiculo} ha salido del estacionamiento.")
    finally:
        semaforo.release()

total_vehiculos = 10
hilos = []

for id_vehiculo in range(total_vehiculos):
    hilo = threading.Thread(target=acceder_estacionamiento, args=(id_vehiculo,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()


print("Todos los vehículos han pasado por el estacionamiento.")
