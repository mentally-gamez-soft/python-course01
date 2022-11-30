import unittest
from core.product import Product, ProductDiscountSuperiorToPriceException

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.name = 'iphone 37'
        self.price = 3000
        self.mobile = Product(self.name, self.price)

    def tearDown(self) -> None:
        del self.mobile

    def test_product_object(self):
        # nombre = 'iphone'
        # price = 999.99
        # p = Product(nombre, price)
        self.assertEqual(self.mobile.name, 'iphone 37', 'the name of the product is different')
        self.assertEqual(self.mobile.price, 3000, 'the price of the product is different')

    def test_product_name(self):
        self.assertEqual(self.mobile.name, self.name, 'the name of the product is different')

    def test_product_price(self):
        self.assertEqual(self.mobile.price, self.price, 'The price of the product is different')

    def test_discount_error(self):
        """ Generate an exception when the discount is superior to the price of the item
        """        
        with self.assertRaises(ProductDiscountSuperiorToPriceException):
            Product(name="Iphone", price=100, discount=200)

    