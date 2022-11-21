import unittest

from core.account import Account

class TestDepositIntoAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account() 
        return super().setUp()

    def test_deposit_to_new_account_check_increased_balance(self):
        # test pour une nouveau compte bancaire
        self.account.add_amount(1000)
        self.assertEqual(self.account.balance, 1000)

    def test_deposit_to_existing_account_check_increased_balance(self):
        # un compte qui a deja un solde positif
        self.account.balance = 6000
        self.account.add_amount(1000)
        self.assertEqual(self.account.balance, 7000) 

if __name__ == "__main__":
    unittest.main()     