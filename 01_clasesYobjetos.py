
# Clases son plantillas para crear objetos.
# Un objeto es una instancia de una clase.

class FcBarcelona:
    # Atributos de clase (variables compartidas por todas las instancias)
    nombre = "Futbol Club Barcelona"
    fundacion = 1899
    estadio = "Spotify Camp Nou"
    titulos_liga = 26  # Número de títulos de liga ganados
    titulos_champions = 5  # Número de títulos de Champions League ganados

    # Método de clase
    def mostrar_info(self):
        return f"{self.nombre}, fundado en {self.fundacion}, juega en el estadio {self.estadio} y ha ganado {self.titulos_liga} títulos de liga y {self.titulos_champions} titulos de Champions League."

equipo = FcBarcelona()
print(equipo.mostrar_info())