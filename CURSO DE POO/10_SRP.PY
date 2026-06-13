class Auto():
    def __init__(self, tanque):
        self.posicion = 0 
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2: 
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2) 
        else:
            print("No hay suficiente combustible")
            
            
    def obtener_posicion(self):
        return self.posicion
            
    
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
        
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
        
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(f"Posición inicial: {autito.obtener_posicion()}")
autito.mover(10)
print(f"Posición tras mover 10: {autito.obtener_posicion()}")
autito.mover(20)
print(f"Posición tras mover 20: {autito.obtener_posicion()}")
autito.mover(30)
print(f"Posición tras mover 30: {autito.obtener_posicion()}")
autito.mover(900)
print(f"Posición tras mover 70: {autito.obtener_posicion()}")
