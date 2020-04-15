class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, new_account):
        self.accounts[new_account.account_id] = new_account.account_balance

    def get_account_balance(self, account_id):
        return self.accounts[account_id]
