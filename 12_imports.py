# ========================================
# IMPORTS EN PYTHON - GUÍA COMPLETA
# ========================================

# 1. IMPORTAR UN MÓDULO COMPLETO
# Sintaxis: import nombre_modulo
import math
import random

print("=== 1. Importar módulo completo ===")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Número aleatorio: {random.randint(1, 10)}")

# 2. IMPORTAR CON ALIAS
# Sintaxis: import nombre_modulo as alias
import datetime as dt

print("\n=== 2. Importar con alias ===")
print(f"Fecha actual: {dt.datetime.now()}")

# 3. IMPORTAR ELEMENTOS ESPECÍFICOS
# Sintaxis: from nombre_modulo import elemento
from math import pi, sqrt, pow

print("\n=== 3. Importar elementos específicos ===")
print(f"Valor de PI: {pi}")
print(f"Raíz de 25: {sqrt(25)}")
print(f"2 elevado a 3: {pow(2, 3)}")

# 4. IMPORTAR TODO EL CONTENIDO (No recomendado en proyectos grandes)
# Sintaxis: from nombre_modulo import *
from random import *

print("\n=== 4. Importar todo ===")
print(f"Número aleatorio con choice: {choice([1, 2, 3, 4, 5])}")

# 5. IMPORTAR ARCHIVOS QUE EMPIEZAN CON NÚMEROS
# Cuando los archivos empiezan con números, usamos importlib
print("\n=== 5. Importar archivos locales con números ===")

import importlib

# Importar módulo que empieza con número
modulo_clases = importlib.import_module("01_clasesYobjetos")
FcBarcelona = modulo_clases.FcBarcelona

equipo = FcBarcelona()
print(equipo.mostrar_info())

# 6. IMPORTAR MÚLTIPLES CLASES DE ARCHIVOS CON NÚMEROS
print("\n=== 6. Importar múltiples clases ===")

modulo_herencia = importlib.import_module("05_Herencia")
PlantillaBarcelona2025 = modulo_herencia.PlantillaBarcelona2025
PlantillaBarcelona2024 = modulo_herencia.PlantillaBarcelona2024
PlantillaBarcelona2023 = modulo_herencia.PlantillaBarcelona2023

plantilla_actual = PlantillaBarcelona2025()
print("Plantilla 2025:")
print(plantilla_actual.mostrar_plantilla())

# 7. IMPORTAR MÓDULO LOCAL COMPLETO CON ALIAS
print("\n=== 7. Importar módulo local completo ===")

poli = importlib.import_module("10_polimorfismo")

# Acceder a las clases del módulo
estudiante = poli.Estudiante("Carlos Pérez", 16, "11vo")
estudiante.mostrar_informacion()
estudiante.mostrar_grado()

# 8. IMPORTAR CON MANEJO DE EXCEPCIONES
# Útil cuando un módulo puede no estar instalado
print("\n=== 8. Importar con manejo de excepciones ===")

try:
    import pandas as pd
    print("Pandas está instalado")
except ImportError:
    print("Pandas no está instalado. Usa: pip install pandas")

# 9. IMPORTAR DESDE SUBCARPETAS
# Sintaxis: from carpeta.subcarpeta import modulo
# (Requiere que cada carpeta tenga un archivo __init__.py)
print("\n=== 9. Importar desde paquetes ===")
print("Para importar desde subcarpetas, crea:")
print("  - carpeta/__init__.py")
print("  - carpeta/modulo.py")
print("Luego: from carpeta.modulo import MiClase")

# 10. VERIFICAR MÓDULOS DISPONIBLES
print("\n=== 10. Módulos importados en este archivo ===")
import sys
print("Algunos módulos cargados:")
for i, modulo in enumerate(list(sys.modules.keys())[:5]):
    print(f"  - {modulo}")

# ========================================
# BUENAS PRÁCTICAS
# ========================================
print("\n=== BUENAS PRÁCTICAS ===")
print("""
1. Importar módulos estándar primero
2. Luego importar módulos de terceros
3. Finalmente importar módulos locales
4. Separar cada grupo con una línea en blanco
5. Usar imports absolutos cuando sea posible
6. Evitar imports circulares
7. No usar 'from modulo import *' en producción
8. Para archivos que empiezan con números, usar importlib
""")
