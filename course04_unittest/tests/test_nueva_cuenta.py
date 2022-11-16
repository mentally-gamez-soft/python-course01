import unittest
from core.cuenta import Cuenta

class TestNuevaCuenta(unittest.TestCase):

    def test_nueva_cuenta(self):
        cuenta1 = Cuenta()
        self.assertEqual(cuenta1.saldo, 0)

if __name__ == "__main__":
    unittest.main()        
