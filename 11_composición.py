class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    def mostrar_info(self):
        return f"{self.nombre} - {self.ciudad}"


class Libro:
    def __init__(self, titulo, autor, editorial, año):
        self.titulo = titulo
        self.autor = autor  # Composición: Libro "tiene un" Autor
        self.editorial = editorial  # Composición: Libro "tiene una" Editorial
        self.año = año

    def mostrar_informacion_completa(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.mostrar_info()}")
        print(f"Editorial: {self.editorial.mostrar_info()}")
        print(f"Año: {self.año}")


# Crear instancias
autor1 = Autor("Gabriel García Márquez", "Colombiano")
editorial1 = Editorial("Sudamericana", "Buenos Aires")

# Crear libro usando composición
libro1 = Libro("Cien años de soledad", autor1, editorial1, 1967)

# Mostrar información
libro1.mostrar_informacion_completa()

print("\n--- Otro libro del mismo autor ---")
autor2 = Autor("Isabel Allende", "Chilena")
editorial2 = Editorial("Plaza & Janés", "Barcelona")

libro2 = Libro("La casa de los espíritus", autor2, editorial2, 1982)
libro2.mostrar_informacion_completa()

autor3 = Autor("James Clear", "Estadounidense")
editorial3 = Editorial("Avery", "Nueva York")
libro3 = Libro("Hábitos Atómicos", autor3, editorial3, 2018)

print("\n--- Otro libro ---")
libro3.mostrar_informacion_completa()