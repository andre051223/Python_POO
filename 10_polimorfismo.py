# El polimorfismo es un principio de la programación orientada a objetos que permite que diferentes clases puedan ser tratadas como instancias de una clase común.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")


# Crear instancia de Estudiante
estudiante1 = Estudiante("Ana García", 15, "10mo")

# Imprimir información usando métodos heredados y propios
print("=== Información del Estudiante ===")
estudiante1.mostrar_informacion()  # Método heredado de Persona
estudiante1.mostrar_grado()  # Método propio de Estudiante

print(f"\nAcceso directo a atributos:")
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Grado: {estudiante1.grado}")