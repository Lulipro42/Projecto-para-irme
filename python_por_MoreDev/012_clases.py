### CLASES ###

# Todo lo que este adentro de la clase tiene que responder a la logica

class MyEmptyPerson: # Los nombres de las classes no se escribe con snake case, ahora es con camel case
    pass # Lo que hace PASS es evitar el error, osea que al no ponerle una clase a una palabra se ejecuta igual al ponerle pass
print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias") -> None: # El __init__ nos sirve para ser un constructor de classes, DEF nos sirve tabien como para crear una funcion
        self.full_name = f"{name} {surname} ({alias})" # o para hacerlo mas corto seria asi
        self.__name = name # Propiedad privada
        
    def get_name (self):
        return self.__name    
        #self.name = name 
        #self.surname = surname # Al hacer SELF se refiere a el mismo osea que si esta adentro de persona se refiere a que esta a dentro ,y si tiene una propiedad como por ej name, se hace esa accion
    def walk (self):
        print(f"{self.full_name} esta en camino") # Mas resumido y mejor estructurado
    
my_person = Person("Ulises", "Solis")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Ulises", "Solis", "LuliPro")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector el loco de los Perros"
print(my_other_person.full_name) 

my_other_person.full_name = "666" # Al ser un tipado fuerte se puede cambiar muy facilmente como por ej seria el 666
print(my_other_person.full_name)