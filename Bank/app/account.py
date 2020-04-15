print('This will run when the file is imported.')


class Account(object):
    def __init__(self, id, balance):
        self.account_id = id
        self.account_balance = balance

    def get_account_id(self):
        return self.account_id

    def get_account_balance(self):
        return self.account_balance
