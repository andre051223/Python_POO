# La herencia permite crear una nueva clase basada en una clase existente.

class PlantillaBarcelona:
    def __init__(self, portero, defensas, mediocampistas, delanteros):
        self.portero = portero
        self.defensas = defensas
        self.mediocampistas = mediocampistas
        self.delanteros = delanteros

    def mostrar_plantilla(self):
        return f"Portero: {self.portero}\nDefensas: {', '.join(self.defensas)}\nMediocampistas: {', '.join(self.mediocampistas)}\nDelanteros: {', '.join(self.delanteros)}"

#Creación de Plantillas de diferentes años mediante herencia
class PlantillaBarcelona2025(PlantillaBarcelona):
    def __init__(self):
        super().__init__(
            portero="Wojhciech Szczesny",
            defensas=["Jules Koundé", "Ronald Araújo", "Andreas Christensen", "Alejandro Balde"],
            mediocampistas=["Frenkie de Jong", "Pedri", "Gavi"],
            delanteros=["Robert Lewandowski", "Raphinha", "Lamine Yamal"]
        )
class PlantillaBarcelona2024(PlantillaBarcelona):
    def __init__(self):
        super().__init__(
            portero="Marc-André ter Stegen",
            defensas=["Jules Koundé", "Ronald Araújo", "Andreas Christensen", "Alejandro Balde"],
            mediocampistas=["Frenkie de Jong", "Gavi", "Ilkay Gündogan"],
            delanteros=["Robert Lewandowski", "Raphinha", "Ferran Torres"]
        )

class PlantillaBarcelona2023(PlantillaBarcelona):
    def __init__(self):
        super().__init__(
            portero="Marc-André ter Stegen",
            defensas=["Jules Koundé", "Ronald Araújo", "Andreas Christensen", "Jordi Alba"],
            mediocampistas=["Sergio Busquets", "Pedri", "Frenkie de Jong"],
            delanteros=["Robert Lewandowski", "Raphinha", "Ansu Fati"]
        )

class PlantillaBarcelona2022(PlantillaBarcelona):
    def __init__(self):
        super().__init__(
            portero="Marc-André ter Stegen",
            defensas=["Dani Alves", "Gerard Piqué", "Eric Garcia", "Jordi Alba"],
            mediocampistas=["Sergio Busquets", "Pedri", "Gavi"],
            delanteros=["Pierre-Emerick Aubameyang", "Ferran Torres", "Ousmane Dembélé"]
        )

plantilla_2025 = PlantillaBarcelona2025()
plantilla_2024 = PlantillaBarcelona2024()
plantilla_2023 = PlantillaBarcelona2023()
plantilla_2022 = PlantillaBarcelona2022()

print("Plantilla FC Barcelona 2025:")
print(plantilla_2025.mostrar_plantilla())
print("Plantilla FC Barcelona 2024:")
print(plantilla_2024.mostrar_plantilla())
print("Plantilla FC Barcelona 2023:")
print(plantilla_2023.mostrar_plantilla())
print("Plantilla FC Barcelona 2022:")
print(plantilla_2022.mostrar_plantilla())

