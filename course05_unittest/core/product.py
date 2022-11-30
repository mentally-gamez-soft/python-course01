

class ProductDiscountSuperiorToPriceException(Exception):
    pass
class Product():
    """
    Class de produits.
    Cette classe contient 2 properties:
    - name: le nom du produit
    - price: le prix du produit
    """
    def __init__(self, name, price, discount=0.0):
        
        if price < discount:
            raise ProductDiscountSuperiorToPriceException("The discount cant be more than the price")

        self.name = name
        self.price = price
        self.discount = discount

    def code(self):
        return "code-{}".format(self.name)