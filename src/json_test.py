# customer_Name = tt['data']['accountName']
# customer_Email = tt['data']['customerEmail']
# customer_Acc = tt['data']['accounts'][0]['accountNumber']
# bank_Name = tt['data']['accounts'][0]['bankName']
# acc_name = tt['data']['accounts'][0]['accountName']
# {
#     'message': 'success',
#     'statusCode': 200,
#     'responseCode': '0',
#     'data': {
#         'contractCode': '7067391661',
#         'accountReference': 'ACC_REF_RGTHC-1691426580.151831',
#         'accountName': 'Elu',
#         'currencyCode': 'NGN',
#         'customerEmail': 'elusieemmanuel@gmail.com',
#         'customerName': 'Alonsome',
#         'accounts': [
#             {
#                 'bankCode': '035',
#                 'bankName': 'Wema bank',
#                 'accountNumber': '5000290736',
#                 'accountName': 'Elu'
#             },
#             {
#             'bankCode': '232',
#             'bankName': 'Sterling bank',
#             'accountNumber': '6001344348',
#             'accountName': 'Elu'
#      }
#          ],
#             'collectionChannel': 'RESERVED_ACCOUNT',
#             'reservationReference': '8WSVFMLQTBV2V5GD7GKQ',
#             'reservedAccountType': 'GENERAL',
#             'status': 'ACTIVE',
#             'createdOn': '2023-08-07 17:42:59.883',
#             'incomeSplitConfig': [],
#             'bvn': '21061582610',
#             'restrictPaymentSource': False
#   }
#}
#
from builtins import super

name = "TEST"

class MainTest:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        print(self.name, self.age)


class Test(MainTest):
    def __init__(self):
        mt = MainTest("Emma", 12)
        super(MainTest, mt)
        print(name)
        print(mt.name)

# tt = Test()
# def test(name:str|int):
#     print(name)
    
# test(Test('10'))
