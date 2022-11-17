import unittest

from core.cuenta import Cuenta

class TestIngresoEnCuenta(unittest.TestCase):

    def test_ingreso_cuenta_nueva_check_saldo_aumenta(self):
        # test pour une nouveau compta bancaire
        cuenta1 = Cuenta()
        cuenta1.ingresar_dinero(1000)
        self.assertEqual(cuenta1.saldo, 1000)

    def test_ingreso_cuenta_existente_check_saldo_aumenta(self):
        # un compte qui a deja un solde positif
        cuenta2 = Cuenta()
        cuenta2.saldo = 6000
        cuenta2.ingresar_dinero(1000)
        self.assertEqual(cuenta2.saldo, 7000)


if __name__ == "__main__":
    unittest.main()     