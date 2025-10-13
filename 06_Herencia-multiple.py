class ProfesoresPerfila:
    def __init__(self, nombre, pais, asignatura):
        self.nombre = nombre
        self.pais = pais
        self.asignatura = asignatura

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, País: {self.pais}, Asignatura: {self.asignatura}"

class AsignaturasPerfila:
    def __init__(self, nombre_asignatura, area_estudio, nivel):
        self.nombre_asignatura = nombre_asignatura
        self.area_estudio = area_estudio
        self.nivel = nivel

    def mostrar_detalles_asignatura(self):
        return f"Asignatura: {self.nombre_asignatura}, Área de Estudio: {self.area_estudio}, Nivel: {self.nivel}"

#profesores
profesor_1 = ProfesoresPerfila( "Michelle Engelmann", "Ecuador", "Autoconocimiento, LinkedIn, Filosofía Estoica" )
profesor_2 = ProfesoresPerfila( "Silvia Alonso", "España", "Comunicación Efectiva, Productividad Personal, Oratoria" )
profesor_3 = ProfesoresPerfila( "Sandra Martinez", "España", "Gestión del Tiempo, Negociación, Gestión de Proyctos" )
profesor_4 = ProfesoresPerfila( "Ana Belén Fernández", "Mexico", "Trabajo en Equipo, Emprendimiento" )
profesor_5 = ProfesoresPerfila( "María Gómez", "España", "Marca Profesional, Pensameinto Critico" )
profesor_6 = ProfesoresPerfila( "Laura Rodríguez", "España", "Liderazgo" )
profesor_7 = ProfesoresPerfila( "Carlos Sánchez", "España", "Inteligencia Artificial" )

#asignaturas nivel básico
asignatura_1 = AsignaturasPerfila( "Autoconocimiento", "Desarrollo Personal", "Básico" )
asignatura_2 = AsignaturasPerfila( "Comunicación Efectiva", "Habilidades Blandas", "Básico" )
asignatura_3 = AsignaturasPerfila( "Gestión del Tiempo", "Productividad", "Básico" )
asignatura_4 = AsignaturasPerfila( "Trabajo en Equipo", "Habilidades Sociales", "Básico" )
asignatura_5 = AsignaturasPerfila( "Marca Profesional", "Desarrollo Profesional", "Básico")

#asignaturas nivel intermedio
asignatura_6 = AsignaturasPerfila( "Liderazgo", "Habilidades Directivas", "Intermedio" )
asignatura_7 = AsignaturasPerfila( "Inteligencia Artificial", "Tecnología", "Intermedio" )
asignatura_8 = AsignaturasPerfila( "LinkedIn", "Redes Profesionales", "Intermedio" )
asignatura_9 = AsignaturasPerfila( "Filosofía Estoica", "Filosofía", "Intermedio" )
asignatura_10 = AsignaturasPerfila( "Productividad Personal", "Productividad", "Intermedio" )

#asignaturas nivel avanzado
asignatura_11 = AsignaturasPerfila( "Oratoria", "Habilidades de Comunicación", "Avanzado" )
asignatura_12 = AsignaturasPerfila( "Negociación", "Habilidades Comerciales", "Avanzado" )
asignatura_13 = AsignaturasPerfila( "Gestión de Proyectos", "Administración", "Avanzado" )
asignatura_14 = AsignaturasPerfila( "Emprendimiento", "Negocios", "Avanzado" )
asignatura_15 = AsignaturasPerfila( "Pensamiento Crítico", "Habilidades Cognitivas", "Avanzado" )

print(profesor_1.mostrar_detalles())
print(profesor_2.mostrar_detalles())
print(profesor_3.mostrar_detalles())
print(profesor_4.mostrar_detalles())
print(profesor_5.mostrar_detalles())
print(profesor_6.mostrar_detalles())
print(profesor_7.mostrar_detalles())