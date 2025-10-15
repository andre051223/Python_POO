class Persona:
    """
    Clase base que representa a una persona con atributos básicos.

    Atributos:
        nombre (str): Nombre de la persona
        edad (int): Edad de la persona
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase padre
        # Agregamos el atributo específico de Estudiante
        self.grado = grado

    def mostrar_grado(self):
        """
        Imprime el grado académico del estudiante.
        """
        print(f"Grado: {self.grado}")

    def mostrar_informacion(self):
        """
        Sobrescribe el método de la clase padre para mostrar información completa.
        Utiliza super() para llamar al método original y agregar más información.
        """
        # Llamamos al método de la clase padre
        super().mostrar_informacion()
        # Agregamos información específica del estudiante
        self.mostrar_grado()


# ============================================
# Programa Principal - Prueba del Sistema
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("SISTEMA DE GESTIÓN ESCOLAR")
    print("=" * 50)
    print()

    # Crear una instancia de Persona
    print("📋 Creando una Persona:")
    print("-" * 50)
    persona1 = Persona("Carlos Martínez", 45)
    persona1.mostrar_informacion()
    print()

    # Crear una instancia de Estudiante
    print("🎓 Creando un Estudiante:")
    print("-" * 50)
    estudiante1 = Estudiante("Ana García", 16, "10° Grado")
    estudiante1.mostrar_informacion()
    print()

    # Crear otro estudiante para demostrar reutilización
    print("🎓 Creando otro Estudiante:")
    print("-" * 50)
    estudiante2 = Estudiante("Luis Rodríguez", 14, "8° Grado")
    estudiante2.mostrar_informacion()
    print()

    # Demostrar el uso individual de métodos
    print("🔍 Usando métodos individuales:")
    print("-" * 50)
    print(f"El estudiante {estudiante1.nombre} tiene {estudiante1.edad} años")
    estudiante1.mostrar_grado()
    print()

    print("=" * 50)
    print("✅ Sistema funcionando correctamente")
    print("=" * 50)

