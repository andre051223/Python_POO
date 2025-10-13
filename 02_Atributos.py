# Los atributos se definen dentro del método __init__ de la clase.
# def se inicializan cuando se crea una instancia de la clase.
# def str se utiliza para definir la representación en cadena (string) de un objeto.


class Equipos:
    def __init__(self, nombre_equipo, pais, entrenador, estadio, titulos):
        self.nombre_equipo = nombre_equipo
        self.pais = pais
        self.entrenador = entrenador
        self.estadio = estadio
        self.titulos = titulos

    def mostrar_info(self):
        return f"{self.nombre_equipo} de {self.pais}, entrenado por {self.entrenador}, juega en {self.estadio} y tiene {self.titulos} títulos."

# Crear instancias fuera de la clase
equipo1 = Equipos("Real Madrid", "España", "Xabi Alonso", "Santiago Bernabéu", 34)
equipo2 = Equipos("Manchester United", "Inglaterra", "Ruben Amorim", "Old Trafford", 20)
equipo3 = Equipos("Bayern Munich", "Alemania", "Vicent Kompany", "Allianz Arena", 31)
equipo4 = Equipos("Juventus", "Italia", "Massimiliano Allegri", "Allianz Stadium", 36)
equipo5 = Equipos("Paris Saint-Germain", "Francia", "Luis Enrique", "Parc des Princes", 10)
equipo6 = Equipos("FC Barcelona", "España", "Hansi Flick", "Spotify Camp Nou", 26)

print(equipo1.mostrar_info())
print(equipo2.mostrar_info())
print(equipo3.mostrar_info())
print(equipo4.mostrar_info())
print(equipo5.mostrar_info())
print(equipo6.mostrar_info())