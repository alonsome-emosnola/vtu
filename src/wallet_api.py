
class WalletAPI:

    def __init__(self):
        self.user_balance = 0

    def get_user_wallet_balance(self):
        return self.user_balance

    def add_user_wallet_balance(self, amount):
        self.user_balance += amount

    def sub_user_wallet_balance(self, amount):
        self.user_balance -= amount

    def fund_wallet(self, amount, customer_name, customer_email, description):
        from monnify_api import get_customer_accounts
        from vtpass_get import get_balance
        if self.get_user_wallet_balance() >= get_balance():
            return "Maximum deposit reached"
        else:
            # get
            # get_customer_accounts()
            self.add_user_wallet_balance(amount)
            return "Success"
