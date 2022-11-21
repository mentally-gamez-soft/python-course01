import unittest
from core.account import Account

class TestNewAccount(unittest.TestCase):

    def test_new_account(self):
        account = Account()
        self.assertEqual(account.balance, 0)

if __name__ == "__main__":
    unittest.main()        
