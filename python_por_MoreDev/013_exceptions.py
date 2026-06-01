### EXCEPTION HANDLIG ###

number0ne = 5
numberTwo = 1
numberTwo = "1"

#if type(numberTwo) == int: # esto sigfica que aunque haya un error se cumpla igual la condicon osea q   ue se ejecutara igual
#    print(number0ne + numberTwo) # esto significa 
#else: # y el else lo que hace es que le da igual 

#    print("No se cumple")

try:
    print(numberTwo + number0ne)
    print("no se ha producio un error") # Esta linea al dar un eror salta lo que hay en el, except osea saltaria ("Se ha producido un error")
except:
    print("Se ha producido un error")

# Try except y else
try:
    print(number0ne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # EL ELSE sirve cuando la condición establecida en un if no se cumple (es falsa).
    # Se ejecuta si no se produce una EXCEPCION
    print("La ejecucion continua correctamente")

# try except, else y finally
try:
    print(number0ne + numberTwo)
    print("No se ha producido un error")
except: # solo que si saco el EXCEPT va a fallar, todo debido a que el try funciona con el EXCEPT
    print("Se ha producido un error")
else: # Puedo sacar el else si quiero total va a funcionar 
    # Se ejecuta si no se produce una EXCEPCION
    print("La ejecucion continua correctamente")
finally: # El finally se ejecuta siempre, haya o no una excepcion
    print("La ejecucion continua")


# Exception por tipo

try:
    print(numberTwo + number0ne)
    print("no se ha producio un error") # Esta linea al dar un eror salta lo que hay en el, except osea saltaria ("Se ha producido un error")
except TypeError: #Esto lo que hace que controla el error osea el TypeError,  y el except se produce solo si anda el TypeError
    print("Se ha producido un TypeError")
except ValueError: # al ser un ValueError no pasa nada esto, lo que tengo que hacer es que cuando en la terminal me salga ValueError poner ese codigo, para que el codigo fuente siga lo mas normal
    print("Se ha producido el ValueError")

# Captura de la informacion de la excepcion

try:
    print(numberTwo + number0ne)
    print("no se ha producio un error") # Esta linea al dar un eror salta lo que hay en el, except osea saltaria ("Se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error: # es una forma de controlar el error, sea lo que sea 
    print(error) 