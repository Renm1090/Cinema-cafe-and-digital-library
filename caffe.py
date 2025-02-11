class Persona:
    list = []

    def __init__(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto

    def Registrar(self):
        Persona.list.append(self)
        print(f"Persona registrada: {self.nombre} - {self.contacto}")

    def actualizar_datos(self, nombre, contacto):
        self.nombre = nombre
        self.contacto = contacto
        print("Los datos han sido actualizados.")

    @classmethod
    def personas_registradas(cls):
        print("Personas Registradas:")
        for persona in cls.list:
            print(f"Nombre: {persona.nombre} - Contacto: {persona.contacto}")

class Cliente(Persona):
    def __init__(self, nombre, contacto):
        super().__init__(nombre, contacto)
        self.historial_pedido = []

    def RealizarPedido(self, pedido):
        if not isinstance(pedido, Pedido):  
            print("❌ Error: Debes pasar un objeto de la clase Pedido.")
            return
        self.historial_pedido.append(pedido) 
        print(f"\n✅ Pedido realizado para {self.nombre}:")
        pedido.mostrar_pedido()  

    def ConsultarHistorial(self):
        if not self.historial_pedido:  
            print(f"ℹ️ {self.nombre} no tiene pedidos en su historial.")
        else:
            print(f"\n📜 Historial de pedidos de {self.nombre}:")
            for i, pedido in enumerate(self.historial_pedido, 1):
                print(f"📦 Pedido {i}:")
                pedido.mostrar_pedido()

class Empleado(Persona):
    def __init__(self, nombre, contacto, rol):
        super().__init__(nombre, contacto)
        self.rol = rol

    def tarea(self):
        roles = {
            "Mesero": "toma las órdenes de los clientes.",
            "Barista": "prepara bebidas y hace trucos.",
            "Gerente": "dirige la cafetería."
        }
        print(f"{self.nombre} ({self.rol}) {roles.get(self.rol, 'realiza sus tareas en la cafetería.')}")

class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Bebida(ProductoBase):
    tipos_permitidos = ["caliente", "fría"]

    def __init__(self, nombre, tamaño, tipo, personalizar, precio):
        if tipo not in self.tipos_permitidos:
            raise ValueError("Tipo de bebida no válido. Debe ser 'caliente' o 'fría'")
        super().__init__(nombre, precio)
        self.tamaño = tamaño
        self.tipo = tipo
        self.personalizar = personalizar

    def menu_bebida(self):
        print(f"{self.nombre} ({self.tipo}, {self.tamaño}) - ${self.precio}")

class Postre(ProductoBase):
    def __init__(self, nombre, tipo_postre, precio):
        super().__init__(nombre, precio)
        self.tipo_postre = tipo_postre

    def menu_postre(self):
        print(f"{self.nombre} ({self.tipo_postre}) - ${self.precio}")

class Inventario:
    def __init__(self):
        self.items = {}

    def agregar_item(self, nombre, cantidad):
        if nombre in self.items:
            self.items[nombre] += cantidad
        else:
            self.items[nombre] = cantidad
        print(f"Agregado {cantidad} de {nombre} al inventario.")

    def verificar_stock(self, nombre, cantidad):
        return self.items.get(nombre, 0) >= cantidad

    def actualizar_stock(self, nombre, cantidad):
        if self.verificar_stock(nombre, cantidad):
            self.items[nombre] -= cantidad
            print(f"Se ha usado {cantidad} de {nombre}.")
        else:
            print(f"No hay suficiente stock de {nombre}.")

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.estado = "Pendiente"
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
        print(f"{producto.nombre} agregado al pedido.")

    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nombre} - Estado: {self.estado}")
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")
        print(f"Total: ${self.total}")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El pedido ahora está en estado: {self.estado}")

class Promocion:
    def __init__(self, nombre, descripcion, descuento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.descuento = descuento

    def aplicar_descuento(self, pedido):
        pedido.total -= self.descuento
        print(f"Descuento aplicado: ${self.descuento}. Nuevo total: ${pedido.total}")


cliente1 =  Persona("Ana", "ana@email.com") 
cliente2 = Persona("Carlos", "carlos@email.com")

cliente1.Registrar()
cliente2.Registrar()

Persona.personas_registradas()

empleado1 = Empleado("Luis", "luis@email.com", "Mesero")
empleado2 = Empleado("María", "maria@email.com", "Barista")
empleado3 = Empleado("Jaimy", "jaimy@email.com", "Gerente")

empleado1.Registrar()
empleado2.Registrar()
empleado3.Registrar()

Persona.personas_registradas()

empleado1.tarea()
empleado2.tarea()
empleado3.tarea()

bebida1 = Bebida("Café Latte", "Grande", "caliente", "Leche de almendra", 50)
bebida2 = Bebida("Té Helado", "Mediano", "fría", "Sin azúcar", 40)

empleado1.tarea()
empleado2.tarea()
empleado3.tarea()

postre1 = Postre("Brownie", "con gluten", 30)
postre2 = Postre("Galleta Vegana", "sin gluten", 25)

inventario = Inventario()
inventario.agregar_item("cafe", 50)
inventario.agregar_item("Té", 5)
inventario.agregar_item("Leche de almendra", 3)
inventario.agregar_item("Azúcar", 8)

promo = Promocion("Descuento de Cliente Frecuente", "Descuento por fidelidad", 10)

cliente1 = Cliente("Ana", "ana@email.com")  # Create an instance of Cliente

pedido1 = Pedido(cliente1)
pedido1.agregar_producto(bebida1)
pedido1.agregar_producto(postre2)
pedido1.mostrar_pedido()


if inventario.verificar_stock("Café", 1):
    inventario.actualizar_stock("Café", 1)


pedido1.cambiar_estado("En preparación")
pedido1.cambiar_estado("Entregado")


promo.aplicar_descuento(pedido1)
cliente1.RealizarPedido(pedido=pedido1)
cliente1.ConsultarHistorial()