import requests
from datetime import datetime



USERNAME = "violet1"
TOKEN = "ultrasonic"
GRAPH_ID = "graph1"
header = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)


update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

put_data = {
    "quantity": "20.10",
}

# response = requests.put(url=update_endpoint, json=put_data, headers=header)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)