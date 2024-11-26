
import threading
import time
import random

# Crear el evento que representa la señal de salida
salida_evento = threading.Event()


def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posición, esperando señal de salida...")
    salida_evento.wait()  # Esperar hasta que se active el evento
    print(f"Corredor {id_corredor} ha comenzado a correr.")
    tiempo_carrera = random.uniform(1, 3)  # Tiempo de carrera aleatorio entre 1 y 3 segundos
    time.sleep(tiempo_carrera)  # Simular el tiempo de carrera
    print(f"Corredor {id_corredor} ha llegado a la meta.")

def iniciar_carrera():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)  # Pausa de 2 segundos antes de dar la salida
    salida_evento.set()  # Activar el evento
    print("¡Salida! Los corredores han comenzado.")

hilos_corredores = []
for i in range(5):  # 5 corredores
    hilo = threading.Thread(target=corredor, args=(i,))
    hilos_corredores.append(hilo)
    hilo.start()

iniciar_carrera()

for hilo in hilos_corredores:
    hilo.join()

print("La carrera ha finalizado.")

