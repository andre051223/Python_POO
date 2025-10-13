# Copilot-Instructions-POO-Python.md

## 🎯 Objetivo del Archivo

Este documento guía a **GitHub Copilot** para que sus sugerencias estén enfocadas en el aprendizaje **intermedio de Programación Orientada a Objetos (POO) con Python**, favoreciendo ejemplos prácticos, comprensión de conceptos y código limpio.

---

## 👩‍💻 Contexto de Aprendizaje

* Rol actual: **Frontend Developer** en proceso de adquirir habilidades backend.
* Objetivo actual: Entender y aplicar los principios de la POO en Python para construir estructuras de código más organizadas y reutilizables.

---

## 🧠 Nivel de Conocimiento Esperado

* Nivel: **Básico**.
* Las sugerencias deben incluir **comentarios explicativos**.
* Se deben evitar patrones avanzados (como metaclases o decoradores complejos), salvo con explicación didáctica.

---

## 💡 Recomendaciones de Estilo

1. Usar **nombres descriptivos** para clases y métodos (en formato `CamelCase` para clases y `snake_case` para métodos).
2. Incluir **docstrings** explicativos en clases y métodos.
3. Priorizar ejemplos prácticos y autoexplicativos.
4. Mostrar cómo **instanciar y utilizar objetos**.
5. Introducir gradualmente conceptos como **herencia, encapsulamiento y polimorfismo**.

---

## 🧩 Temas Prioritarios

1. **Clases y Objetos:** definición, atributos, métodos.
2. **Método `__init__`:** inicialización de atributos.
3. **Encapsulamiento:** uso de propiedades (`@property`).
4. **Herencia:** clases padre e hijas, uso de `super()`.
5. **Polimorfismo:** redefinición de métodos.
6. **Composición:** objetos dentro de otros objetos.
7. **Buenas prácticas:** separación lógica y reutilización del código.

---

## 🧩 Ejemplo de Interacción Esperada

> **Prompt:** "Crea un ejemplo de herencia en Python usando clases Animal y Perro"
>
> **Respuesta esperada de Copilot:**
>
> ```python
> class Animal:
>     def __init__(self, nombre):
>         self.nombre = nombre
>
>     def hacer_sonido(self):
>         print("Este animal hace un sonido.")
>
>
> class Perro(Animal):
>     def hacer_sonido(self):
>         print(f"{self.nombre} dice: ¡Guau guau!")
>
>
> mi_perro = Perro("Rocky")
> mi_perro.hacer_sonido()
> ```

---

## ✅ Objetivo Final

Aplicar correctamente los principios de la POO en proyectos Python reales, comprendiendo cómo estructurar código reutilizable, escalable y fácil de mantener.
