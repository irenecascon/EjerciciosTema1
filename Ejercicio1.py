
import time
import random
import threading

def procesar_usuario (idUsuario, **kwargs):
    nombre = kwargs.get('nombre', 'Desconocido')
    edad = kwargs.get('edad', "Desconocida")
    time.sleep(random.uniform(0.5, 2))
    print(f"id del Usuario: {idUsuario}, Nombre: {nombre}, Edad: {edad}")

usuarios = [
    (1, {"nombre": "Ana", "edad": 30}),
    (2, {"nombre": "Carlos", "edad": 22}),
    (3, {"nombre": "Beatriz", "edad": 27}),
    (4, {"nombre": "David", "edad": 35}),
    (5, {"nombre": "Elena", "edad": 29}),
  ]

hilos = []


for idUsuario, usuario in usuarios:
      hilo = threading.Thread(target=procesar_usuario, args=(idUsuario,), kwargs = usuario)
      hilos.append(hilo)
      hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los usuarios han sido procesados")