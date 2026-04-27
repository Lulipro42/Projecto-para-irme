class TarjetaSube:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial # Encapsulamiento pro

    def cargar_saldo(self):
        while True:
            try:
                monto = input("Ingrese el monto a cargar: ")
                monto = float(monto) # Aquí es donde puede ocurrir el error
                
                if monto <= 0:
                    print("Error: El monto debe ser mayor a cero.")
                    continue # Vuelve a empezar el bucle
                
                self.__saldo += monto
                print(f"Carga exitosa. Nuevo saldo: ${self.__saldo}")
                break # Sale del bucle porque todo salió bien
                
            except ValueError:
                # Este bloque se ejecuta SI Y SOLO SI el usuario pone letras
                print("Dato inválido: Por favor, ingrese solo números.")

# --- Prueba del sistema ---
mi_tarjeta = TarjetaSube(1000)
mi_tarjeta.cargar_saldo()


"""
EJERCICIO 2 
"""
class Componente:
    def __init__(self, marca, modelo, precio): # CON ESTO LO QUE HAGO ES QUE CREO UNA CLASSE
        self.marca = marca # ESTAS TRES COSAS SON LOS ATRIBUTOS DE LA CLASS 
        self.modelo = modelo
        self.precio = precio
        
    
class Procesador(Componente): # OTRA CLASE SOLO QUE CON ESTA TOMA HERENCIA DE LA PRIMERA QUE ES COMPONENTE
    def __init__(self, marca, modelo, precio, nucleos):
        super().__init__(marca, modelo, precio)
        self.nucleos = nucleos
        
        
class Disco(Componente):
    def __init__(self, marca, modelo, precio, capacidad):
        super().__init__(marca, modelo, precio)
        self.capacidad = capacidad # LO MISMO PASA CON ESTA QUE TOMA HERENCIA DE LA PRIMERA Y EL SUPPER SIRVE PARA TRAER LOS ATRIBUTOS DE LA PRIMERA CLASE A LA QUE YO QUIERA
        
    
class Carrito:
    def __init__(self) -> None:
        self.productos = [] # CON LOS CORCHETES ESOS ABRO UNA LISTA PAR YA HACER LAS COSAS MAS PROS
        
    def agregar(self, producto):
        try: # CON EL TRY HACE QUE SI NO ANDA NINGUNA DE LAS SOLICITUDES QUE LE MANDO TIENE DOS POSIBILIDADES 
            if producto is None: # ACA DICE QUE SI EL PRODUCTO ES NONE OSEA INVALIDO PONE LO DEL PRINT
                raise ValueError("No se puede agregar un producto")
            
            self.productos.append(producto)
            print(f"Agregado exitosamente: {producto.marca} {producto.modelo}")
            
        except AttributeError:# Un AttributeError en Python es una excepción (error) que se produce cuando intentas acceder o asignar un atributo (método, propiedad o variable) a un objeto que no lo tiene
            print("Error del sistema: El objeto que intetas agregar no existe")
        except Exception as e: #except Exception as e: es una estructura en Python para el manejo de excepciones (errores) que captura cualquier error genérico ocurrido en un bloque try y lo asigna a la variable e. Imprimir {e} permite mostrar el mensaje descriptivo del error específico sin detener la ejecución del programa. 


            print(f"Error inesperado al agregar: {e}")
        
    def ver_total(self):
        try:
            total = sum(p.precio for p in self.productos)
            print(f"Total del carrito ${total}")
        except TypeError:
            print("Error critico: Unod de los productos en el carrito no existe")
    
    
    def mostrar_detalle(self):
        print("\n ----- DETALLE DEL CARRITO -----")
        for p in self.productos: # ACA LO QUE HACE QUE SE METE DETNRO DE EL SELF.PRODUCTO
            detalle = f"item {p.marca} {p.modelo}  | Precio ${p.precio}"
            
            if isinstance(p, Procesador):
                detalle += f" | Nucleos: {p.nucleos}"
            else:
                detalle += f" | Capacidad: {p.capacidad}"
            
            print(detalle)
        
cpu = Procesador("amd", "ryzen 5 5600 gt", 15000, 6)
ssd = Disco("Kinsgton", "490gb", 5000, "A500")


mi_compra = Carrito()
mi_compra.agregar(cpu) # ACA LO QUE HACE ES QUE LLAMA A LOS ATRIBUTOS QUE PUSE 


mi_compra.mostrar_detalle()
mi_compra.ver_total()

"""
EJERCICO 2 DE ENTORNOS VIRTUALES ESTA VEZ CLASES
"""
class Estudiante: # CREO UNA CLASE QUE SE LLAME ESTUDIANTE
    def __init__(self, nombre, edad, promedio, asistencias):
        self.nombre = nombre
        self.edad = edad
        self.promedio = float(promedio.replace(',', '.')) if isinstance(promedio, str) else promedio # ACA LO PRIMERO QUE HACE EL FLOAT ALMACENA NUEMEROS REALES QUE INCLUYAN DEDCIMALES. DESPUES REPLACE LO QUE HACE ES QUE REMPLAZA LAS COMAS POR LOS PUNTOS 
        self.asistencias = int(asistencias) # ACA LO QUE HACE QUE INT SOLO PERMITE NUMEROS ENTEROS
        
        
    def evaluar_beca(self):
        if self.edad >= 18:
            print(f"No puede cursar mas debido a que supera la edad regular {self.edad}")
        else:
            print("Puede seguir cursando")    
        
        if self.promedio > 8 and self.asistencias > 85: # ACA LO QUE HACE ES QUE PROMEDIO TIENE QUE SER MAYOR A 8 Y QUE LAS ASISTENCIAS TIENEN QUE SER MAYOR A 85
            print(f"!Felicidades! {self.nombre}! Tienes la beca") # BUENO ACA IMPRIME ESE PRINT CON EL NOMBRE
        else:
            print(f"Lamentablemente {self.nombre}, no cumples los requisitos principales para poder obtener la beca") # LO MISMO QUE EL ANTERIOR IMPRIME LE PRINT
        if self.asistencias < 0 and self.promedio > 10:
            print("Error: el promedio debe estar entre 0 o 10") # ACA DICE QUE SI LAS ASISTENCIAS SON MENORES A 0 Y QUE EL PROMEDIO ES MAYOR A 10 TIENE QUE HABER UN 50/50
            return        
    
    def __str__(self):
        return f"Estudiante: {self.nombre} | Promedio: {self.promedio} | Edad:{self.edad}"
    
alumno1 = Estudiante("Ulises", 16, "9", "90") # ACA CREO DOS VARIANTES DE ALUMNOS QUE UNO ES EXCELEMTE Y OTRO NO ENTONCES VEO LOS RESULTADOS QUE ME ARROJA LA MAQUINA
alumno2 = Estudiante("Benja", 21, "5", "67")
alumno1.evaluar_beca()
print(alumno1)
    
"""
TAREA: SISTEMA DE CONTROL DE ACCESO (LOGIN PRO)

1. Crea una clase 'Usuario' que reciba 'nombre' y 'password'.
2. Define atributos internos: 
   - 'self.intentos_fallidos' (debe empezar en 0).
   - 'self.bloqueado' (debe empezar en False).
3. Implementa el método 'intentar_login(password_ingresada)':
   - PRIMERO: Si 'self.bloqueado' es True, imprimir "Cuenta bloqueada" y salir del método.
   - SEGUNDO: Si 'password_ingresada' es igual a 'self.password':
     * Imprimir "¡Acceso concedido!".
     * Resetear 'self.intentos_fallidos' a 0.
   - TERCERO (Si falla): 
     * Sumar 1 a 'self.intentos_fallidos'.
     * Imprimir cuántos intentos lleva.
     * SI 'self.intentos_fallidos' llega a 3, cambiar 'self.bloqueado' a True.
"""
class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.intentos_fallidos = 0
        self.bloqueado = False
        
    def intentar_login(self):
        if self.bloqueado == True:
            print(f"Error la cuenta de {self.nombre} ha sido bloqueda")
            return
        
        password_ingresada = input(f"Hola {self.nombre}, ingrese su contraseña: ")

        if password_ingresada == self.password:
            print("!Acceso concedido! Bienvenido")
            self.intentos_fallidos = 0
            
        else:
            self.intentos_fallidos += 1
            print(f"Contraseña incorrecta. Llevas {self.intentos_fallidos}")
            
            if self.intentos_fallidos >= 3:
                self.bloqueado = True
                print("Demasiados INTENTOS: porfavor espera a que se reinicie le contador")

user1 = Usuario("Dafne", "river2026")
user1.intentar_login()

"""
TAREA: SISTEMA DE RESERVA DE TURNOS

1. Crea una clase 'Entrenamiento' que reciba 'deporte' y 'cupo_maximo'.
2. Define atributos internos:
   - 'self.inscriptos' (debe ser una lista vacía para guardar los nombres).
3. Implementa el método 'inscribir_persona(nombre_persona)':
   - PRIMERO: Si el largo de la lista 'self.inscriptos' es igual o mayor al 'self.cupo_maximo',
     imprimir: "Cupo lleno para {self.deporte}. {nombre_persona} queda en espera."
   - SEGUNDO: Si hay lugar, agregar el nombre a la lista y decir: "{nombre_persona} inscripto con éxito".
4. Implementa el método 'mostrar_lista()':
   - Debe imprimir todos los nombres que están anotados hasta el momento.
5. EXTRA: Agregá un método 'cancelar_reserva(nombre_persona)' que busque el nombre en la lista y lo saque.
"""
"""
TAREA: SISTEMA DE RESERVA DE TURNOS (REVISADO)

1. Crea una clase 'Entrenamiento' que reciba 'deporte' y 'cupo_maximo'.
2. Define atributos internos:
   - 'self.inscriptos' (lista vacía).
3. Implementa el método 'inscribir_persona(nombre_persona)':
   - Usa len() para comparar la cantidad de gente con el cupo.
   - Si hay lugar, usa .append() para sumarlo a la lista.
4. Implementa el método 'mostrar_lista()':
   - Recorre la lista con un bucle for e imprime cada nombre.
"""

"""
TAREA: SISTEMA DE LOGÍSTICA Y TRANSPORTE (FLOTA) 🚛

1. Crea una clase 'Paquete' que reciba 'descripcion', 'peso_kg' y 'destino'.
2. Crea una clase 'Camion' que tenga 'patente' y 'capacidad_maxima_kg'.
3. Define un atributo interno en Camion: 'self.carga' (lista vacía).
4. Implementa el método 'cargar_paquete(paquete)':
   - Usa un bloque try/except para validar que el 'peso_kg' sea un número.
   - Calcula si el peso del nuevo paquete + el peso total ya cargado supera la 'capacidad_maxima_kg'.
   - Si supera la capacidad, lanza un error: raise ValueError("Sobrecarga: El camión no soporta tanto peso").
   - Si hay lugar, agregalo a 'self.carga'.
5. Implementa el método 'estado_del_envio()':
   - Debe mostrar la patente del camión, cuántos paquetes lleva y el peso total actual.
6. EXTRA: Crea un método 'descargar_por_destino(ciudad)' que elimine de la lista 
   todos los paquetes que tengan ese destino.
"""

class Paquete:
    def __init__(self, descripcion, peso_kg, destino):
        self.descripcion = descripcion
        self.peso_kg = peso_kg
        self.destino = destino
        
class Camion:
    def __init__(self, patente, capacidad_maxima_kg):
        self.patente = patente
        self.capacidad_maxima_kg = capacidad_maxima_kg
        self.carga = []
    
    """
Pista para el método cargar_paquete:
1. Usá una variable para sumar el peso de lo que ya está en self.carga.
2. Usá un try/except para convertir el peso del paquete a número si es necesario.
3. Usá un IF para comparar con la capacidad_maxima_kg.
"""

# Así debería verse tu lógica adentro de la clase Camion:

    def cargar_paquete(self, paquete):
        try:
            # 1. Calculamos el peso actual del camión
            peso_actual = 0
            for p in self.carga:
                peso_actual += p.peso_kg
            
            # 2. Vemos cuánto pesaría si sumamos el nuevo
            peso_final = peso_actual + paquete.peso_kg
            
            # 3. Comparamos con el límite
            if peso_final > self.capacidad_maxima_kg:
                # Si se pasa, lanzamos el error
                raise ValueError(f"Sobrecarga: El camión llegaría a {peso_final}kg y el máximo es {self.capacidad_maxima_kg}kg")
            else:
                # Si hay lugar, lo guardamos
                self.carga.append(paquete)
                print(f"Paquete '{paquete.descripcion}' cargado con éxito.")
                
        except TypeError:
            print("Error: El peso del paquete no es un número válido.")
        except ValueError as e:
            # Acá atrapamos el error de sobrecarga que lanzamos arriba
            print(f"ALERTA: {e}")
        
    def estado_del_envio(self):
        peso_total = sum(p.peso_kg for p in self.carga)
        print(f"\n ------ ESTADO DEL CAMION [{self.patente}] ------")
        print(f"Paquete a bordo: {len(self.carga)}")
        print(f"Peso actual: {peso_total}kg / {self.capacidad_maxima_kg}")
        
mi_camion = Camion("ford pro mas", 2100)

p1 = Paquete("Procesador Ryzen", 4300, "Mendoza")
p2 = Paquete("Monitores led", 200, "Jujuy")
p3 = Paquete("Gabinete gamer", 600, "San luis")

mi_camion.cargar_paquete(p1)
mi_camion.cargar_paquete(p2)
mi_camion.cargar_paquete(p3)

mi_camion.estado_del_envio()



"""
TAREA: SIMULADOR DE WEB SCRAPER 🕷️

1. Crea una clase 'Producto' que reciba 'nombre', 'url' y 'precio_objetivo'.
2. Crea una clase 'Scraper' que tenga un método 'obtener_precio(url)':
   - Debe usar un bloque try/except.
   - Dentro del try, debe "simular" que se conecta (imprimí: "Conectando a [url]...").
   - Si la URL no empieza con "https", lanza un ValueError("URL no segura").
3. Implementa el método 'chequear_oferta(producto, precio_actual)':
   - Si el 'precio_actual' es menor o igual al 'precio_objetivo', imprime: "¡OFERTA! Comprar [nombre]".
   - Si no, imprime: "Sigue caro, toca esperar".
"""
import requests

class Litkila:
    def __init__(self, nombre, url, precio_objetivo):
        self.nombre = nombre
        self.url = url
        self.precio_objetivo = precio_objetivo
        
class Scraper:
    def obtener_precio(self, url):
        try:
            print(f"Conectando a la {url}...")
            
            if not url.startswith("https"):
                raise ValueError("URL no segura")
            
            return 145000
        
        except ValueError as e:
            print(f"Error de validacion: {e}")
            return None
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            return None

    def chequear_oferta(self, producto, precio_actual):
        if precio_actual is None:
            print("No se puede chequear la oferta ya que hubo un error")
            return
        
        if precio_actual <= producto.precio_objetivo:
            print(f"!OFERTA! Comprar {producto.nombre}")
        else:
            print(f"Sigue caro el {producto.nombre}, toca esperar")
            
procesador2 = Litkila("Ryzen 5 5600GT","https://tienda.com/cpu", 15000 )

mi_scraper = Scraper()

precio_detectado = mi_scraper.obtener_precio(procesador2.url)
mi_scraper.chequear_oferta(procesador2, precio_detectado)



"""
EJERCICIO: SISTEMA RESTAURANTE AUTOMÁTICO 🤖
------------------------------------------
1. Clase 'Pedido': Debe recibir 'plato', 'mesa' y 'temperatura_coccion'.
2. Clase 'ChefRobot':
   - Método 'preparar(pedido)':
     - Usa un bloque try/except.
     - Si la 'temperatura_coccion' < 60, lanza ValueError("Riesgo sanitario: temperatura baja").
     - Si la 'mesa' == 0, lanza Exception("Error de sala: Mesa no asignada").
     - Si todo está ok, imprime: "Cocinando [plato]...".
3. Clase 'Cajero':
   - Método 'generar_ticket(pedido, precio)':
     - Calcula el precio final sumando un 10% de servicio.
     - Imprime el plato y el total a pagar.
"""

class Pedido:
    def __init__(self, plato, mesa, temperatura_coccion):
        self.plato = plato
        self.mesa = mesa
        self.temperatura_coccion = temperatura_coccion
        
class ChefRobot:
    def preparar(self, pedido):
        try:
            print(f"\n--- Recibiendo orden: {pedido.plato} ---")
            if pedido.temperatura_coccion < 60:
                raise ValueError("Riesgo sanitario: temperatura baja")
            
            if pedido.mesa == 0:
                raise Exception("Error de la sala: Mesa no asignada")
            print(f"👨‍🍳 Robot: {pedido.plato} en proceso de cocción.")
            return True
        except ValueError as e:
            print(f"Hubo un error: {e}")
            return False
        except Exception as ve:
            print(f"Hubo un erro inesperado: {ve}")
            return False


class Cajero:
    def generar_ticket(self, pedido, precio):
        
        total = precio * 1.10
        print(f"---- TICKETC MESA {pedido.mesa}")
        print(f"Producto: {pedido.plato}")
        print(f"Total con servicio (10%): ${total}")
        print("----------------------------")
        
pizza = Pedido("Pizza especial", 5, 200)
robot = ChefRobot()
caja = Cajero()

if robot.preparar(pizza):
    caja.generar_ticket(pizza, 10000)