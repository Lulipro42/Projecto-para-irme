# LA CLASE ES LA FORMA DE PODER CREAR UN OBJETO COMO QUIERAS 
# Lo que creo aca son objetos que son instancias de la clase osea resumidamente cree un objeto
# El SELF representa la instancia actual de una clase. Permite que los métodos y atributos accedan a los datos específicos de ese objeto. 
#Y los INIT son es un metodo instancial 
# Para resumir los metodos es una FUNCION
class  Celular():
    def __init__(self, marca, camara, modelo):
        self.marca = marca
        self.camara = camara
        self.modelo = modelo

    def Llamar(self):
        print(f"Estas haciendo un llamado desde tu :{self.modelo}")

    def Cortar(self):
        print(f"cortaste el llamado desde tu: {self.modelo}")

celular1 = Celular("Xiaomi", "60MP", "Redmi note 14")
celular2 = Celular("Apple", "70MP", "Iphone 17 pro max")


print(celular2.modelo)
celular1.Cortar()



class Auto():
    def __init__(self, marca, modelo, color):
        self.marca1 = marca
        self.modelo1 = modelo
        self.color = color

    def Camino(self):
        print(f"Llegaste a la quiaca con tu: {self.modelo1}")

    def Perdido(self):
        print(f"Antes de llegar se te pincho la rueda en tu modelo: {self.modelo1}")

auto1 = Auto("Renault", "clio", "azul")
print(auto1.modelo1)
auto1.Perdido()


class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

nombre = input("Digame su nombre")
edad = input("Digame su edad")
grado = input("Digame su grado")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower == "estudiar"):
        estudiante.estudiar(self)
    else:
        print("Su estidante no se puede cursar")