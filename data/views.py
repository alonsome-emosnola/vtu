from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from src.vtpass_get import(get_data_variation_prices, get_service_categories, get_data_variation_codes)
from src.vtpass_post import(buy_data, check_data_purchase_status)


# Create your views here.
def home(request):
    return JsonResponse({"name": "Hello World"})

def data_prices(request):
    service_id = request.GET.get("serviceID", ["mtn-data", "airtel-data", "glo-data", "etisalat-data"])
    variations = get_data_variation_prices(service_id)
    varations = variations["content"]["varations"]
    variations_codes = [dictionary["variation_code"] for dictionary in varations]
    # names = [dictionary["name"] for dictionary in varations]
    # amts = [dictionary["variation_amount"] for dictionary in varations]
    # fixed_prices = [dictionary["fixedPrice"] for dictionary in varations]
    for variation_code in variations_codes:
        print(variation_code)
    # for name in names:
    #     print(name)
    # for amt in amts:
    #     print(amt)
    # for fixed_price in fixed_prices:
    #     print(fixed_price)
    return JsonResponse(varations, safe=False)

@csrf_exempt
def buy_data_for_self(request, serviceID):
    if request.method == "POST":
        billers_code = request.POST.get("billersCode")
        variation_code = request.POST.get("variationCode")
        amount = request.POST.get("amount")
        number = request.POST.get("number")
        try:
            variation_codes = get_data_variation_codes(serviceID)
        except TypeError as te:
            response = {
                "status": f"An error occured, please ensure you are connected to the internet"
            }
            return JsonResponse(response, safe=False)
        if serviceID not in ["mtn-data", "airtel-data", "glo-data", "etisalat-data"]:
            response = {
                "status": f"Please input the correct serviceID, {serviceID} is not valid"
            }
            return JsonResponse(response, safe=False)
        if len(billers_code) != 11 or not billers_code.startswith("0"):
            response = {
                "status": f"Please input the correct number, {billers_code} is incomplete or over the limit of 11digits or is not a proper phone number"
            }
            return JsonResponse(response, safe=False)
        if variation_code not in variation_codes:
            response = {
                "status": f"Variation code, {variation_code} is invalid"
            }
            return JsonResponse(response, safe=False)
        if int(amount) >= 1000 or int(amount) < 50: 
            # 1000 here means wallet balance
            response = {
                "status": f"Amount #{amount} is insufficient or below limit"
            }
            return JsonResponse(response, safe=False)
        if len(number) != 11 or not number.startswith("0"):
            response = {
                "status": f"Please input the correct number, {number} is incomplete or over the limit of 11digits or is not a proper phone number"
            }
            return JsonResponse(response, safe=False)
    else:
        response = {
            "status": f"Request method {request.method} is not POST"
        }
        return JsonResponse(response, safe=False)
    request_id = buy_data(serviceID, billers_code, variation_code, amount, number)
    return redirect(f"check_status/?requestID={request_id}")

def check_status(request, serviceID):
    request_id = request.GET.get("requestID")
    response = check_data_purchase_status(request_id)
    response["serviceID"] = serviceID
    return JsonResponse(response["content"], safe=False)
            
