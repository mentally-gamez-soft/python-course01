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

    def test_shopping_cart_is_empty(self):        
        self.assertTrue(self.shop_cart.empty(), "Error the shopping cart is not empty")

    def test_shopping_cart_is_not_empty(self):
        self.assertFalse(self.shop_cart2.empty(), "Error the shopping cart is empty")