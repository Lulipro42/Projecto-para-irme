### CONCDICIONALES ###

# un condicional usando la palabra if

my_condicionals = False

# no se imprime el if debido a que my_condicionals puse que es falsa y el if es SI
if my_condicionals:
    print("Se ejecuta la condicion del if")

my_condicionals = 5 * 5 

# Al ponerle un 10 si se ejecuta debido a que 5 * 2 es 10 que es True encambio si pongo 11 es False y no se ejecutara
if my_condicionals == 10:
    print("se ejecuta la condicion del if")

# pasa algo raro debido a que no se ejecuta con un 10 o 11 pero si con un 5
if my_condicionals > 10 and my_condicionals < 20:
    print("es mayor que 10 y menor que 20")
# elif es para evaluar múltiples condiciones de forma secuencial dentro de una misma estructura condicional
if my_condicionals > 10 and my_condicionals < 20:
    print("es mayor o igual a 10 y menor que 20")
elif my_condicionals == 25:
    print("es igual a 25")
# el ELSE es que si no se cumple lo que dice el if,  SE TIENE QUE CUMPLIR LO QUE DICE EL else
else:    
    print("es menor o igual que 10 o mayor o igual que 20 o distino de 25")
    
    
print("la ejecucion continua")

# if elif y else SON todos los condicionales que tenemos que saber 

my_string = ""

if not my_string:
    print("mi cadena de texto es vacia")

if my_string == "mi cadena de textooooooo":
    print("Estas cadenas de texto coinciden")