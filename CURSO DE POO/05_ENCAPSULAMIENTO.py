# SIRVE PARA LA ILEGIBIDAD DEL CODIGO, CONSISTE EN PROTEJER LOS ELEMENTOS DE UNA CLASE 
class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor" # AL PONERLE UN SOLO GUION BAJO ES UN ATRIBUTO PRIVADO, NIVEL BAJO OSEA NORMAL, QUE SI ALGUIEN QUIERE ACCEDER PUDE HACERLO Y AL PONERLE DOS GUIONES BAJOS ES SUPER PRIVADO,OSEA NO PUEDO ACCEDER EN CAMBIO QUE SEPA
        # y para acceder tenemos que saber utilizar GETERS Y SETTERS
        
    def _hablar(self): # TAMBIEN SE PUEDE HACER CON EL PRINT OSEA "_hablar" O "__hablar"
        print("Hola, como estas")
objeto = MiClase() 
print(objeto._hablar())



class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre # Y AL PONERLE LOS GUIONES BAJOS NO PODES ACCEDER
        self._edad = edad
    
    def get_nombre(self): # GET ES COMO OBTENERLO OSEA ACCEDE A LA PROPIEDAD QUE SUPUESTAMENTE ESTA PRIVADA Y LO AGARRA 
        return self._nombre
    
    def get_nombre(self, new_nombre): #  
        self._nombre = new_nombre
    
ulises = Persona("Ulises", 17)

nombre = ulises.get_nombre()
print(nombre)

ulises.set_nombre("Benja")

nombre = ulises.get_nombre
print(nombre)