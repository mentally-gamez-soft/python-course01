python -m unittest discover tests
python -m unittest discover tests -v

python -m unittest tests/test_shopping_cart.py
python -m unittest tests/test_shopping_cart.py -v

python -m unittest tests.test_shopping_cart.TestShoppingCart
python -m unittest tests.test_shopping_cart.TestShoppingCart -v

python -m unittest tests.test_shopping_cart.TestShoppingCart.test_shopping_cart_is_not_empty
python -m unittest tests.test_shopping_cart.TestShoppingCart.test_shopping_cart_is_not_empty -v