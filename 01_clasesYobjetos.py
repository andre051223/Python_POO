# Las clases son plantillas para crear objetos.
# Un objeto es una instancia de una clase.
# Atributos de clase (variables compartidas por todas las instancias)

class EquiposDeFutbol:
    def __init__(self, nombre, estadio, fundacion, titulos, entrenador, jugadores):
        #Creación del constructor de la clase
        self.nombre = nombre
        self.estadio = estadio
        self.fundacion = fundacion
        self.titulos = titulos
        self.entrenador = entrenador
        self.jugadores = jugadores

    def mostrar_informacion(self):
        #Método para mostrar la información del equipo
        print(f"Nombre: {self.nombre}")
        print(f"Estadio: {self.estadio}")
        print(f"Año de Fundación: {self.fundacion}")
        print(f"Títulos: {self.titulos}")
        print(f"Entrenador: {self.entrenador}")
        print(f"Jugadores: {', '.join(self.jugadores)}")

# Creación de objetos (instancias de la clase)
equipo1 = EquiposDeFutbol(
    nombre="FC Barcelona",
    estadio="Camp Nou",
    fundacion=1899,
    titulos=26,
    entrenador="Hansi Flick",
    jugadores=["Robert Lewandowski", "Lamine Yamal", "Raphinha"]
)

equipo2 = EquiposDeFutbol(
    nombre="Real Madrid",
    estadio="Santiago Bernabéu",
    fundacion=1902,
    titulos=34,
    entrenador="Xabi Alonso",
    jugadores=["Vinicius Junior", "Alvaro Carreras", "Kylian Mbappé"]
)

equipo3 = EquiposDeFutbol(
    nombre="Atlético de Madrid",
    estadio="Wanda Metropolitano",
    fundacion=1903,
    titulos=11,
    entrenador="Diego Simeone",
    jugadores=["Antoine Griezmann", "Jan Oblak", "Alexander Sorloth"]
)
