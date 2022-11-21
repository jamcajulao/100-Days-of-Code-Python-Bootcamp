# Workout Tracker
"""A workout tracker that asks the user what exercises they did for the day.
 The user can type their exercises using natural language and the programs
 logs the date, time, exercise, duration and calories into a Google Sheet"""

import requests
from datetime import datetime

# |----------------------------- SETUP -----------------------------|

# API KEYS
# Nutritionix - register for a free account on https://www.nutritionix.com to get your API ID and Keys
NUTRITIONIX_ID = "YOUR_ID"
NUTRITIONIX_KEY = "YOUR_KEY"

# Sheets - connect your google sheet file and create a project in https://sheety.co to get your authorization and links
SHEETS_PROJECT = "<YOUR_USERID>/<PROJECT_NAME>/<SHEET_NAME>"
SHEETS_TOKEN = "YOUR_TOKEN"

# input your personal details
GENDER = "YOUR_GENDER"
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0

# |----------------------------- CONVERT INPUT TO DATA  -----------------------------|
exercise_log = input("Tell me which exercises you did today: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
}
nutritionix_parameters = {
    "query": exercise_log,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(nutritionix_endpoint, json=nutritionix_parameters, headers=nutritionix_headers)
exercise_stats = response.json()["exercises"]

# |----------------------------- POST IN GOOGLE SHEETS -----------------------------|
date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

for item in exercise_stats:

    sheets_endpoint = f"https://api.sheety.co/{SHEETS_PROJECT}"
    sheets_parameters = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    sheets_header = {
        "Authorization": SHEETS_TOKEN,
    }

    response = requests.post(sheets_endpoint, json=sheets_parameters, headers=sheets_header)
    print(response.text)
