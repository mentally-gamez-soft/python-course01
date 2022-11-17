class Cuenta():
    saldo = 0 #variable de classe

    def ingresar_dinero(self, amount):
        self.saldo += amount

    def retirada_dinero(self, amount):
        if amount <= self.saldo:
            self.saldo -= amount
        else:
            raise Exception("El saldo es insuficiente")