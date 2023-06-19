import requests
from datetime import datetime
import pytz
import hmac
import hashlib
import base64
import math
import random
from core.exceptions import BadRequestException, CustomException

API_KEY = 'c453012707bce21a9d086fd3b7a112dc'
SECRET_KEY = 'f8702b6eeb9bad0eac66788d2972893f'
MESSAGE = '{*code*} is your verification code.'
ENDPOINT = 'https://api.smsglobal.com/v2/otp'

def send_verify_code(phone: str) -> dict:
    # Define the endpoint and payload
    phone = ''.join(filter(str.isdigit, phone))
    payload = {
        'message': MESSAGE,
        'destination': phone
    }
    # Build the Authorization header
    ts = math.floor(datetime.timestamp(datetime.now(pytz.timezone('US/Central'))))
    #ts = math.floor(datetime.timestamp(datetime.now(pytz.utc)))
    # ts = math.floor(datetime.timestamp(datetime.now()))
    nonce = math.floor(random.random() * 10000000)      # check it
    uri='/v2/otp'
    port=443
    host='api.smsglobal.com'
    auth = f"{ts}\n{nonce}\nPOST\n{uri}\n{host}\n{port}\n\n"
    hash = hmac.new(
        SECRET_KEY.encode(),
        msg=auth.encode(),
        digestmod=hashlib.sha256
        ).digest ()
    hash = base64.b64encode (hash)
    hash = hash.decode("utf-8")
    token  = 'MAC id=\"%s\", ts=\"%s\", nonce=\"%s\", mac=\"%s\"' % (API_KEY, ts, nonce, hash)
    print(token)
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
    }
    print("start request")
    response = requests.post(
        ENDPOINT,
        headers=headers,
        json=payload,
    )
    print("Phone Verify Code Sent")
    if response == None:
        print ("BadREQUEST")
        raise BadRequestException
    print("response~~~~:", response.content)

    if response.status_code != 200:
        print('OTP failed to send. Response code:', response.status_code)
        print ("BadREQUEST")
        raise CustomException(code=response.status_code, message=response.content)
    return { 'token': token, 'request_id': response.json()['requestId'] }
    
def validate_code(id: str, code: str, token: str) -> int:
    code = ''.join(filter(str.isdigit, code))
    payload = {
        'code': code
    }
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    print("Start request")
    response = requests.post(
        ENDPOINT+'/requestid/'+id+'/validate',
        headers=headers,
        json=payload
    )
    print("Validate Code Sent")
    # Check the response
    if response == None:
        print ("BadREQUEST")
        raise BadRequestException
    print("response~~~~:", response.content)
    return response.status_code