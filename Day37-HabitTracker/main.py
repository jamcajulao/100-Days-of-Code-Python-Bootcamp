import requests
from datetime import datetime

# |--------------------- SETUP USER ACCOUNT ---------------------|
USERNAME = input("Username: ")
TOKEN = input("Token: ")

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": input("Agree on Terms of Service (yes/no): "),
    "notMinor": input("Not a minor (yes/no): "),
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# |--------------------- CREATE GRAPH ---------------------|

GRAPH_ID = input("Graph ID: ")
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": input("Graph Name: "),
    "unit": input("Unit: "),
    "type": "float",
    "color": "shibafu",
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
print(response.text)

# |--------------------- POST A PIXEL ---------------------|
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now().strftime("%Y%m%d")
pixel_params = {
    "date": today,
    "quantity": input("Quantity: "),
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=HEADERS)
print(response.text)

# |--------------------- UPDATE A PIXEL ---------------------|
update_date = input("Date (yyyyMMdd): ")
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{update_date}"
update_pixel_parameters = {
    "quantity": input("Updated Quantity: "),
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=HEADERS)
print(response.text)

# |--------------------- DELETE A PIXEL ---------------------|
delete_date = input("Date (yyyyMMdd): ")
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{delete_date}"

response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
print(response.text)
