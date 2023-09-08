from users.models import Profile

class WalletAPI:
    
    MINIMUM_BAL = 50

    def __init__(self):
        # wallet_balances = Profile.objects.get().wallet_balance
        # check if all users wallet balance is not equal or greater than admin balance and not less than minimum balance
        pass
    
    def get_admin_balance(self):
        pass
    
    def get_user_wallet_balance(self, username, email):
        bal = Profile.objects.select_related('user').filter(user__username=username, user__email=email)[0].wallet_balance
        return bal

    def add_user_wallet_balance(self, amount, username, email):
        user = Profile.objects.select_related('user').filter(user__username=username, user__email=email)[0]
        user.wallet_balance = user.wallet_balance + amount
        user.save()

    def sub_user_wallet_balance(self, amount, username, email):
        user = Profile.objects.select_related('user').filter(user__username=username, user__email=email)[0]
        user.wallet_balance = user.wallet_balance - amount
        user.save()

    def fund_user_wallet(self, user:dict):
        pass
    
# WalletAPI().sub_user_wallet_balance(200, "test2313", "test@test.com")
bal = WalletAPI().get_user_wallet_balance("test2313", "test@test.com")
print(bal)