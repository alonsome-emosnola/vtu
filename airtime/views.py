from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, response
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from src.vtpass_post import buy_airtime, check_airtime_purchase_status
from src.vtpass_get import get_balance, get_data_variation_codes
from src.wallet_api import WalletAPI
import json

pageTitle = "Smarttelweb | We offer instant recharge of Airtime, Databundle, CableTV (DStv, GOtv & Startimes), Electricity Bill Payment and more"

# Create your views here.

@csrf_exempt
def index(request):
    response = {
        "pageTitle": pageTitle,
    }
    return JsonResponse(get_balance(), safe=False)

@login_required
@csrf_exempt
def buy_airtime_for_self(request, serviceID):
    wallet = WalletAPI(request.user.username, request.user.email)
    bal = wallet.get_user_wallet_balance()
    if serviceID in ["mtn", "airtel", "glo", "etisalat"]:
        if request.method == "POST":
            amount = request.POST.get("amount")
            number = request.POST.get("number")
            if float(amount) >= bal or float(amount) < wallet.MINIMUM_BAL: # wallet balance
                return JsonResponse({"status": "Error, please check your wallet balance"}, safe=False)
            if len(number) != 11:
                return JsonResponse({"status": f"Phone number {number} is not upto 11 digits", "length_of_number": len(number)}, safe=False)
            if not number.startswith("0"):
                return JsonResponse({"status": f"Phone number {number} does not start with zero"}, safe=False)
            else:
                request_ID = buy_airtime(serviceID, amount, number=number)
                wallet.sub_user_wallet_balance(amount)
                # TODO update user wallet balance
                # TODO update user transaction history
                return redirect(f"check_status/?request-id={request_ID}")
        else:
            return JsonResponse({"status": "Error, request method is not POST"}, safe=False)
    else:
        return JsonResponse({"status": f"service ID {serviceID} not valid, try 'mtn, airtel, glo or etisalat'"}, safe=False)

@login_required
@csrf_exempt
def check_airtime_status(request, serviceID):
    requestID = request.GET.get("request-id")
    result = check_airtime_purchase_status(requestID)
    result["service_id"] = serviceID
    return JsonResponse(result, safe=False)

@login_required
def buy_for_others(request):
    return JsonResponse({"status": "Successful"}, safe=False)

