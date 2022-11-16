import unittest

# def sum():
#     n1 = int(input("value 1:"))
#     n2 = int(input("value 2:"))
#     return n1 + n2

# result = sum()
# print(result)


# def lire_num():
#     return int(input("introduire numero:"))

# def sum(n1, n2):
#     return n1 + n2

# n1 = lire_num()
# n2 = lire_num()
# result = sum(n1, n2)
# print(result)

class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        n1 = 10
        n2 = 20
        result = n1 + n2

        # valor esperado: 30
        #assert result == 30

        self.assertEqual(result, 30)

    def test_rest_number(self):
        self.assertEqual(50-20, 30)

if __name__ == "__main__":
    unittest.main()