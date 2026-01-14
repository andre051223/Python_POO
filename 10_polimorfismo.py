# El polimorfismo es un principio de la programación orientada a objetos que permite que diferentes clases puedan ser tratadas como instancias de una clase común.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Persona - Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_informacion(self):  # Sobrescribe el método
        print(f"Estudiante - Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}")

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_informacion(self):  # Sobrescribe el método
        print(f"Profesor - Nombre: {self.nombre}, Edad: {self.edad}, Materia: {self.materia}")

# Ejemplo de polimorfismo
personas = [
    Persona("Juan", 30),
    Estudiante("Ana", 15, "10mo"),
    Profesor("Carlos", 40, "Matemáticas")
]

for persona in personas:
    persona.mostrar_informacion()  # Mismo método, diferentes comportamientos