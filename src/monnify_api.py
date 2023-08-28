# from .monnify.pymonnify.pymonnify import InitializeMonnify
import os
from dotenv import load_dotenv
from src.monnify.monnify import get_token, monnifyCredential, Monnify

load_dotenv()

init = Monnify()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
CONTRACT_CODE = os.getenv("CONTRACT_CODE")
WALLET_ID = os.getenv("WALLET_ID")

login_credential = monnifyCredential(api_key=API_KEY, secret_key=SECRET_KEY, contract=CONTRACT_CODE, walletId=WALLET_ID, is_live=False)
token = get_token(login_credential)

# limit_profile = init.get_limit_profile(token, login_credential)
# print(limit_profile)

# reserve_limited_acc = init.reserve_account_with_limit(token, login_credential, '32PD2N23LBRF', CONTRACT_CODE, "TestLimit003_P1", "NGN", "ref-001-27/08/2023", "test@testlimit.com", "Test Limit")

print()


# reserve_account = init.reserve_account(token, login_credential, accountReference='tw663552', accountName='Samson Olu', customerEmail='olusam@gmail.com', customerName="Samson Olu", customerBvn='66377273233', availableBank=True)

# transfer = init.tranfer()
# check = init.verify_account(login_credential, 2106158261, 232)
# invoice = init.create_invoice(
#               login_credential, 
#               amount='1000', 
#               invoiceReference='uueyyws', 
#               description='test invoice', 
#               customerEmail='test@gmail.com', 
#               customerName='Samson', 
#               expiryDate='2023-08-30 12:00:00', 
#               paymentMethods=['CARD', 'ACCOUNT_TRANSFER', 'USSD'], 
#               redirectUrl='https://monnify-webhook.onrender.com/get-monnify-transactions/latest'
#               )

# wallet_balance = init.get_wallet_balance(login_credential)
# init.reserve_account_transactions(token, login_credential)

# invoiceReference
# accountReference
# transferReference


