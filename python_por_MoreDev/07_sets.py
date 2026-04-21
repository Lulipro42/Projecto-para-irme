### SETS ###

my_set = set("")
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # esto es un diccionario

my_other_set = ["Ulises", "Solis", 17]
print(type(my_other_set)) 

# (Len) Para obtener la longitud de un objeto
print(len(my_other_set))

print("Ulises" in my_other_set)
print("Ulisis" in my_other_set)

my_other_set.remove("Ulises")
print(my_other_set)

# (clear) borra todo lo de la variable
my_other_set.clear()
print(my_other_set)

# el del elimina todo en cambio el clear solo elimina lo de adentro RECORDAR
del my_other_set

my_set = {"Ulises", "solis", "17", "1.77"}
my_list = list(my_set)
print(my_list)
print(my_list[-1])

my_other_set = {"Sigma","pro", "python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"}))