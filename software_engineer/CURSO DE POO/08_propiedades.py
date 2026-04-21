class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
        
    @property # ESTO LO QUE HACE ES QUE COMPRENDE QUE ES LO QUE ESTA ABAJO POR ENDE NO ES NECESARIO QUE HAGAS UNA FUNCION OSEA PONER PARENTESIS LO CONVIERTE EN PROPIEDAD
    def nombre(self):
        return self._nombre
        
    @nombre.setter  # ESTO LO QUE HACE ES QUE NOP CREA DOS METODOS EN UNA CLASE LO QUE HACE ES QUE CREA DOS DECORADORES DIFERENTES  
    def nombre(self, new_nombre):
        self._nombre = new_nombre
    
    
ulises = Persona("ulises", 17)

nombre = ulises.nombre
print(nombre)

ulises.nombre = "Pepe"

nombre = ulises.nombre
print(nombre)



del ulises._nombre # Nota: Esto elimina el atributo interno, no la propiedad.

print("Que haces down vas a llegar a japon con un par de wachas ")