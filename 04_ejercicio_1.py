# Clase llamada Estudiante con atributos nombre, edad y grado..
# La clase debe tener un metodo llamado "estudiar" que imprima un mensaje indicando que el estudiante esta estudiando.
# El usuario debe poder ingresar los datos del estudiante por consola.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando.")

nombre = input("Ingresa el nombre del estudiante: ")
edad = input("Ingresa la edad del estudiante: ")
grado = input("Ingresa el grado del estudiante: ")
estudiante = Estudiante(nombre, edad, grado)
estudiante.estudiar()
print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Grado: {estudiante.grado}")