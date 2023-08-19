# from .monnify.pymonnify.pymonnify import InitializeMonnify
import os
from dotenv import load_dotenv
from monnify.monnify import get_token, monnifyCredential, Monnify

load_dotenv()

init = Monnify()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
CONTRACT_CODE = os.getenv("CONTRACT_CODE")
WALLET_ID = os.getenv("WALLET_ID")

login_credential = monnifyCredential(api_key=API_KEY, secret_key=SECRET_KEY, contract=CONTRACT_CODE, walletId=WALLET_ID, is_live=False)
token = get_token(login_credential)

reserve_account = init.reserve_account(token, login_credential, accountReference='tw663552', accountName='Samson Olu', customerEmail='olusam@gmail.com', customerName="Samson Olu", customerBvn='66377273233', availableBank=True)
print(reserve_account)

# init = InitializeMonnify(apiKey=API_KEY, secretKey=SECRET_KEY, contractCode=CONTRACT_CODE, refStart="EMP",currencyCode="NGN")


# def make_deposit(amount, customer_email, customer_name, payment_description, redirect_url="https://monnify.com"):
#     try:
#         t = init.initializeTransaction(amount=amount, customerEmail=customer_email, customerName=customer_name,
#                                        paymentDescription=payment_description)
#         return t
#     except Exception:
#         print("Something went wrong, please try again")
#     else:
#         # redirect user to redirect_url
#         # notify user via email or SMS
#         pass


# def get_customer_reserved_accounts(customer_name, customer_email, customer_BVN, bankCodes):
#     try:
#         tt = init.reserveBankAccount(customerBVN=customer_BVN, customerEmail=customer_email,customerName=customer_name, preferredCodes=bankCodes)
#     except ConnectionError as e:
#         print("Error trying to connect, please check your internet connection " + e.strerror)
#     except Exception as e:
#         print(e)
#     else:
#         return tt
        
# accs = get_customer_reserved_accounts("Elon", "elon@elon.com", "21061582610", [232, "035"])
# print(accs)

