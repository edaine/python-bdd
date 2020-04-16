from nose.tools import assert_equal, assert_in
from webtest import TestApp

from app.bank_app import app, BANK
from app.account import Account


class robotLibrary(object):
    def __init__(self):
        self.browser = None
        self.response = None
        self.form_response = None

    def Create_Account(self, account_number, balance):
        a = Account(account_number, balance)
        BANK.add_account(a)

    def Visit_Homepage(self):
        self.browser = TestApp(app)
        self.response = self.browser.get('http://${SERVER}/')
        assert_equal(self.response.status_code, 200)

    def Retrieve_Account(self, account_number):
        form = self.response.forms['account-form']
        form['account_number'] = account_number
        self.form_response = form.submit('submit')
        assert_equal(self.form_response.status_code, 200)

    def Display_Balance(self, expected_balance):
        assert_in("Balance: {}".format(expected_balance),
                  self.form_response.text)
