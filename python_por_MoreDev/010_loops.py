### LOOPS/BUCLE ###
# es un mecanismo que nos sirve apra iterar, osea repetir algo llamado bucle

# While Un bucle funciona ejecutando repetidamente un bloque de código mientras una condición específica se mantenga verdader
# Mientra el WHILE sea verdadero la accion seria que haga algo
my_condition = 0
# imprime en infinito el numero 0 o otra cosa, deja de imprimilo hasta que yo no le ponga un break(romper)
# while es una especie de if
# y solo nos acepta el else y el if 
while my_condition < 20:
    print(my_condition)
    my_condition += 4 # esto es igual que incrementarle al numero y esto lo que hace es detener el bucle
if my_condition == 10:
    print("mi condicion es igual a 10")
else: # esto sucede justo antes de llegar al 10 cumple lo dicho el codigo y hace lo que dice el print
    
    print("mi condicion es mayor o igual que 10")    

print("la ejecucion continua")


while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("mi condicion es 15")
        break
    print(my_condition)
print("la ejecucion continua")

# Bucle For
# Un bucle for nos sirve para iterar un listado de elementos

my_list = [35, 24, 62, 12, 52, 42,17]

for element in my_list:
    print(element)
    

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)
    

my_set = {"Ulises", "solis", "17"}
for element in my_set:
    print(element)
    
my_dict = {"Nombre":"Ulises", "Apellido":"Solis", "Edad":"17", "1":"papu"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("se ejecuta")
    #elif element == 1: EL ELIF no se puede utilizar con el FOR
    #print("element vale 1")
else:
    print("El bulce for para diccionario ha finalizado")
    


y_dict = {"Nombre":"Ulises", "Apellido":"Solis", "Edad":"17", "1":"papu"}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue # con este continue le podemos indicar que sea capaz de hacer algo que nosotros queramos como por ejemplo que ponga el 1 y lo que hace es que continua pero volviendo al for    
    print("se ejecuta")
else:
    print("El bulce for para diccionario ha finalizado")