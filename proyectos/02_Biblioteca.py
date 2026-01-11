# Proyecto: Biblioteca de Gestión de Libros
# Primera clase -> Libros
# Segunda clase -> Usuarios (miembros de la biblioteca)
# Tercera clase -> Bibliotecaria (gestiona libros y usuarios)

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Estado: {estado}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver_libro(self):
        self.disponible = True
        print (f"El libro '{self.titulo}' ha sido devuelto.")

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def mostrar_info(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolver_libro()
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no tiene el libro '{libro.titulo}' prestado.")

class Bibliotecaria:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado en la biblioteca.")

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.mostrar_info())

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.mostrar_info())

#Creación de objetos y demostración de funcionalidades

libro1 = Libro("Habitos Atomicos", "James Clear")
libro2 = Libro("Liderazgo", "Alex Ferguson")
libro3 = Libro("El Hombre en Busca de Sentido", "Viktor Frankl")
libro4 = Libro("ADN Barca", "Paco Seirullo")

usuario1 = Usuario("Ana Perez", 101)
usuario2 = Usuario("Luis Gomez", 102)

bibliotecaria = Bibliotecaria()
bibliotecaria.agregar_libro(libro1)
bibliotecaria.agregar_libro(libro2)
bibliotecaria.agregar_libro(libro3)
bibliotecaria.agregar_libro(libro4)
bibliotecaria.registrar_usuario(usuario1)
bibliotecaria.registrar_usuario(usuario2)
bibliotecaria.mostrar_libros()
bibliotecaria.mostrar_usuarios()

# Demostración de préstamos y devoluciones
print("\n--- Préstamos de libros ---")
usuario1.prestar_libro(libro1)
usuario2.prestar_libro(libro2)
usuario1.prestar_libro(libro3)

print("\n--- Estado después de los préstamos ---")
bibliotecaria.mostrar_libros()
bibliotecaria.mostrar_usuarios()

print("\n--- Devolución de libros ---")
usuario1.devolver_libro(libro1)

print("\n--- Estado final ---")
bibliotecaria.mostrar_libros()
bibliotecaria.mostrar_usuarios()
