# la encapsulación consiste en restringir el acceso directo a algunos de los componentes de un objeto.
# Esto se hace para proteger la integridad del objeto y evitar que su estado interno sea modificado de manera inapropiada.
# Ejemplo práctico - cuenta bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=250):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 100 dolares.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Cantidad inválida o fondos insuficientes.")

    def mostrar_saldo(self):
        return f"Saldo actual de {self.titular}: {self.__saldo}"

