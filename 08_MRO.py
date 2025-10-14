#Metodo de resolución de orden
# Ejecutar según el orden de herencia

class A:
    def hablar(self):
        print("Hola, soy A")

class B(A):
    def hablar(self):
        print("Hola, soy B")
        super().hablar()  # Llama al método hablar de A

class C(A):
    def hablar(self):
        print("Hola, soy C")
        super().hablar()  # Llama al método hablar de A

class D(B, C):
    def hablar(self):
        print("Hola, soy D")
        super().hablar()  # Llama al método hablar de B

#creación de objeto
a = A()
a.hablar()

b = B()
b.hablar()

c = C()
c.hablar()

d = D()
d.hablar()