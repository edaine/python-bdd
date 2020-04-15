import unittest
from mock import Mock
from mock import patch
from app.account import Account


class AccountTest(unittest.TestCase):
    def test_account_returns_data_for_id_1(self):
        accountData = {"id": "1", "name": "test"}
        mockDataIF = Mock()
        mockDataIF.get.return_value = accountData
        account = Account(mockDataIF)
        self.assertDictEqual(accountData, account.get_account(1))

    def test_account_when_connect_exception_raised(self):
        mockDataIF = Mock()
        mockDataIF.get.return_value = "Connection error occurred. Try Again."
        account = Account(mockDataIF)
        self.assertEqual("Connection error occurred. Try Again.",
                         account.get_account(1))

    @patch('app.account.requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Some text data'
        mock_requests.get.return_value = mock_response
        account = Account(Mock())
        self.assertEqual({'status': 200, 'data': 'Some text data'},
                         account.get_current_balance('1'))


if __name__ == "__main__":
    unittest.main()
