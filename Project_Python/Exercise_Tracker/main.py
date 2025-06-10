import requests
import os
from datetime import datetime


GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 171
AGE = 20

APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_exercise = input("Tell me which exercise you did: ")

parameters = {
    "query": user_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age":AGE,
}



response = requests.post(url=nutritionix_endpoint, json=parameters, headers=header)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
            "workout": {
                "date": today,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
    }

    # Sheety Authentication Option 1: No Auth
    # sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)

    # Sheety Authentication Option 2: Basic Auth

    # sheet_response = requests.post(
    #     url=sheety_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["ENV_SHEETY_USERNAME"],
    #         os.environ["ENV_SHEETY_PASSWORD"],
    #     )
    # )


    # Sheety Authentication Option 3: Bearer Token
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }

    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Sheety Response: \n {sheet_response.text}")








