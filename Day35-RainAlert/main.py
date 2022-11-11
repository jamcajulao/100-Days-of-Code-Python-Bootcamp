# RAIN ALERT SMS/TELEGRAM
"""Checks the weather forecast for the day if it is going to rain
and sends an SMS or a Telegram chat to bring an umbrella"""

import requests
from twilio.rest import Client

# ------------------- SETUP -------------------

# get your city's latitude and longitude at https://www.latlong.net
MY_LAT = 0
MY_LONG = 0

# API KEYS
# OpenWeatherMap - register for a free account on https://openweathermap.org to get your API Key
OWM_API_KEY = ""
# Twilio - register for a trial account on https://www.twilio.com to get your trial ID, Token, and phone number
TWILIO_ACCOUNT_ID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
OWN_PHONE_NUMBER = ""
# TelegramBot - create a free bot on telegram using @BotFather to get Token and chatID
TG_BOT_TOKEN = ""
TG_BOT_CHATID = ""


# ------------------- REQUEST WEATHER DATA -------------------
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
OWM_PARAMS = {
    "lat": 3.1569,
    "lon": 101.7123,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=OWM_URL, params=OWM_PARAMS)
response.raise_for_status()
data = response.json()

# ------------------- CHECK FOR RAIN -------------------
will_rain = False
for num in range(0, 12):
    if data["hourly"][num]["weather"][0]["id"] < 700:
        will_rain = True

RAIN_ALERT = "It's going to 🌧 today. Remember to bring an ☂️."
if will_rain:

    # OPTION 1: Send an SMS to your mobile phone number
    client = Client(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(body=RAIN_ALERT,
                from_=TWILIO_PHONE_NUMBER,
                to=OWN_PHONE_NUMBER
                )
    print(message.status)

    # OPTION 2: Send a chat to your bot account in Telegram
    url = f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage?chat_id={TG_BOT_CHATID}&text={RAIN_ALERT}"
    print(requests.get(url).json())
