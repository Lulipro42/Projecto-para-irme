# EL POLIMORFISMO es mandar un mensaje entre comillas, que de ese mensaje puedo recibiri varias respuestas por ej: a un perro le digo que camine pero uno camina y los otros no etc, pero es basado en objetos al ser de ddiferentes tipos o otra cosa pero en que contesten esta bien


class Gato():
    def sonido(self):
        return "Miua"
    
class Perro():
    def sonido(self):
        return "Guaa"


def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(gato)

print(perro.sonido())

# EJERCICIO 2 
num1 = 3.
num2 = 4.7

resultado = num1 + num2

print(resultado)
print(type(resultado))


def recorrer(elemento):
    for item in elemento:
        print(f"El elemento acutual es: {item}")
        
lista = [1, 2, 3, 4]
lista2 = ["maquina", "como", "andas"]
# EN ESTE CASO EL POLIMORFISMO FUNCIONA YA QUE RECORRE IGUAL LAS OCSAS SIN NECESIDAD DE SER FLOAT O ENTERO PUEDE SER CUALQUIERA COSAS 
recorrer(lista2)

# TENGO QUE ESTUIDAR DUCK STYLING O ALGO ASI 
# ESTUDIAR ENLACES DINAMICOS Y ESTATICOS
# Y LO QUE ES EL TIPO REAL Y EL TIPO DECLARADO RESUMEN: EL TIPO REAL ES EL ORIGEN DE TODO Y EL TIPO DECLARADO ES EL ORIGEN DE TODO