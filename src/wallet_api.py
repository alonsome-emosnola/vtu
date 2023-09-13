from users.models import Profile
from src.vtpass_get import get_balance

class WalletAPI:
    
    MINIMUM_BAL = 50

    def __init__(self, username: str, email: str) -> str|None:
        self.username = username
        self.email = email
        user_wallet_bal = self.get_user_wallet_balance()
        admin_bal = self.get_admin_balance()
        if user_wallet_bal > admin_bal or user_wallet_bal <= self.MINIMUM_BAL:
            return ""
        else:
            pass
    
    def get_admin_balance(self):
        return get_balance()
    
    def get_user_wallet_balance(self):
        bal = Profile.objects.select_related('user').filter(user__username=self.username, user__email=self.email)[0].wallet_balance
        return bal

    def add_user_wallet_balance(self, amount:float):
        user = Profile.objects.select_related('user').filter(user__username=self.username, user__email=self.email)[0]
        user.wallet_balance = float(user.wallet_balance) + float(amount)
        user.save()

    def sub_user_wallet_balance(self, amount:float):
        user = Profile.objects.select_related('user').filter(user__username=self.username, user__email=self.email)[0]
        user.wallet_balance = float(user.wallet_balance) - float(amount)
        user.save()

    def fund_user_wallet(self, user:dict):
        pass

# WalletAPI("test2313", "test@test.com").add_user_wallet_balance(99.1)
bal = WalletAPI("test2313", "test@test.com").get_user_wallet_balance()
print(bal)