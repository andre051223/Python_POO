class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito: {monto}. Nuevo saldo: {self.saldo}")
        else:
            print("El monto del depósito debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro: {monto}. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto del retiro debe ser positivo.")

    def obtener_saldo(self):
        return self.saldo

    def obtener_info_cuenta(self):
        return {
            "Número de cuenta": self.numero_cuenta,
            "Titular": self.titular,
            "Saldo": self.saldo
        }
