from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest, QueryDict
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def buy_airtime_for_self(request, serviceID):
    if serviceID in ["mtn", "airtel", "glo", "etisalat"]:
        if request.method == "POST":
            amount = request.POST.get("amount")
            number = request.POST.get("number")
            if int(amount) >= 1000 or int(amount) < 50: # wallet balance
                return JsonResponse({"status": "Error, please check your wallet balance"}, safe=False)
            if len(number) != 11:
                return JsonResponse({"status": f"Phone number {number} is not upto 11 digits", "length_of_number": len(number)}, safe=False)
            if not number.startswith("0"):
                return JsonResponse({"status": f"Phone number {number} does not start with zero"}, safe=False)
            else:
                request_ID = buy_airtime(serviceID, amount, number=number)
                # TODO update user wallet balance
                # TODO update user transaction history
                return redirect(f"check_status/?request-id={request_ID}")
        else:
            return JsonResponse({"status": "Error, request method is not POST"}, safe=False)
    else:
        return JsonResponse({"status": f"service ID {serviceID} not valid, try 'mtn, airtel, glo or etisalat'"}, safe=False)

@csrf_exempt
def check_airtime_status(request, serviceID):
    requestID = request.GET.get("request-id")
    result = check_airtime_purchase_status(requestID)
    result["service_id"] = serviceID
    return JsonResponse(result, safe=False)

def buy_for_others(request):
    return JsonResponse("", safe=False)

