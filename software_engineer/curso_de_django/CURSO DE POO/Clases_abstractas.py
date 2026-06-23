# LAS CLASES ABSTRACTAS ES CREAR PLANTILLAS, PARA PODER CREAR CLASES A PARTIR DE ESAS PLANTILLAS  
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass 
    
    def hablar(self):
        print("habla")

class Perro(Animal):
    def hablar(self):
        print("Woof!")
        
class Gato(Animal):
    def hablar(self):
        print("Meow!")
        
perro = Perro()
perro.hablar()
gato = Gato()
gato.hablar()

animal = Animal() # CON ESTO LO INSTANCIO PERO AL HACER ESO PIERDE TODO EL SENTIDO DEBIDO A QUE SON CLASES ABSTRACTAS

animal.hablar()