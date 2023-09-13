from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .utils import account_reference
from src.monnify_api import init, login_credential, token
from django.contrib.auth.decorators import login_required


# Create your views here.
"""
    This view function should be called from the registration view
"""
@login_required
@csrf_exempt
def get_reserved_accounts(request):
    if request.method == "POST":
        # # coming from admin table in DB
        customer_BVN = request.POST.get("customerBVN")
        bank_codes = request.POST.get("bankCodes")
        # coming from request params
        # coming from user table in DB
        if len(customer_BVN) != 11:
            response = {
                "status": f"Please input the correct BVN, {customer_BVN} is incomplete or over the limit of 11digits or is not a proper Bank Verification customer_BVN"
            }
            return JsonResponse(response, safe=False)
        else:
            reserved_accounts = init.reserve_account(token, login_credential, accountReference=account_reference(), accountName=f"{request.user.first_name} {request.user.last_name}", customerEmail=request.user.username, customerName=request.user.email, customerBvn=customer_BVN, availableBank=True)
            return JsonResponse(reserved_accounts, safe=False)
    else:
        response = {
            "status": f"Request method {request.method} is not POST"
        }
        return JsonResponse(response, safe=False)
    
@login_required
@csrf_exempt
def pay(request):
    pass