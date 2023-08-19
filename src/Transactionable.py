from abc import ABC, abstractmethod

class Transactionable(ABC):
    
    def __str__(self) -> str:
        return super().__str__()
    
    @abstractmethod
    def get_transaction(self, transaction_id:str|dict) -> dict:
        """Gets one transaction using @param = transaction_id """
        pass
    @abstractmethod
    def get_transactions(self) -> list:
        """"Gets all transactions all at once"""
        pass
    @abstractmethod
    def set_transaction_details(self, transaction_id:str|dict, **kwargs:dict) -> dict:
        """Sets one transaction using @param = transaction_id using @param = **kwargs"""
        pass
    @abstractmethod
    def set_all_transactions_details(self, **kwargs:dict) -> list:
        """Sets all transactions using @param = **kwargs"""
        pass
    
class AirtimeTransactions(Transactionable):
    
    def __init__(self) -> None:
        print(self.__str__())
        
    def __str__(self) -> str:
        return f"Printing from the __str__() method"
        
    def get_transaction(self, transaction_id: str | dict) -> dict:
        return {"type": "dict"}
    
    def get_transactions(self) -> list:
        return super().get_transactions()
    
    def set_transaction_details(self, transaction_id: str | dict, **kwargs: dict) -> dict:
        return super().set_transaction_details(transaction_id, **kwargs)
    
    def set_all_transactions_details(self, **kwargs: dict) -> list:
        return super().set_all_transactions_details(**kwargs)
    
class DataTransactions(Transactionable):
    tt = Transactions.objects.all()
    
    details = [
        {
            "status": "delivered",
            "product_name": "GLO Data",
            "unique_element": "08011111111",
            "unit_price": 100,
            "quantity": 1,
            "service_verification": None,
            "channel": "api",
            "commission": 4,
            "total_amount": 96,
            "discount": None,
            "type": "Data Services",
            "email": "elusie@gmail.com",
            "phone": "08139746712",
            "name": None,
            "convinience_fee": 0,
            "amount": "100.00",
            "platform": "api",
            "method": "wallet",
            "transactionId": "16920947991155375524134010"
        }, 
        {
            "status": "delivered",
            "product_name": "MTN Data",
            "unique_element": "08011111111",
            "unit_price": 200,
            "quantity": 1,
            "service_verification": None,
            "channel": "api",
            "commission": 4,
            "total_amount": 196,
            "discount": None,
            "type": "Data Services",
            "email": "emmanuel@gmail.com",
            "phone": "08139746712",
            "name": None,
            "convinience_fee": 0,
            "amount": "200.00",
            "platform": "api",
            "method": "wallet",
            "transactionId": "16920947991155375524134000"
        },
        {
            "status": "delivered",
            "product_name": "MTN Data",
            "unique_element": "08011111111",
            "unit_price": 200,
            "quantity": 1,
            "service_verification": None,
            "channel": "api",
            "commission": 4,
            "total_amount": 196,
            "discount": None,
            "type": "Data Services",
            "email": "emmanuel@gmail.com",
            "phone": "08139746712",
            "name": None,
            "convinience_fee": 0,
            "amount": "200.00",
            "platform": "api",
            "method": "wallet",
            "transactionId": "16920947991155375524134111"
        }
    ]
    
    def __init__(self) -> None:
        pass
        
    def __str__(self) -> str:
        return f"Your transaction details are: {self.details}"
        
    def get_transaction(self, transaction_id: str | dict) -> dict|None:
        for detail in self.details:
            if type(transaction_id) == str and detail["transactionId"] == transaction_id:
                return detail
            elif type(transaction_id) == dict and detail["transactionId"] == transaction_id["transactionId"]:
                return detail
            # else:
            #     response = {
            #         "status": f"No transaction with ID: {transaction_id if type(transaction_id) == str else transaction_id['transactionId']} found, please try again..."
            #     }
            #     return response
    
    def get_transactions(self) -> list:
        if self.details == None:
            response = {
                "status": f"No transaction found, please try again..."
            }
            return response
        else:
            return self.details
    
    def set_transaction_details(self, transaction_id: str | dict, **kwargs: dict) -> dict:
        return super().set_transaction_details(transaction_id, **kwargs)
    
    def set_all_transactions_details(self, **kwargs: dict) -> list:
        return super().set_all_transactions_details(**kwargs)
    

data = {
            "transactionId": "16920947991155375524134000"
        }
D = DataTransactions()
print(D.get_transaction(data))

# T = DataTransactions()
# print(T.get_transaction("16920947991155375524134111"))
