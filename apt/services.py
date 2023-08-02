import requests
from django.conf import settings
import environ
env = environ.Env()
environ.Env.read_env()

def send_sms(user_name, number, date_time, flag):
    url = "https://www.fast2sms.com/dev/bulkV2"
    message_token = env('AUTH_TOKEN')
    authorization = message_token,
    if flag == 0:
        message = f" Hi {user_name} your appointment has been bookeed for {date_time} "
    else:
        message = f" Hi {user_name} this is the reaminder for your have scheduled appointment at {date_time} "
    querystring = {
    "authorization": authorization,
    "message": message,
    "language":"english",
    "route":"q",
    "numbers":number
    }
    headers = {
    'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(message)