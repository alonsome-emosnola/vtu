from django.contrib.auth.models import User

class WalletAPI:

    def __init__(self):
        # initialize User table 
        # self.user = User.object.all()
        pass

    def get_user_wallet_balance(self, username:str|User|None, email:str|User|None=None):
        pass

    def add_user_wallet_balance(self, username=None, email=None):
        pass

    def sub_user_wallet_balance(self, amount):
        pass

    def fund_wallet(self, amount, customer_name, customer_email, description):
        pass
