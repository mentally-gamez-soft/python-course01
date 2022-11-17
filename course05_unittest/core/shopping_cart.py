
class ShoppingCart():
    
    def __init__(self):
        self.products = []

    def empty(self):
        if len(self.products) == 0:
            return True
        return False

    def add_item(self, product):
        self.products.append(product)