import unittest

from core.account import Account

class TestWithdrawFromAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account = Account()
        self.account.balance = 6000
        return super().setUp()

    def test_withdraw_from_existing_account_check_balance_lowers(self):
        self.account.withdraw_amount(1000)
        self.assertEqual(self.account.balance, 5000)

    def test_withdraw_from_account_check_insuficient_balance(self):
        self.assertRaises(Exception, self.account.withdraw_amount, 8000)      # self.account.withdraw_amount(1000)

if __name__ == '__main__':
    unittest.main()   