import threading

class SesionUsuario:
    def __init__(self):
        self.nombre_usuario = None
    def iniciar_sesion(self,nombre_usuario):
        self.nombre_usuario = nombre_usuario
    def mostrar_sesion(self):
        print(f"Usuario iniciado: {self.nombre_usuario}")


datos_usuario = threading.local

def gestionar_sesion(nombre_usuario):
    usuario = SesionUsuario()
    usuario.iniciar_sesion(nombre_usuario)
    usuario.mostrar_sesion()

nombres_usuarios = ["Ana", "Lola", "Mario", "Jorge"]

hilos = []

for nombre in nombres_usuarios:
    hilo = threading.Thread(target=gestionar_sesion, args =(nombre,))
    hilos.append(hilo)
    hilo.start()
for hilo in hilos:
    hilo.join()
print("Todas las sesiones gestionadas")
