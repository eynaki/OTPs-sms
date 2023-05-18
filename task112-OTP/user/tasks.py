import requests

from celery import shared_task
from celery import Celery

from random import randint
from redis import Redis

from otp.settings import API_KEY


con = Redis(host="localhost", port=6379, db=0, charset="utf-8", decode_responses=True)
app = Celery("tasks", broker="redis://localhost:6379")

@shared_task
def send_sms(phone_number):
    
    rand = str(randint(100000, 999999))
    con.set(phone_number, rand, ex=90)
    
    url = "https://api.sms.ir/v1/send/verify/"
        
    data = {
        "mobile": phone_number,
        "templateId": 100000,
        "parameters": [
            {
                "name": "Code",
                "value": rand
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "text/plain",
        "x-api-key": API_KEY
    }
    
    print(rand)
    requests.post(url, json=data, headers=headers)