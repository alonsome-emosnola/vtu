from datetime import datetime
import time
import requests
import os
from dotenv import load_dotenv
from text_generator import generate
from random import Random

rr = Random

load_dotenv()

VTPASS_API_KEY = os.getenv("VTPASS_API_KEY")
# VTPASS_PUBLIC_KEY = os.getenv("VTPASS_PUBLIC_KEY")
VTPASS_SECRET_KEY = os.getenv("VTPASS_SECRET_KEY")

SANDBOX_BASE_URL = os.getenv("SANDBOX_BASE_URL")
LIVE_BASE_URL = os.getenv("LIVE_BASE_URL")

POST_HEADERS = {
    "api-key": VTPASS_API_KEY,
    "secret-key": VTPASS_SECRET_KEY,
    "Authorization": f"Bearer {VTPASS_API_KEY}"
}

def requestID():
    now = datetime.now()
    current_clock = time.strftime("%H%M", time.localtime())
    return f"{now.strftime('%Y%m%d')}{current_clock}{generate(length_minimal=8, length_maximal=8)}"

def buy_airtime(service_ID, amount, number="08011111111"):
    parameters = {
        "request_id": requestID(),
        "serviceID": service_ID,
        "amount": amount,
        "phone": number
    }
    try:
        r = requests.post(f"{SANDBOX_BASE_URL}/pay", headers=POST_HEADERS, params=parameters)
        return parameters["request_id"]
    except Exception:
        print(Exception)


def check_airtime_purchase_status(request_ID):
    try:
        r = requests.post(f"{SANDBOX_BASE_URL}/requery", headers=POST_HEADERS, params={"request_id": request_ID})
        return r.json()
    except Exception:
        print(Exception)


def buy_data(service_ID, billers_code, variation_code, amount, number="08011111111"):
    parameters = {
        "request_id": requestID(),
        "serviceID": service_ID,
        "billersCode": billers_code,
        "variation_code": variation_code,
        "amount": amount,
        "phone": number
    }
    try:
        r = requests.post(f"{SANDBOX_BASE_URL}/pay", headers=POST_HEADERS, params=parameters)
        return parameters["request_id"]
    except Exception:
        print(Exception)


def check_data_purchase_status(request_ID):
    try:
        r = requests.post(f"{SANDBOX_BASE_URL}/requery", headers=POST_HEADERS, params={"request_id": request_ID})
        return r.json()
    except Exception:
        print(Exception)
        
# r = buy_airtime("mtn", 50)
# print(check_airtime_purchase_status(r))