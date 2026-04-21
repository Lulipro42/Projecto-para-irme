###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


# solucion 
mi_nombre = "Ulises"
mi_ciudad = "Buenos aires, La Plata"


### Completa aquí



print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

# solucion 
a = "a"
b = "3.14159"
c = "Hola mundo"
d = True
e = None

print("Tipo de",type(a))
print("tipo de",type(b))
print("tipo de",type(c))
print("tipó de",type(d))
print("tipo de",type(e))

### Completa aquí

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

# solucion 

### Completa aquí

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"
# solucion 
mi_nombre = "Ulises"
edad = 17
altura = 1.77

print(f"Hola me llamo: {mi_nombre}, tengo {edad} y mido actualmente {altura}")
# ¡Ojo! Los decimales en Python se escriben con punto (.), no con coma (,).
# altura = 1,77 crea una tupla (1, 77), no el número que esperas.


# Ejemplo sin la 'f': Imprime el texto literal.

# Ejemplo con la 'f' (f-string): Reemplaza las variables por sus valores.

### Completa aquí

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

# Solucion 
# Redondeamos directamente el valor de pi sin almacenarlo en una variable
resultado = int(round(3.1416) / 2)
print("valor de PI (aproximado):", 3.1416)
print("PI redondeado", round(3.1416))
print("Division entera de PI redeondado seria 2", resultado)


### EJERCICIOS QUE ME DIO CHATGPT
mi_nombre = "ulises"
mi_edad = 17

print(mi_nombre, mi_edad)

# operacion 2
numero = 20

doble = numero * 2

triple = numero * 3

print("numero", numero)
print("El numero pero doble", doble)
print("El numero pero triple", triple)

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")


# ejercicio 3

numero = 2
if numero <=10:
    print("el numero es chico")
elif numero <=50:
    print("medio")
else:
    print("grande")