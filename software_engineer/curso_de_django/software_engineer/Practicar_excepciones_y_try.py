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
    
    

# Definimos la estructura de un gasto individual
class Gasto:
    def __init__(self, concepto, monto, categoria):
        # Guardamos los datos que nos pasan en 'atributos' del objeto
        self.concepto = concepto
        self.monto = monto
        self.categoria = categoria

# Definimos quién va a guardar y procesar esos gastos
class Billetera:
    def __init__(self):
        # Creamos una lista vacía que será nuestra 'base de datos' temporal
        self.historial = []
        
    def registrar_gasto(self, gasto):
        """Recibe un objeto de tipo Gasto y lo guarda si es válido."""
        try:
            # Validamos que el dinero sea un número positivo
            if gasto.monto <= 0:
                # Si es 0 o menos, lanzamos el error manualmente
                raise ValueError("Monto inválido: debe ser mayor a 0")
            
            # .append es el comando para 'meter' el objeto adentro de la lista
            self.historial.append(gasto)
            print(f"✅ Registrado con éxito: {gasto.concepto}")
            
        except ValueError as e:
            # Si saltó el raise de arriba, se ejecuta este bloque
            print(f"❌ Error al registrar: {e}")

    def total_por_categoria(self, categoria_buscada):
        """Suma todos los montos de una categoría específica."""
        total = 0  # El acumulador empieza en 0
        
        print(f"\n--- Analizando categoría: {categoria_buscada} ---")
        
        # Recorremos la lista de objetos uno por uno
        for g in self.historial:
            # 'g' es el objeto Gasto actual en la vuelta del bucle
            if g.categoria == categoria_buscada:
                # Si la categoría coincide, sumamos su monto al total
                total += g.monto 
                print(f"Item: {g.concepto} | Valor: ${g.monto}")
        
        # Devolvemos el resultado final para que otra clase lo use
        return total

# Definimos quién analiza si estamos gastando de más
class Analizador:
    def comprobar_salud(self, total, limite):
        """Compara el total gastado contra un límite presupuesto."""
        if total > limite:
            # Calculamos la diferencia para dar una mejor respuesta
            sobrante = total - limite
            print(f"⚠️ ALERTA: Gastaste ${total}. Te pasaste por ${sobrante} del límite.")
        else:
            print(f"✅ Todo bajo control. Te quedan ${limite - total} de presupuesto.")

# --- ZONA DE PRUEBAS (Donde el código cobra vida) ---

# 1. Instanciamos las clases principales
mi_billetera = Billetera()
mi_analizador = Analizador()

# 2. Creamos los 'objetos' de datos
g1 = Gasto("Cena con amigos", 5000, "Comida")
g2 = Gasto("Entrada Cine", 3000, "Ocio")
g3 = Gasto("Compra Supermercado", 8000, "Comida")

# 3. Usamos la billetera para guardar esos objetos
mi_billetera.registrar_gasto(g1)
mi_billetera.registrar_gasto(g2)
mi_billetera.registrar_gasto(g3)

# 4. Procesamos los datos: Pedimos el total de 'Comida'
# Guardamos ese resultado (un número) en una variable
gasto_comida = mi_billetera.total_por_categoria("Comida")

# 5. Pasamos ese número al analizador para que tome una decisión
mi_analizador.comprobar_salud(gasto_comida, 10000)





"""
EJERCICIO: STREAMING APP 📺 (RUBRO ENTERTAINMENT)
------------------------------------------------
1. Clase 'Contenido': 
   - Debe recibir 'titulo', 'genero' (ej: "Acción") y 'puntuacion' (ej: 9).

2. Clase 'Plataforma':
   - Debe tener una lista llamada 'catalogo' vacía.
   - Método 'subir_contenido(contenido)':
     - Usa try/except.
     - Si la 'puntuacion' es menor a 1 o mayor a 10, lanza ValueError("Puntuación fuera de rango").
     - Si está ok, agrega el objeto 'contenido' a la lista 'catalogo' e imprime éxito.
   - Método 'recomendar_por_genero(genero_buscado)':
     - Debe recorrer la lista 'catalogo' con un bucle for.
     - Si el género del contenido coincide con el buscado, imprime el título.

3. Clase 'Critico':
   - Método 'evaluar_calidad(lista_contenidos)':
     - Debe recorrer la lista que recibe.
     - Si la puntuación es >= 8, imprime: "[titulo] es una Joya 💎".
     - Si no, imprime: "[titulo] es Regular 🍿".
"""

class Contenido:
    def __init__(self, titulo, genero, puntuacion):
        self.titulo = titulo
        self.genero = genero
        self.puntuacion = puntuacion

# 2. La Plataforma gestiona el catálogo (Nuestra "Base de Datos")
class Plataforma:
    def __init__(self):
        # La lista empieza vacía cada vez que creamos una plataforma nueva
        self.catalogo = []
        
    def subir_contenido(self, contenido):
        try:
            # Validamos el rango (usamos 'or' porque no puede ser las dos a la vez)
            if contenido.puntuacion < 1 or contenido.puntuacion > 10:
                raise ValueError(f"Puntuación {contenido.puntuacion} fuera de rango (1-10)")
            
            # Si pasó el IF, lo guardamos físicamente en la lista
            self.catalogo.append(contenido)
            print(f"✅ Subido: {contenido.titulo}")
            
        except ValueError as e:
            # Atrapamos el error para que el programa no se cierre
            print(f"❌ ERROR en {contenido.titulo}: {e}")

    def recomendar_por_genero(self, genero_buscado):
        print(f"\n--- 🎬 Recomendaciones de {genero_buscado} ---")
        encontrado = False
        # Recorremos objeto por objeto dentro de la lista
        for c in self.catalogo:
            if c.genero == genero_buscado:
                print(f"-> {c.titulo} (Puntaje: {c.puntuacion})")
                encontrado = True
        
        if not encontrado:
            print("No hay contenido disponible para este género.")

# 3. El Crítico analiza la calidad (Procesamiento de datos)
class Critico:
    def evaluar_calidad(self, lista_contenidos):
        """Recibe una lista de objetos y los clasifica."""
        print("\n--- 🕵️ INFORME DEL CRÍTICO ---")
        # 'peli' es el nombre temporal que le damos a cada objeto en el bucle
        for peli in lista_contenidos:
            if peli.puntuacion >= 8:
                print(f"💎 {peli.titulo}: Es una JOYA.")
            else:
                print(f"🍿 {peli.titulo}: Es REGULAR.")

netflix = Plataforma()
ulises_critico = Critico()

peli1 = Contenido("Batman", "Acción", 9)
peli2 = Contenido("Titanic", "Drama", 7)
peli3 = Contenido("Inception", "Acción", 10)
peli4 = Contenido("Peli Trucha", "Comedia", 15)

netflix.subir_contenido(peli1)
netflix.subir_contenido(peli2)
netflix.subir_contenido(peli3)
netflix.subir_contenido(peli4) 

netflix.recomendar_por_genero("Acción")

ulises_critico.evaluar_calidad(netflix.catalogo)