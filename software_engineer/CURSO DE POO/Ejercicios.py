# EJERCIOS PARA PODER APRENDER
# EXPLICACIÓN DE LOS CONCEPTOS APLICADOS:

"""
TAREA:
1. Crea una clase 'Celular'.
2. El constructor debe recibir: marca, modelo y RAM.
3. Agregá un método 'describir' que imprima: "Soy un [marca] [modelo] con [RAM]GB".
4. Instanciá dos objetos (ej: un Samsung y un iPhone) y llamá al método.
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 1: CLASES Y OBJETOS ---
# Aquí definimos el "molde" (Clase) llamado Celular. 
# El método __init__ es el constructor: se ejecuta al crear el objeto para darle sus valores iniciales.
# 'self' es la forma en que el objeto se refiere a sí mismo para acceder a sus propiedades.

# Definimos la clase Celular
class Celular:
    def __init__(self, marca, modelo, Ram):
        self.marca = marca
        self.modelo = modelo
        self.Ram = Ram

    def describir(self):
        print(f"Soy {self.marca} mi modelo es {self.modelo} y tengo {self.Ram} de ram")
        
celular1 = Celular("Samsung", "S21", 8)
celular2 = Celular("Iphone", "17 Pro Max", 6)
print(celular1)
print(celular2)
celular2.describir()

### EJERCICIO 2 
"""
TAREA 2:
1. Crea una clase padre 'Personaje' con nombre y fuerza.
2. Crea una clase hija 'Guerrero' que herede de Personaje.
3. El Guerrero debe tener un atributo extra: 'arma'.
4. Sobrescribí el método 'atacar' para que diga: "[nombre] ataca con su [arma]".
"""

# --- EXPLICACIÓN NIVEL 2: HERENCIA ---
# La Herencia permite que una clase (Guerrero) tome atributos y métodos de otra (Personajes).
# Usamos 'super().__init__' para no repetir el código de asignación de nombre y fuerza que ya está en el padre.
# Sobrescribir (Override) es redefinir un método del padre para que haga algo específico en el hijo.

# Clase base para todos los personajes
class Personaje:
    def __init__(self, nombre, fuerza):
        self.nombre = nombre
        self.fuerza = 200
        
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, arma):
        super().__init__(nombre, fuerza)
        self.arma = arma
        
    def atacar(self):
        print(f"El Guerrero cuyo nombre es {self.nombre} ataca con su {self.arma}")

pj = Personaje("Benja", 200)
print(pj)
arma2 = Guerrero("Asta", 200, "espada")
print(arma2)

arma2.atacar()

""" 
TAREA 3 :
1. Crea una clase 'CuentaBancaria'.
2. El atributo 'saldo' debe ser privado (__saldo).
3. Crea un decorador @property para ver el saldo.
4. Crea un método 'depositar' que valide que el monto sea positivo antes de sumar.
5. Crea un método 'retirar' que valide que haya saldo suficiente.
"""

# --- EXPLICACIÓN NIVEL 3: ENCAPSULAMIENTO Y PROPIEDADES ---
# El uso de '__saldo' (doble guion bajo) hace que la variable sea privada, protegiéndola de cambios accidentales externos.
# @property actúa como un "Getter": permite leer el saldo como si fuera un atributo, pero sin poder modificarlo directamente.
# Los métodos depositar y retirar actúan como filtros de seguridad (validación de lógica de negocio).

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        # Atributo privado: nadie puede hacer 'cuenta.__saldo' desde afuera
        self.__saldo = saldo_inicial # Encapsulamiento fuerte
        
    @property # Convierte el método en un atributo de lectura
    def saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        # Lógica de negocio: validación de datos
        # Validación de Ingeniero: no podés depositar plata negativa
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Error: El monto a depositar debe ser positivo.")
            
    def retirar(self, monto):
        # Validación: ¿tiene plata suficiente?
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.__saldo}")
        elif monto > self.__saldo:
            print("Error: Fondos insuficientes.")
        else:
            print("Error: Monto de retiro no válido.")

# --- PRUEBA DEL NIVEL 3 ---
mi_cuenta = CuentaBancaria(5000)

# Usamos la @property para ver el saldo (sin paréntesis)
print(f"Saldo inicial: ${mi_cuenta.saldo}")

# Intentamos depositar
mi_cuenta.depositar(2000)

# Intentamos retirar más de lo que hay
mi_cuenta.retirar(1231)


from abc import ABC, abstractmethod

"""
TAREA:
1. Crea una clase abstracta 'Notificador' con un método abstracto 'enviar(mensaje)'.
2. Crea una clase 'NotificadorEmail' que implemente 'enviar' (print "Enviando Email...").
3. Crea una clase 'NotificadorSMS' que implemente 'enviar' (print "Enviando SMS...").
4. Crea una clase 'Usuario' que reciba cualquier TIPO de notificador (esto es Polimorfismo).
5. El usuario debe tener un método 'alertar' que use el notificador que le pasaste.
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 4: ABSTRACCIÓN Y POLIMORFISMO ---
# Notificador(ABC) es una Clase Abstracta: es un contrato. No puedes crear un "Notificador" a secas, debes crear algo específico (Email o SMS).
# El @abstractmethod obliga a las clases hijas a tener el método 'enviar'.
# Polimorfismo: El método 'alertar' del Usuario no sabe si recibe un Email o un SMS, solo sabe que tiene un método '.enviar()'. 
# El objeto se comporta de forma distinta según su tipo real.
from abc import ABC, abstractmethod

# Clase abstracta: no se puede instanciar, sirve de molde
class Notificador(ABC):
    @abstractmethod # Obliga a las hijas a implementar este método
    def enviar(self, mensagge, destiny):
        pass
# Implementación específica para Email
class NotifierEmail(Notificador):
    def enviar(self, mensagge, destiny):
        print(f"Sending email: [{destiny}]: {mensagge}")
# Implementación específica para SMS        
class NotifierSMS(Notificador):
    def enviar(self, mensagge, destiny):
        print(f"Sending SMS : [{destiny}]: {mensagge}")
# Clase que utiliza los notificadores (Inyección de dependencias / Polimorfismo)
class User:
    def __init__(self, name, email, phone):
    # Este método acepta cualquier objeto que sea un 'Notificador'
        self.name = name
        self.email = email 
        self.phone = phone
        # Lógica para decidir qué dato de contacto usar según el tipo de notificador
        
    def alertar(self, notificador, mensagge):
        if isinstance(Notificador, NotifierEmail):
            destiny = self.email
        else:
            destiny = self.phone
            
        notificador.enviar(mensagge, destiny)
        
ulises = User("Ulises", "solisulises422@gmail.com", "21212412")

servicio_email = NotifierEmail()
sms_service = NotifierSMS()

ulises.alertar(servicio_email, "!Tu codigo funciona!")
ulises.alertar(sms_service, "!Nivel 4 completado!")

"""
TAREA:
1. Crea una clase base 'Componente' con marca, modelo y precio.
2. Crea clases hijas 'Procesador' (agrega atributo 'núcleos') y 'Disco' (agrega 'capacidad').
3. Crea una clase 'Carrito' que tenga una lista vacía de productos.
4. Implementa un método 'agregar' y un método 'ver_total'.
5. EXTRA: El método 'mostrar_detalle' del Carrito debe recorrer la lista y usar 
   polimorfismo para mostrar los datos específicos de cada pieza.
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 5: COMPOSICIÓN Y COLECCIONES DE OBJETOS ---
# Aquí vemos cómo una clase (Carrito) puede contener una lista de objetos de otra clase (Componente).
# Se usa 'isinstance' para identificar el tipo de objeto en tiempo de ejecución y mostrar detalles específicos.
# Esto simula un sistema real de compras donde diferentes objetos comparten una base común.
# Clase base con atributos comunes
class Componente:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

# Subclase con atributo extra 'nucleos'        
class Procesador(Componente):
    def __init__(self, marca, modelo, precio, nucleos):
        super().__init__(marca, modelo, precio)
        self.nucleos = nucleos

# Subclase con atributo extra 'capacidad'        
class Disco(Componente):
    def __init__(self, marca, modelo, precio, capacidad):
        super().__init__(marca, modelo, precio)
        self.capacidad = capacidad
        
class Carrito:
    def __init__(self):
        # Creamos una lista vacía donde vamos a meter los objetos
        self.productos = []
        
    # Agrega cualquier tipo de Componente a la lista
    def agregar(self, producto):
        self.productos.append(producto)
        print(f"Agregado: {producto.marca} {producto.modelo}")

    # Calcula la suma de precios usando una expresión generadora        
    def ver_total(self):
        total = sum(p.precio for p in self.productos)
        print(f"Total del carrito ${total}")

    # Muestra detalles usando Polimorfismo e inspección de tipos        
    def mostrar_detalle(self):
        print("---\n DETALLE DEL CARRITO ----")
        for p in self.productos:
            # Polimorfismo: cada objeto sabe qué datos tiene
            detalle = f"item {p.marca} {p.modelo} | Precio: ${p.precio}"
            # Usamos isinstance para dar el toque de "Ingeniero"
            if isinstance(p, Procesador):
                detalle += f" | Nucleos: {p.nucleos}"
            else:
                detalle += f" | Capacidad: {p.capacidad}"
        
            print(detalle)
        
        
# --- PRUEBA DEL CÓDIGO ---
# Creamos los componentes (como los de tu PC)
cpu = Procesador("amd", "ryzen 5 55600gt", 15000, 6)
ssd = Disco("Kinsgton", "480gb", 45000, "A500")

# usamos carrito
mi_compra = Carrito()
mi_compra.agregar(cpu)
mi_compra.agregar(ssd)

mi_compra.mostrar_detalle()
mi_compra.ver_total()


"""
TAREA:
1. Crea una clase 'PerfilUsuario'.
2. Atributos privados: '__username' y '__password'.
3. Usa @property para que el 'username' se pueda leer pero NO modificar.
4. Crea un método 'actualizar_password(vieja, nueva)'.
5. REGLA: Solo se cambia si 'vieja' coincide con la actual Y si 'nueva' tiene 8+ caracteres.
6. Agregá un @classmethod llamado 'crear_invitado' que devuelva un usuario 
   con nombre "Guest" y clave "00000000".
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 6: MÉTODOS DE CLASE (FACTORY) ---
# @classmethod recibe 'cls' (la clase) en lugar de 'self' (la instancia). 
# Se usa aquí como una "Fábrica": una forma rápida de crear un objeto preconfigurado (un Invitado) 
# sin que el usuario tenga que pasarle los datos manualmente.
class PerfilUsuario:
    def __init__(self, username, password):
        self.__username = username # Privado
        self.__password = password # Privado
        
    @property # Getter para el username (solo lectura)
    def username(self):
        return self.__username
    
    def actualizar_password(self, vieja, nueva):
        # Encapsulamiento: protegemos cómo se cambia la contraseña
        # Lógica de guardia:
        # 1. ¿La clave vieja que me das es igual a la que tengo guardada?
        if vieja == self.__password:
            # 2. ¿La nueva es lo suficientemente segura (8+ caracteres)?
            if len(nueva) >= 8:
                self.__password = nueva
                print("✅ Contraseña actualizada con éxito.")
            else:
                print("❌ Error: La nueva contraseña es muy corta (mínimo 8 caracteres).")
        else:
            print("❌ Error: La contraseña vieja no coincide.")

    @classmethod # Método de clase para crear instancias predefinidas (Factory pattern)
    def crear_invitado(cls):
        # Usamos 'cls' para crear una instancia de esta misma clase
        return cls("Guest", "00000000")

# --- PRUEBA DEL NIVEL 2 ---
usuario1 = PerfilUsuario("Ulises", "papi1234")

# Intentamos cambiar con clave vieja mal
usuario1.actualizar_password("error123", "nuevaClave123")

# Intentamos con clave vieja bien pero nueva muy corta
usuario1.actualizar_password("papi1234", "123")

# Cambio correcto
usuario1.actualizar_password("papi1234", "ingeniero2026")

# Crear invitado con el classmethod
invitado = PerfilUsuario.crear_invitado()
print(f"Usuario creado: {invitado.username}")


from abc import ABC, abstractmethod

"""
TAREA:
1. Crea la clase abstracta 'Entidad' con el método abstracto 'recibir_daño(cantidad)'.
2. Crea la clase 'Jugador' (con vida) que implemente 'recibir_daño' restando a su vida.
3. Crea la clase 'Enemigo' que haga lo mismo pero que imprima "El enemigo gritó de dolor".
4. Crea la clase 'Habilidad' que tenga un método 'activar(objetivo)'.
5. REGLA DE ORO: 'activar' debe poder recibir CUALQUIER Entidad y quitarle 20 de vida.
   (No importa si el objetivo es Jugador o Enemigo).
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 7: INTERFACES Y LÓGICA DE JUEGO ---
# Este ejercicio refuerza que el Polimorfismo permite tratar a un Jugador y a un Enemigo como una 'Entidad'.
# La clase 'Habilidad' no necesita saber qué está golpeando, solo que el objetivo sabe 'recibir_daño'.
# 1. ABSTRACCIÓN (El Contrato)
# Creamos una clase abstracta que sirve como "molde". 
# Obliga a que cualquier cosa que sea una 'Entidad' sepa cómo 'recibir_daño'.
class Entidad(ABC):
    @abstractmethod
    def recibir_daño(self, cantidad):
        pass
    
# 2. HERENCIA
# 'Jugador' y 'Enemigo' heredan de 'Entidad'. 
# Ambos CUMPLEN el contrato pero de formas distintas.
class Jugador(Entidad):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
    
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        print(f"🩸 {self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")
        
class Enemigo(Entidad):
    def __init__(self, tipo):
        self.tipo = tipo
        self.vida = 100
        
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        print(f"El {self.tipo} grito de dolor. Vida del enemgio {self.vida}")

# 3. POLIMORFISMO (La clave del ejercicio)
# La clase 'Habilidad' no sabe (ni le importa) si el 'objetivo' es un Jugador o un Enemigo.
# Solo sabe que, como es una 'Entidad', tiene el método 'recibir_daño'.
class Habilidad:
    def __init__(self, nombre_poder):
        self.nombre_poder = nombre_poder
        
    def activar(self, objetivo):
        print(f"Activando {self.nombre_poder}...")
        # Aquí ocurre el polimorfismo: el mismo método (.recibir_daño) 
        # hace cosas diferentes según el objeto que reciba.
        objetivo.recibir_daño(20)
        
# 4. EJECUCIÓN
ulises2 = Jugador("Ulises3", 100)
zombie = Enemigo("Zombie de resident evil")
fuego = Habilidad("Bola de fuego")
fuego.activar(zombie)  # El enemigo grita.
fuego.activar(ulises2) # El jugador muestra una gota de sangre.


"""
TAREA:
1. Crea una clase 'Persona' con nombre y edad.
2. Crea una clase 'Jugador' que herede de Persona y agregue 'posicion' y 'nro_camiseta'.
3. Crea una clase 'Equipo' que tenga un nombre y una lista de 'objetos Jugador'.
4. En 'Equipo', crea un método 'agregar_jugador(jugador)' que valide que no haya 
   más de 6 jugadores en la lista.
5. Crea un método 'presentar_equipo' que recorra la lista y muestre los datos de cada uno.
"""

# Tu código aquí...
# 1. Definimos la clase base 'Persona'
class Persona:
    def __init__(self, nombre, edad):
        # Guardamos los datos básicos que cualquier persona tiene
        self.nombre = nombre
        self.edad = edad
        

# 2. 'Jugador' hereda de 'Persona' (Herencia)
class Jugador(Persona):
    def __init__(self, nombre, edad, posicion, nro_camiseta):
        # super() envía el nombre y edad al constructor de Persona para no repetir código
        super().__init__(nombre, edad)
        # Agregamos los atributos específicos de un deportista
        self.posicion = posicion
        self.nro_camiseta = nro_camiseta
        
    
# 3. La clase 'Equipo' funcionará como un contenedor (Composición)
class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        # Inicializamos una lista vacía para guardar los OBJETOS de tipo Jugador
        self.jugadores = [] 
        
    def agregar_jugador(self, jugador):
        # Lógica de control: verificamos el tamaño de la lista antes de añadir
        if len(self.jugadores) < 6:
            self.jugadores.append(jugador)
            print(f"✅ {jugador.nombre} unido a {self.nombre_equipo}")
        else:
            # Si ya hay 6, bloqueamos la entrada
            print(f"❌ Error: El equipo {self.nombre_equipo} ya está completo.")
            
    def presentar_equipo(self):
        # Recorremos la lista de objetos y accedemos a sus atributos internos
        print(f"\n--- FORMACIÓN DE {self.nombre_equipo} ---")
        for j in self.jugadores:
            # Aquí se ve el poder de la POO: 'j' es un objeto con todas sus propiedades
            print(f"Nombre: {j.nombre} | Posición: {j.posicion} | Camiseta: {j.nro_camiseta}")

# --- PRUEBA DEL SISTEMA ---
# Instanciamos el objeto principal (el contenedor)
san_juan_voley = Equipo("San Juan Voley")

# Creamos instancias de la clase hija
j1 = Jugador("Ulises", 20, "Armador", 10)
j2 = Jugador("Carlos", 22, "Líbero", 5)

# Relacionamos los objetos: pasamos los jugadores al método del equipo
san_juan_voley.agregar_jugador(j1)
san_juan_voley.agregar_jugador(j2)

# Mostramos el resultado final
san_juan_voley.presentar_equipo()


from abc import ABC, abstractmethod

"""
TAREA:
1. Crea una clase abstracta 'Arma' con un método abstracto 'usar()'.
2. Crea 'Pistola' (imprime "Pum!") y 'Escopeta' (imprime "¡BOOM! Daño en área").
3. Crea una clase 'Inventario' que pueda guardar armas.
4. Implementa un método en Inventario llamado 'disparar_todo()' que recorra las armas 
   y ejecute el método 'usar()' de cada una.
5. EXTRA: Agregá un atributo '__municion' privado a las armas y restá 1 cada vez que se usen.
"""

# Tu código aquí...
# --- EXPLICACIÓN NIVEL 9: MANEJO DE ESTADOS Y PRIVACIDAD ---
# Aquí se practica el manejo de errores lógicos: no puedes disparar si no hay balas.
# El atributo privado '__municion' asegura que solo los métodos internos de la clase puedan restarla.
class Arma(ABC):
    def __init__(self, nombre, municion):
        self.nombre = nombre
        self.__municion = municion
        
    @property
    def municion(self):
        return self.__municion

    @abstractmethod
    def usar(self):
        pass
    
    
    def reducir_municion(self):
        if self.__municion > 0:
            self.__municion -= 1
        else:
            print(f"!Click! {self.nombre} no tiene balas")

class Pistola(Arma):
    def usar(self):
        if self.municion > 0:
            print(f"{self.nombre} !Pum! (Balas {self.municion - 1})")
            self.reducir_municion()
        else:
            print("Sin municion")
            
class Escopeta(Arma):
    def usar(self):
        if self.municion > 0:
            print(f"{self.municion}: !BOOM! Dano en area (Balas {self.municion - 1})")
            self.reducir_municion()
        else:
            print("Sin municion")
            
            
class Inventario:
    def __init__(self):
        self.armas = []
        
    def agregar_arma(self, arma):
        self.armas.append(arma)
        print(f"Guardado: {arma.nombre}")
        
    def disparar_todo(self):
        print("\n---- ZOMBIES A LA VISTA -----")
        for arma in self.armas:
            arma.usar()
            

# --- PRUEBA DEL DESAFÍO ---
mi_inventario = Inventario()

# Creamos las armas
glock = Pistola("Glock 17", 10)
remington = Escopeta("Remington 870", 5)

# Guardamos
mi_inventario.agregar_arma(glock)
mi_inventario.agregar_arma(remington)

# Usamos el polimorfismo
mi_inventario.disparar_todo()





#TAREA:
#1. Crea una clase 'ProductoHardware'.
#2. Atributos: nombre, __precio (privado), stock.
#3. Usa @property para leer el precio y un @setter para modificarlo, pero 
#   solo si el nuevo precio es mayor a cero.
#4. Crea un método 'vender(cantidad)' que reste al stock solo si hay suficiente.
#5. Crea un @classmethod llamado 'crear_desde_tu_pc' que devuelva un objeto 
#   ya configurado como "Ryzen 5 5600GT, 150000, 10".


# Tu código aquí...
class ProductoHardware:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor a 0")

    @classmethod
    def crear_desde_tu_pc(cls):
        return cls("Ryzen 5 5600GT", 150000, 10)


#TAREA:
#1. Crea la clase 'TarjetaSube'.
#2. Atributos: 'propietario' y '__saldo' (privado).
#3. Usa @property para poder consultar el saldo desde afuera.
#4. Crea el método 'cargar_saldo(monto)': debe sumar al saldo solo si el monto es > 0.
#5. Crea el método 'pagar_viaje()': debe restar 100 del saldo, pero SOLO si 
#   el saldo es suficiente. Si no, avisar con un print.


 #--- EXPLICACIÓN: PRÁCTICA DE ENCAPSULAMIENTO ---
 #Similar a la cuenta bancaria, protege el saldo de la tarjeta para que no sea negativo.
class TarjetaSube:
    def __init__(self, propietario, saldo_inicial):
        self.propietario = propietario
        self.__saldo = saldo_inicial
        
    
    @property
    def saldo(self):
        return self.__saldo
        
    
    def cargar_sube(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se pudo cargar el saldo exitosamente {self.__saldo}")
        else:
            print("Error no se pudo cargar su tarjeta sube ")
            
        
    def pagar_viaje(self):
        costo = 200
        if self.__saldo >= costo:
            self.__saldo -= costo
            print(f"Viaje pagado correctamente, tu saldo restante es ${self.__saldo}")
        else:
            print("Error: Saldo insuficiente")
        
        
mi_sube = TarjetaSube("Ulises", 200)
mi_sube.pagar_viaje()
mi_sube.cargar_sube(500)




#TAREA:
#1. Crea la clase padre 'Personaje' con 'nombre' y 'salud'.
#2. En 'Personaje', crea el método 'recibir_daño(cantidad)' que reste salud 
#   y avise si el personaje murió (salud <= 0).
#3. Crea la clase hija 'Leon' que herede de Personaje.
#4. En el __init__ de 'Leon', usá super() para el nombre y salud, 
#   y agregale el atributo 'habilidad'.
#5. Crea un método 'usar_habilidad()' en Leon que imprima un mensaje épico.

# --- EXPLICACIÓN: EXTENSIÓN DE CLASES ---
# Muestra cómo un hijo (Leon) puede tener más funcionalidades que el padre (curar, usar_habilidad).


class Personaje5:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        
    def recibir_dano(self, cantidad):
        self.salud -= cantidad
        if self.salud <= 10:
            self.salud = 0
            print(f"El {self.nombre} ha muerto")
        else:
            print(f"{self.nombre} recibio dano su salud es: {self.salud}")
            
class Leon(Personaje5):
    def __init__(self, nombre, salud, habilidad):
        super().__init__(nombre, salud)
        self.habilidad = habilidad
        
    def curar(self, cantidad):
        self.salud += cantidad
        print(f"✨ {self.nombre} se ha curado. Salud actual: {self.salud}")
        
    
    def usar_habilidad(self):
        print(f"{self.nombre} uso {self.habilidad} contra el zorro")

prota = Leon("Leon S Kennedy", 100, "Patada giratoria")
prota.recibir_dano(60)
prota.curar(30)
prota.usar_habilidad()



#TAREA:
#1. Crea la clase 'Database'.
#2. Atributo: '__conectado' (privado, empieza en False).
##3. Método 'conectar()': cambia el estado a True.
##4. Método 'desconectar()': cambia el estado a False.
#5. Método 'ejecutar_consulta(query)': 
 #  - SI está conectado: imprime "Ejecutando {query}".
 ##  - SI NO está conectado: imprime "Error: Sin conexión".

#EXPLICACIÓN: LÓGICA DE ESTADO 
# El objeto Database actúa como una máquina de estados (Conectado/Desconectado) que condiciona el éxito de sus métodos.

class Database:
    def __init__(self):
        self.__conectado = False
        
    def concectar(self):
        self.__conectado = True
        print("Conexion establecida con la base de datos")
    
    def desconectar(self):
        self.__conectado = False
        print("🔌 Conexión cerrada.")
    
    def ejecutar_consulta(self, query):
        if self.__conectado:
            print(f"Ejecutando consulta : '{query}'...")
        else:
            print("Error: No se puede haycer la consulta")
            
            
db = Database()

db.ejecutar_consulta("SELECT * FROM productos")
db.concectar()
db.ejecutar_consulta("SELECT * FROM productos")
db.concectar()



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

class Pedido:
    def __init__(self, plato, mesa, temperatura_coccion):
        self.plato = plato
        self.mesa = mesa
        self.temperatura_coccion = temperatura_coccion
        
class ChefRobot:
    def preparar(self, pedido):
        try:
            print(f"\n--- Recibiendo orden: {pedido.plato} ---")
            
            # Agregamos 'pedido.' antes de cada variable
            if pedido.temperatura_coccion < 60:
                raise ValueError("Riesgo sanitario: temperatura baja")
            
            if pedido.mesa == 0:
                raise Exception("Error de la sala: Mesa no asignada")
            
            print(f"👨‍🍳 Robot: {pedido.plato} en proceso de cocción.")
            return True
            
        # El try SIEMPRE necesita su except
        except ValueError as e:
            print(f"❌ ALERTA: {e}")
            return False
        except Exception as e:
            print(f"❌ ERROR: {e}")
            return False

class Cajero:
    def generar_ticket(self, pedido, precio):
        # Calculamos el 10% (multiplicar por 1.10)
        total = precio * 1.10
        print(f"--- TICKET MESA {pedido.mesa} ---")
        print(f"Producto: {pedido.plato}")
        print(f"Total con servicio (10%): ${total}")
        print("--------------------------")

# --- PRUEBA RAPIDA ---
pizza = Pedido("Pizza Especial", 5, 200)
robot = ChefRobot()
caja = Cajero()

if robot.preparar(pizza):
    caja.generar_ticket(pizza, 10000)