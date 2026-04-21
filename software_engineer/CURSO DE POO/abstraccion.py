# LA ABSTRACCIÓN consiste en ocultar la complejidad lógica interna de un objeto
# y exponer solo los métodos necesarios para que el usuario pueda interactuar con él.

class Auto():
    def __init__(self):
        self._estado = "apagado" # Atributo interno (el usuario no necesita tocarlo)
        
    def encender(self):
        self._estado = "encendido"
        print(f"El auto esta encendido")
        
    def conducir(self):
        # El usuario solo quiere conducir. 
        # La lógica de verificar si está encendido es "abstracta" para él.
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto")
        
mi_auto = Auto()
# El usuario no tiene que encenderlo manualmente, la interfaz (conducir) lo resuelve.
mi_auto.conducir()