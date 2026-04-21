### DICCIONARIOS ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"nombre": "ulises", "Apellido":"solis", "edad":17,1:"python"}

my_dict = {
    "Nombre":"Ulises", 
    "Apellido":"Solis",
    "Edad":"17",
    "Lenguaje":{"Python","Swift", "KOtlin"},
    1:1.77
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"])

print(my_dict[1])

# Esto es para cambiar cosas
my_dict["Calle"] = "Calle ulisesDev"
print(my_dict)

# para eliminar un solo elemento seria esto
del my_dict["Calle"]
print(my_dict)

print("Ulises"in my_dict)
print("apellido" in my_dict)

# con items tenemos un listado de cada uno de los ites
print(my_dict.items())
# las keys solo nos retorna las keys
print(my_dict.keys())
# values nos da los valores como mi estatura edad nombre etc
print(my_dict.values())

my_list = ["Nombre", "1", "piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, my_dict)
print(my_new_dict)

