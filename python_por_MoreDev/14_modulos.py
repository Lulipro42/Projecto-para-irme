### MODULOS ###
# Los modulos en Python son archivos que contienen codigo Python osea puedo agarrar cualquier codigo de cualquier fichero y utilizarlo a mi favor en otro fichero.
# Estos archivos pueden definir funciones, clases y variables.
# Los modulos permiten organizar el codigo en partes reutilizables y mantenibles.
# Para usar un modulo en otro archivo Python, se utiliza la palabra clave 'import'.
# Ejemplo de como importar un modulo:
from my_module import sum, printValue, sigmaValue
# my_module.sum(5, 10, 15)
# En este ejemplo, estamos importando un modulo llamado 'module' y utilizando una funcion llamada 'sum' definida en ese modulo. 
# my_module.printValue("Hola Morronga")
# Esto permite reutilizar la funcion 'printValue' en diferentes archivos sin tener que reescribir el codigo.
sum(5, 10, 15) # Esto llamara a la funcion sum del modulo my_module y pasara los argumentos 5, 10 y 15 osea hago una operacion en concreta.
printValue("Hola Morronga") # Esto llamara a la funcion printValue del modulo my_module y pasara el argumento "Hola Morronga" ya que en el import esta definido.
sigmaValue("Hola Sigma") # Esto llamara a la funcion sigmaValue del modulo my_module y pasara el argumento "Hola Sigma" ya que en el import esta definido.

import 