import unittest

from core.product import Product
from core.shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.shop_cart = ShoppingCart()

        self.mobile = Product('Iphone', 89.23)
        self.shop_cart2 = ShoppingCart()
        self.shop_cart2.add_item(self.mobile)


    def tearDown(self) -> None:
        del self.shop_cart
        del self.shop_cart2
        del self.mobile

    @classmethod
    def setUpClass(cls):
        print(" --- MESSAGE BEFORE ALL TESTS")

    @classmethod
    def tearDownClass(cls):
        print(" --- MESSAGE AFTER ALL TESTS")

    def test_shopping_cart_is_empty(self):        
        self.assertTrue(self.shop_cart.empty(), "Error the shopping cart is not empty")

    def test_shopping_cart_is_not_empty(self):
        self.assertFalse(self.shop_cart2.empty(), "Error the shopping cart is empty")

    def test_product_in_shopping_cart(self):
        self.assertIn(self.mobile, self.shop_cart2.get_items())

    def test_product_not_in_shopping_cart(self):
        self.shop_cart2.remove_item(self.mobile) 
        self.assertNotIn(self.mobile, self.shop_cart.get_items())

    def test_total_shopping_cart(self):
        item_1  = Product(name="le dernier des mohicans", price=10)
        item_2  = Product(name="Sony A7", price=1000, discount=200)
        self.shop_cart.add_item(item_1)
        self.shop_cart.add_item(item_2)

        self.assertEqual(self.shop_cart.total(), 810)  # Verifie l egailté du total
        self.assertGreater(self.shop_cart.total(), 0)  # verifie que le total est superior to zero
        self.assertLess(self.shop_cart.total(), 1000)

    @unittest.skip("The test id deprecated")
    def test_skip(self):
        self.assertEqual(1,1)
    
    # Skip a test if a service is not available
    @unittest.skipIf(ShoppingCart.check_database_online(), "The BDD is not available")
    def test_skip2(self):
        self.assertEqual(1,1)

    