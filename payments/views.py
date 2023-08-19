from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from src.monnify_api import get_customer_reserved_accounts

# Create your views here.
"""
    This view function should be called from the registration view
"""
@csrf_exempt
def get_reserved_accounts(request):
    if request.method == "POST":
        # # coming from admin table in DB
        customer_BVN = request.POST.get("customerBVN")
        bank_codes = request.POST.get("bankCodes")
        users = User.objects.all().values()
        # coming from request params
        # coming from user table in DB
        for user in users:
            customer_name = user["username"]
            customer_email = user["email"]
            if len(customer_BVN) != 11:
                response = {
                    "status": f"Please input the correct BVN, {customer_BVN} is incomplete or over the limit of 11digits or is not a proper Bank Verification customer_BVN"
                }
                return JsonResponse(response, safe=False)
            accs = get_customer_reserved_accounts(customer_name, customer_email, customer_BVN, bank_codes.split(","))
            return JsonResponse(accs, safe=False)
    else:
        response = {
            "status": f"Request method {request.method} is not POST"
        }
        return JsonResponse(response, safe=False)