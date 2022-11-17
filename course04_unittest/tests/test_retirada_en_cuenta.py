import unittest

from core.cuenta import Cuenta

class TestRetiradaEnCuenta(unittest.TestCase):

    def test_retirada_cuenta_existente_check_saldo_disminuye(self):
        cuenta1 = Cuenta()
        cuenta1.saldo = 6000
        cuenta1.retirada_dinero(1000)
        self.assertEqual(cuenta1.saldo, 5000)


    def test_retirada_cuenta_existente_check_saldo_insuficiente(self):
        cuenta2 = Cuenta()
        cuenta2.saldo = 6000 
        self.assertRaises(Exception, cuenta2.retirada_dinero, 8000)      # cuenta2.retirada_dinero(8000)



if __name__ == '__main__':
    unittest.main()    