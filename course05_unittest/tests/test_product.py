import unittest
from core.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        print("setUp() se lance avant chaque test")
        self.name = 'iphone 37'
        self.price = 3000
        self.mobile = Product(self.name, self.price)

    def tearDown(self) -> None:
        print("tearDown() se lance apres chaque test")
        del self.mobile

    def test_product_object(self):
        nombre = 'iphone'
        price = 999.99
        p = Product(nombre, price)
        self.assertEqual(p.name, 'iphone', 'El nombre es diferente')
        self.assertEqual(p.price, 999.99, 'El precio es diferente')

    def test_product_name(self):
        self.assertEqual(self.mobile.name, self.name, 'El nombre es diferente')

    def test_product_price(self):
        self.assertEqual(self.mobile.price, self.price, 'The price is different')