import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from text_generator import generate
from random import Random

rr = Random

load_dotenv()

VTPASS_API_KEY = os.getenv("VTPASS_API_KEY")
VTPASS_PUBLIC_KEY = os.getenv("VTPASS_PUBLIC_KEY")
# VTPASS_SECRET_KEY = os.getenv("VTPASS_SECRET_KEY")

SANDBOX_BASE_URL = os.getenv("SANDBOX_BASE_URL")
LIVE_BASE_URL = os.getenv("LIVE_BASE_URL")

GET_HEADERS = {
    "api-key": VTPASS_API_KEY,
    "public-key": VTPASS_PUBLIC_KEY,
    "Authorization": f"Bearer {VTPASS_API_KEY}"
}


def get_balance():
    try:
        r = requests.get(f"{SANDBOX_BASE_URL}/balance", headers=GET_HEADERS)
        r = r.json()
        return r["contents"]["balance"]
    except Exception:
        print(Exception)


def get_service_categories():
    try:
        r = requests.get(f"{SANDBOX_BASE_URL}/service-categories", headers=GET_HEADERS)
        return r
    except Exception:
        print(Exception)


def get_by_service_id(id):
    try:
        r = requests.get(f"{SANDBOX_BASE_URL}/services?identifier={id}", headers=GET_HEADERS)
        return r
    except Exception:
        print(Exception)


# Data API

def get_data_variation_prices(service_id):
    try:
        r = requests.get(f"{SANDBOX_BASE_URL}/service-variations?serviceID={service_id}", headers=GET_HEADERS)
        return r.json()
    except Exception:
        print(Exception)
        
def get_data_variation_codes(service_id):
    try:
        r = requests.get(f"{SANDBOX_BASE_URL}/service-variations?serviceID={service_id}", headers=GET_HEADERS)
        res = r.json()
        varations = res["content"]["varations"]
        variations_codes = [dictionary["variation_code"] for dictionary in varations]
        return variations_codes
    except Exception:
        print(Exception)