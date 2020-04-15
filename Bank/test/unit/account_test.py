import unittest
from app.account import Account


class AccountTest(unittest.TestCase):

    def test_create_account_object_with_params(self):
        initID = "001"
        initBalance = 500
        account = Account(initID, initBalance)
        self.assertEqual(initID, account.get_account_id())
        self.assertEqual(initBalance, account.get_account_balance())


if __name__ == "__main__":
    print('This will get executed only if')
    print('the module is invoked directly.')
    print('It will not run when this module is imported')
    unittest.main()
