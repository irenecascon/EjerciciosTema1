import threading

# Contador para el estado del sistema
estado = 1  # 1: Preparación, 2: Procesamiento, 3: Empaque
iteraciones_totales = 5  # Número total de ciclos de producción

# Objeto Condition para sincronización
condition = threading.Condition()

# Función para la tarea de preparación
def preparacion():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 1)
            print(f"Preparación {i} completada")
            estado = 2
            condition.notify_all()

# Función para la tarea de procesamiento
def procesamiento():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 2)
            print(f"Procesamiento {i} completado")
            estado = 3
            condition.notify_all()

# Función para la tarea de empaque
def empaque():
    global estado
    for i in range(1, iteraciones_totales + 1):
        with condition:
            condition.wait_for(lambda: estado == 3)
            print(f"Empaque {i} completado")
            estado = 1
            condition.notify_all()

# Crear los hilos
hilo_preparacion = threading.Thread(target=preparacion)
hilo_procesamiento = threading.Thread(target=procesamiento)
hilo_empaque = threading.Thread(target=empaque)

# Iniciar los hilos
hilo_preparacion.start()
hilo_procesamiento.start()
hilo_empaque.start()

# Esperar a que todos los hilos terminen
hilo_preparacion.join()
hilo_procesamiento.join()
hilo_empaque.join()

# Mensaje final
print("Producción completada.")
