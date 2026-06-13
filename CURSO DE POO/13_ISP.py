# PRINCIPIO DE SEGREGACIÓN DE INTERFAZ (ISP)
# El principio ISP dice que ninguna clase debería ser forzada a implementar 
# métodos que no necesita. Es mejor crear interfaces pequeñas y específicas.

from abc import ABC, abstractmethod

# --- PROBLEMA (Violando ISP) ---
# Si creamos una interfaz "Trabajador" muy grande, obligamos a todos a hacer todo.
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self): pass
    
    @abstractmethod
    def comer(self): pass

class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")
    
    def comer(self):
        # ¡PROBLEMA! Un robot no come. Estamos obligados a implementar algo inútil.
        pass

# --- SOLUCIÓN (Siguiendo ISP) ---
# Dividimos la interfaz grande en interfaces más pequeñas y específicas.

class TrabajadorAccion(ABC):
    @abstractmethod
    def trabajar(self): pass

class ComedorAccion(ABC):
    @abstractmethod
    def comer(self): pass

# El Humano necesita ambas, así que hereda de las dos (Herencia Múltiple)
class Humano(TrabajadorAccion, ComedorAccion):
    def trabajar(self): print("El humano trabaja")
    def comer(self): print("El humano come")

# El Robot solo necesita trabajar, no lo obligamos a "comer"
class RobotInteligente(TrabajadorAccion):
    def trabajar(self): print("El robot trabaja eficientemente")

robot = RobotInteligente()
robot.trabajar()

juan = Humano()
juan.comer()