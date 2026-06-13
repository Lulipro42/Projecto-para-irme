# El PASS sirve como un marcador de posición (placeholder) nulo. Permite definir clases, métodos o funciones vacías sin generar errores de sintaxis, ideal para prototipar o dejar código pendiente de implementación futura. 
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def Hablar(self):
        print("Hola estoy hablando y soy super pro porque cobro eso anualmente y eso va a cobrar ulises en el futuro mas")
        
        
class Empleado(Persona): # (Persona) es una clase de Empleado
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


# El SUPPER me sirve para poder hacer que las nuevas cosas que ponga lo puedan heredar de el padre osea el (Persona)
class Estudiante(Persona): # Estuiante es una super clase de Empleado(Persona)
    def __init__(self,nombre,edad,nacionalidad,notas,examenes):
        super().__init__(nombre,edad,nacionalidad) # 
        self.notas = notas
        self.examenes = examenes


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidades(self):
        print(f"Mi habilidad es: {self.habilidad}")


class EmpleadoArtista(Persona,Artista): # Esto es herencia Supper
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f'Hola soy: {self.nombre}, soy {self.nacionalidad}, tengo esta habilidad {self.habilidad} y por ahora no trabajo en {self.empresa}, como no trabajo mi salario actual es: {self.salario}')


benja = Estudiante("benja", 21, "uruguayo", "10/10", "por ahora nada")

roberto = Empleado("Roberto", 45, "peruano", "Programador", "100.000 anuales")

roberto.Hablar()

ramon = EmpleadoArtista("ramon", 24, "Argentino", "arquitectura", "por ahora no", "niguna empresa")
ramon.presentarse()

herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(benja, Estudiante)
print(herencia)
print(instancia)