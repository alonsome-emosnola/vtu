# import requests

# stop = True
# r = requests.post("https://monnify-webhook.onrender.com/monnify-transactions")
# print(r.json())
# r = requests.get("https://monnify-webhook.onrender.com/get-monnify-transactions/0")
# data = r.json()
# details = {
#     "status": data["eventType"],
#     "amount": data["eventData"]["amountPaid"],
#     "customer_name": data["eventData"]["customer"]["name"],
#     "customer_email": data["eventData"]["customer"]["email"]
# }

# while stop:
#     if r.json()["bal"] >= 5000:
#        stop = False
#     else:
#         continue
