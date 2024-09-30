import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "bikes/"
URL = f"{BASE_URL}{ENDPOINT}"

# Authentication credentials
USERNAME = 'anas'
PASSWORD = 'roshni123'


def post_bike():
    data = {
        "brand": "Kawasaki",
        "vehicle_type": "Bike",
        "color": "GREEN",
        "year": 2018,
        "has_gear": True
    }

    try:
        response = requests.post(url=URL, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()
        print("Bike created successfully!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during POST request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during POST request:", err)


def get_bike(bike_id=None):
    try:
        if bike_id:
            response = requests.get(url=f"{URL}{bike_id}/", auth=HTTPBasicAuth(USERNAME, PASSWORD))
        else:
            response = requests.get(url=URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

        response.raise_for_status()
        print("GET request successful!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during GET request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during GET request:", err)


def update_bike(bike_id):
    data = {
        "brand": "Yamaha",
        "vehicle_type": "Bike",
        "color": "BLUE",
        "year": 2020,
        "has_gear": False
    }

    try:
        response = requests.put(url=f"{URL}{bike_id}/", json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()
        print("Bike updated successfully!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during PUT request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during PUT request:", err)


def delete_bike(bike_id):
    try:
        response = requests.delete(url=f"{URL}{bike_id}/", auth=HTTPBasicAuth(USERNAME, PASSWORD))
        if response.status_code == 204:
            print("Bike deleted successfully.")
        else:
            print(f"Failed to delete Bike. Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during DELETE request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during DELETE request:", err)


def partial_update_bike(bike_id, partial_data):
    try:
        response = requests.patch(url=f"{URL}{bike_id}/", json=partial_data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()
        print("Bike partially updated successfully!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during PATCH request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during PATCH request:", err)


def list_bikes(page=1):
    try:
        response = requests.get(url=f"{URL}?page={page}", auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()
        print(f"Bikes on page {page}:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during list request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during list request:", err)


# post_bike()
# get_bike()
# get_bike(bike_id=1)
# update_bike(bike_id=1)
delete_bike(bike_id=7)
# partial_update_bike(bike_id=1, partial_data={"color": "GREEN"})
