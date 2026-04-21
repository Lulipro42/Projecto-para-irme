class Lista:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    
    # El método __str__ sirve para definir una representación del objeto en cadena de texto (string)
    # que sea legible para el usuario final. Se activa cuando usas print() o str().
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    # El método __repr__ es similar, pero busca ser una representación técnica para desarrolladores
    # (útil para debugging). Si __str__ no está definido, print() usará __repr__.
    def __repr__(self):
        return f'Lista("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Lista(nombre+otro.nombre,nuevo_valor)
    
    
    
ulises = Lista("Ulises", 17)
dalto = Lista("Dalto", 25)

# Al hacer print, Python busca el método __str__ automáticamente.
# Si no existiera __str__, verías algo feo como: <__main__.Lista object at 0x...>
print(ulises) 

# Ejemplo con una lista real:
otra_lista = [1, 2, 3]
print(otra_lista) # Las clases integradas de Python ya tienen su propio __str__ definido.

resultado = ulises + dalto
print(nueva_persona.edad)