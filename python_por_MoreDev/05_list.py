### listas ###


mi_lista = list()
# esto [] tambie cuenta como otra lista
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [17, 24, 62, 52, 49, 14, 23]

print(mi_lista)
# el len es para calcular el tamoaño o caracteres me parece 
print(len(mi_lista))

mi_otra_lista = ["35", "1.77", "Ulises", "Solis"]

print(type(mi_lista))
print(type(mi_otra_lista))

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-2])
print(mi_otra_lista.count)
# Al pasarse de los caracteres tira un error y es llamado pete(algo asi)
# esto es un error 
# print(mi_otra_lista[4])
# Como tambien icluye en el [-5] osea asi
# print(mi_otra_lista[-5])

print(mi_lista + mi_otra_lista)
#print(mi_lista - mi_otra_lista) no funciona tira error

# inserta otra cosa pero me parece que al final lo pone
mi_otra_lista.append("UlisesDev")
print(mi_otra_lista)

# inserta lo que quieras en el casillero que quieras
mi_otra_lista.insert(1, "Celeste")
print(mi_otra_lista)

# como dice su nombre saca las cosas que quieras como en este caso es "UlisesDev"
mi_otra_lista.remove("UlisesDev")
print(mi_otra_lista)



# En Python, pop() es un método para eliminar y devolver un elemento de una colección 
print(mi_lista.pop())
print(mi_lista)

del mi_lista[2]
print(mi_lista)

mi_pop_elemeto = mi_lista.pop(2)
print(mi_lista)
print(mi_pop_elemeto)


mi_nueva_lista = mi_lista.copy()

mi_nueva_lista.reverse()
print(mi_nueva_lista)