from .product import Product
class ShoppingCart():
    
    def __init__(self):
        self.products = []

    def empty(self):
        if len(self.products) == 0:
            return True
        return False

    def add_item(self, product:Product):
        self.products.append(product)

    def remove_item(self, product:Product):
        self.products.remove(product) 

    def get_items(self):
        return self.products

    def total(self):
        total = []
        for product in self.get_items():
            total.append(product.price - product.discount)
        return sum(total)

    @classmethod
    def check_database_online(cls):
        return True
