import requests
from setup import SetupInterface

setup = SetupInterface()

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": setup.selected_category,
    "difficulty": setup.selected_difficulty,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]

