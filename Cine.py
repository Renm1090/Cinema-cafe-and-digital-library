class Persona:
    lista = []

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def Registrar(self):
        Persona.lista.append(self)
        print(f"Persona registrada: {self.nombre} - {self.correo}")

    def ActualizarDatos(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        print(f"Los datos han sido actualizados")

    @classmethod
    def personas_registradas(cls):
        print(f"Personas registradas")
        for persona in cls.lista:
            print(f"Nombre: {persona.nombre} - Correo: {persona.correo}")

class Usuario(Persona):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.numreserva = []

    def reserva(self, funcion, asiento, promocion=None):
        if any(r.asiento == asiento and r.funcion == funcion for r in self.numreserva):
            print(f"El asiento {asiento} ya está reservado por {self.nombre}.")
            return None

        nueva_reserva = Reserva(self, funcion, asiento, promocion)
        if nueva_reserva.ConfirmarReserva(): 
            self.numreserva.append(nueva_reserva)
            return nueva_reserva
        return None

    def cancelar_reserva(self, asiento):
        for reserva in self.numreserva:
            if reserva.asiento == asiento:
                reserva.CancelarReserva()
                self.numreserva.remove(reserva)
                return
        print(f"No se encontró una reserva para el asiento {asiento}.")

    def acceder_promo(self):
        print(f"{self.nombre} accedió a una promoción.")


class Empleado(Persona):
    def __init__(self, nombre, correo, rol):
        super().__init__(nombre, correo)
        self.rol = rol

    def realizar_tarea(self):
        if self.rol in ["taquillero", "administrador"]:
            print(f"{self.nombre}, con rol {self.rol}, puede gestionar funciones.")
        else:
            print(f"{self.nombre}, con rol {self.rol} solo realiza tareas de limpieza.")

    def agregar_funcion(self, funciones, funcion):
        if self.rol in ["taquillero", "administrador"]:
            funciones.append(funcion)
            print(f"{self.nombre} agregó la función {funcion.pelicula.titulo} a las {funcion.hora}")
        else:
            print(f"{self.nombre} no tiene permisos para agregar funciones.")


class Espacio:
    def __init__(self, tamaño, identificador):
        self.tamaño = tamaño
        self.identicador = identificador

    def descripcion(self):
        print(f"El edificio tiene un tamaño de {self.tamaño} y su ID es {self.identicador}")


class Sala(Espacio):
    TIPO = ["2D", "3D", "IMAX"]

    def __init__(self, tipo):
        if tipo not in self.TIPO:
            raise ValueError(f"Tipo de sala no válido. Debe ser de tipo {self.TIPO}")
        self.disponibilidad = True
        self.tipo = tipo

    def consultar_disponibilidad(self):
        if self.disponibilidad:
            print(f"La sala está disponible")
        else:
            print(f"La sala no está disponible")


class Zona_comida(Espacio):
    def __init__(self):
        self.menu = {}

    def agregar_productos(self, producto, precio):
        self.menu[producto] = precio

    def mostrar_menu(self):
        print(f"Menú de Comida:")
        for producto, precio in self.menu.items():
            print(f"{producto}: ${precio}")


class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.clasificacion = clasificacion
        self.genero = genero

    def Detalles(self):
        print(f"Título: {self.titulo} \nDuración: {self.duracion} \nClasificación: {self.clasificacion} \nGénero: {self.genero}\n------------------------")

class Funcion:
    def __init__(self, hora, sala, pelicula):
        self.hora = hora
        self.sala = sala
        self.pelicula = pelicula
        self.asientos_disponibles = [f"A{i}" for i in range(1, 11)]  

    def consultar_asientos(self):
        print(f"Asientos disponibles para: {self.pelicula.titulo}\n Horario: {self.hora}\nAsientos Disponibles:  {','.join(self.asientos_disponibles)}\n__________________________________")

    def reservar_asientos(self, asiento):
        if asiento in self.asientos_disponibles:  
            self.asientos_disponibles.remove(asiento)  
            return True 
        else:
            print("Asiento no disponible")  
            return False  

    def liberar_asiento(self, asiento):
        if asiento not in self.asientos_disponibles: 
            self.asientos_disponibles.append(asiento)  
        else:
            print(f"El asiento {asiento} ya está disponible.")



class Promocion:
    def __init__(self, descuento, condicion):
        self.descuento = descuento
        self.condicion = condicion

    def Aplicar_promo(self, usuario):
        if self.condicion(usuario):
            print(f"Descuento del {self.descuento}% aplicado a {usuario.nombre}")
            return True
        return False


class Reserva:
    def __init__(self, usuario, funcion, asiento, promocion=None):
        self.usuario = usuario
        self.funcion = funcion
        self.asiento = asiento
        self.promocion = promocion

    def ConfirmarReserva(self):
        if self.funcion.reservar_asientos(self.asiento):
            print(f"Reserva confirmada para {self.usuario.nombre} en asiento {self.asiento} para la función {self.funcion.pelicula.titulo}.")
            if self.promocion:
                self.promocion.Aplicar_promo(self.usuario)
            return True
        print(f"No se pudo reservar el asiento {self.asiento} para {self.usuario.nombre}.") 
        return False

    def CancelarReserva(self):
        print(f"Reserva cancelada para {self.usuario.nombre} en asiento {self.asiento}.")
        self.funcion.liberar_asiento(self.asiento)



# Objetos

p1 = Persona("Luis", "luis@gamil.com")
p2 = Persona("Juan", "juan@gmail.com")
p3 = Persona("Pedro", "pedro@gmail.com")

em1 = Persona("Juju", "juju@gmail.com")
em2 = Persona("Jaimy", "Jaimy@gmail.com")
em3 = Persona("Isaac", "isaac@gmail.com")

p1.Registrar()
p2.Registrar()
p3.Registrar()
em1.Registrar()
em2.Registrar()
em3.Registrar()

Persona.personas_registradas()

user1 = Usuario("Luis", "luis@gmail.com")
user2 = Usuario("Juan", "juan@gmail.com")
user3 = Usuario("Pedro", "pedro@gmail.com")

em1 = Empleado("Juju", "juju@gmail.com", "administrador")
em2 = Empleado("Jaimy", "jaimy@gmail.com", "taquillero")
em3 = Empleado("Isaac", "isaac@gmail.com", "limpieza")

em1.realizar_tarea()
em2.realizar_tarea()
em3.realizar_tarea()

lugar = Espacio("110 m", 1234)
lugar.descripcion()

sal1 = Sala("3D")
sal2 = Sala("2D")
sal3 = Sala("IMAX")

sal1.consultar_disponibilidad()
sal2.consultar_disponibilidad()
sal3.consultar_disponibilidad()

men = Zona_comida()
men.agregar_productos("Palomitas", 70)
men.agregar_productos("Nachos", 45)
men.agregar_productos("Coca-Cola", 30)
men.agregar_productos("Agua", 20)

men.mostrar_menu()

peli1 = Pelicula("Your Name", "1:50", "A", "Romance")
peli2 = Pelicula("Mi vecino Totoro", "1:26", "AA", "Aventura/Fantasia")
peli3 = Pelicula("Aura", "1:30", "A", "Comedia/Romance")

peli1.Detalles()
peli2.Detalles()
peli3.Detalles()

fun1 = Funcion("1:15", sal1, peli1)
fun1.consultar_asientos()
fun1.reservar_asientos("A1")
fun1.consultar_asientos()

fun2 = Funcion("2:30", sal2, peli2)
fun2.consultar_asientos()
fun2.reservar_asientos("A5")
fun2.reservar_asientos("A5")
fun2.consultar_asientos()

fun3 = Funcion("2:30", sal3, peli3)
fun3.consultar_asientos()
fun3.reservar_asientos("A7")
fun3.consultar_asientos()

promo1 = Promocion(20, lambda usuario: usuario.nombre == "Pedro")

fun1.consultar_asientos()
res1 = Reserva(user1, fun1, "A10", promo1)
res1.ConfirmarReserva()







