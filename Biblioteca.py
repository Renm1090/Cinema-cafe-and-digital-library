from datetime import datetime, timedelta

class Material:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

    def mostrar_info(self):
        return f"{self.titulo} - {'Disponible' if self.disponible else 'No disponible'}"

    def actualizar_estado(self, estado):
        self.disponible = estado

class Libro(Material):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo)
        self.autor = autor
        self.genero = genero

class Revista(Material):
    def __init__(self, titulo, edicion, periocidad):
        super().__init__(titulo)
        self.edicion = edicion
        self.periocidad = periocidad

class MaterialDigital(Material):
    def __init__(self, titulo, tipo_archivo, enlace):
        super().__init__(titulo)
        self.tipo_archivo = tipo_archivo
        self.enlace = enlace

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Usuario(Persona):
    def __init__(self, nombre, email, id_usuario):
        super().__init__(nombre, email)
        self.id_usuario = id_usuario
        self.material_prestado = []
        self.multas = 0
    
    def prestar_material(self, material):
        if material.disponible:
            self.material_prestado.append(material)
            material.actualizar_estado(False)
            print(f"{material.titulo} prestado a {self.nombre}")
        else:
            print("Material no disponible para préstamo")
    
    def devolver_material(self, material, fecha_devolucion):
        if material in self.material_prestado:
            self.material_prestado.remove(material)
            material.actualizar_estado(True)
            print(f"{material.titulo} devuelto por {self.nombre}")
            
            if fecha_devolucion > datetime.now():
                print("Devolución tardía. Se aplicará una multa.")
                self.multas += 50  
        else:
            print("Este material no pertenece a este usuario.")



    def mostrar_estado(self):
        print(f"Usuario: {self.nombre}, Multas acumuladas: ${self.multas}")
        print("Materiales prestados:")
        for material in self.material_prestado:
            print(f"- {material.titulo}")


class Bibliotecario(Persona):
    def __init__(self, nombre, email, id_bibliotecario):
        super().__init__(nombre, email)
        self.id_bibliotecario = id_bibliotecario

    def agregar_material(self, sucursal, material):
        sucursal.materiales.append(material)
        print(f"Material {material.titulo} añadido al sistema")

    def transferir_material(self, material, sucursal_origen, sucursal_destino):
        if material in sucursal_origen.materiales:
            sucursal_origen.materiales.remove(material)
            sucursal_destino.materiales.append(material)
            print(f"{material.titulo} transferido a {sucursal_destino.nombre}")
        else:
            print("El material no está en la sucursal origen")
        
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales = []
        self.usuarios = []
        self.bibliotecarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} registrado en {self.nombre}")

    def buscar_material(self, titulo):
        for material in self.materiales:
            if material.titulo.lower() == titulo.lower():
                return material.mostrar_info()
        return "Material no encontrado"




libro1 = Libro("1984", "George Orwell", "Ficción")
libro2 = Libro("Cien Años de Soledad", "Gabriela Garcia", "Realismo")
libro3 = Libro("Crónica de una muerte anunciada", "Gabriela Garcia", "Misterio")

revista1 = Revista("National Geographic", " Edicion 2024", "Mensual")
revista2 = Revista("Forbes", "Edicion 2023", "Mensual")
revista3 = Revista("Popular Science", "Edicion Primavera", "Trismetral")

mdigital = MaterialDigital("Curso de Python Avanzado", "PDF", "https://curso-python.com")
mdigita2 = MaterialDigital("Enciclopedia de Ciencia Moderna", "PDF", "https://ciencia-moderna.org")

user1 = Usuario("Juan", "juan@gamil.com", 2303)
user2 = Usuario("Luna", "luna@gmail.com", 3203)
user3 = Usuario("Daniel", "daniel@gmail.com", 5768)

sucursal1 = Sucursal("Biblioteca Central")

sucursal1.registrar_usuario(user1)
sucursal1.registrar_usuario(user2)
sucursal1.registrar_usuario(user3)




user1.prestar_material(libro3)
fecha_devolucion = datetime.now() - timedelta(days=2)
fecha_devolucion = datetime.now() - timedelta(days=2)
user1.devolver_material(libro1, fecha_devolucion)

user1.devolver_material(libro3, fecha_devolucion)

user1.mostrar_estado()

user2.prestar_material(revista1)
fecha_devolucion = datetime.now() + timedelta(days=5)

user3.prestar_material(mdigita2)

biblio1 = Bibliotecario("Ana", "ana@gmail.com", 2345)

biblio1 = Bibliotecario("Ana", "ana@gmail.com", 2345)

biblio1.agregar_material(sucursal1, libro1)
biblio1.agregar_material(sucursal1, libro2)
biblio1.agregar_material(sucursal1, libro3)

biblio1.agregar_material(sucursal1, revista1)
biblio1.agregar_material(sucursal1, revista2)
biblio1.agregar_material(sucursal1, revista3)

biblio1.agregar_material(sucursal1, mdigital)
biblio1.agregar_material(sucursal1, mdigita2)




