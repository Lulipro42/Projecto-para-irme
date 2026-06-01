### Tuplas ###
# Una tupla es un conjunto de valores 

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (17, 1.77, "Ulises", "Ulises", "Morronga", "Morronga", "Solis")
my_other_tuple = (41, 13, 51, 24, 34)
print(my_tuple)

# el type es para que en la terminal muestre que clase es 
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[6]) Es un error  debido a que no hay tantos caracteres para que llegue a ese numero
#print(my_tuple[-5]) es un error debido a que no hay tantos caracteres para que llegue a ese numero

# count cuenta cuanta palabras hay con la palabra que escribiste tu 
print(my_tuple.count("Ulises"))
# index dice en que posicion del numero esta en este caso es 4
print(my_tuple.index("Solis"))
print(my_tuple.count("Morronga"))

# no me deja no se porque 
#my_tuple[1] = 1.87
# se suman al ponerle +
print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Ulises"
my_tuple.insert(1, "celeste")
my_tuple= tuple(my_tuple)
print(tuple(my_tuple))
print(my_tuple)

del my_tuple
# print(my_tuple) Es un error NO HAY QUE HACERLO 