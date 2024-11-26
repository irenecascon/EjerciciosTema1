import threading

estado = 1  # 1: Preparación, 2: Procesamiento, 3: Empaque
iteraciones_totales = 5  # Número total de ciclos de producción

condition = threading.Condition()

def preparacion():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 1)
            print(f"Preparación {i} completada")
            estado = 2
            condition.notify_all()

def procesamiento():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 2)
            print(f"Procesamiento {i} completado")
            estado = 3
            condition.notify_all()

def empaque():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 3)
            print(f"Empaque {i} completado")
            estado = 1
            condition.notify_all()


hilo_preparacion = threading.Thread(target=preparacion)
hilo_procesamiento = threading.Thread(target=procesamiento)
hilo_empaque = threading.Thread(target=empaque)

hilo_preparacion.start()
hilo_procesamiento.start()
hilo_empaque.start()

hilo_preparacion.join()
hilo_procesamiento.join()
hilo_empaque.join()

print("Producción completada.")
