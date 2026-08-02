import requests, base64
from datetime import datetime
from core.config import settings

def get_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET))
    return r.json()['access_token']

def stk_push(phone: str, amount: float, order_id: int):
    token = get_token()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    password = base64.b64encode((settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()).decode()
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE, "Password": password, "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline", "Amount": int(amount), "PartyA": phone,
        "PartyB": settings.MPESA_SHORTCODE, "PhoneNumber": phone,
        "CallBackURL": "https://yourdomain.com/api/payment/callback",
        "AccountReference": f"Order{order_id}", "TransactionDesc": "SupaShop Payment"
    }
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post("https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest", json=payload, headers=headers).json()
