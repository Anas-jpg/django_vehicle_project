import requests
from requests.auth import HTTPBasicAuth

# Base URL configuration
BASE_URL = "http://127.0.0.1:8000/"  # Base URL of your API
ENDPOINT = "bikes/"  # Endpoint for the Bike model
URL = f"{BASE_URL}{ENDPOINT}"

# Authentication credentials
USERNAME = 'anas'  # Replace with your actual username
PASSWORD = 'roshni123'  # Replace with your actual password


# 1. POST Request - Add new Bike
def post_bike():
    data = {
        "brand": "Yamaha",
        "vehicle_type": "Bike",  # Ensure this matches the expected vehicle type
        "color": "GREEN",
        "year": 2012,
        "has_gear": True
    }

    try:
        response = requests.post(url=URL, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()  # Raise an error for bad status codes
        print("Bike created successfully!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during POST request:", err)
        print(f"Response: {response.text}")
    except Exception as err:
        print("An error occurred during POST request:", err)


# 2. GET Request - Retrieve data (all or by ID)
def get_bike(bike_id=None):
    try:
        if bike_id:  # Fetch specific Bike by ID
            response = requests.get(url=f"{URL}{bike_id}/", auth=HTTPBasicAuth(USERNAME, PASSWORD))
        else:  # Fetch all Bikes
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


# 3. PUT Request - Update existing Bike (complete update)
def update_bike(bike_id):
    data = {
        "brand": "Yamaha",
        "vehicle_type": "Bike",  # Ensure consistency with the model
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


# 4. DELETE Request - Delete a specific Bike by ID
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


# 5. PATCH Request - Partial Update (Optional)
def partial_update_bike(bike_id, partial_data):
    """
    Perform a partial update on a Bike instance.
    :param bike_id: ID of the Bike to update
    :param partial_data: Dictionary containing fields to update
    """
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


# 6. List Bikes with Pagination (Optional)
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


# 7. Create a Bike with Invalid Data (For Testing Validation)
def post_invalid_bike():
    data = {
        "brand": "",  # Empty brand to trigger validation error
        "vehicle_type": "Bike",
        "color": "PURPLE",  # Invalid color choice
        "year": 2026,  # Future year to trigger validation error
        "has_gear": "yes"  # Invalid boolean value
    }

    try:
        response = requests.post(url=URL, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
        response.raise_for_status()
        print("Bike created successfully!")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred during POST request with invalid data:", err)
        print(f"Response: {response.json()}")
    except Exception as err:
        print("An error occurred during POST request with invalid data:", err)


# Test the functions
if __name__ == "__main__":
    # Uncomment one function at a time to test the respective CRUD operation

    # 1. POST Request - Create a new Bike
    # post_bike()

# 2. GET Request - Retrieve all Bikes
# get_bike()

# 2. GET Request - Retrieve Bike by ID
# get_bike(bike_id=1)

# 3. PUT Request - Update an existing Bike (replace ID with the actual Bike ID)
# update_bike(bike_id=1)

# 4. DELETE Request - Delete a Bike (replace ID with the actual Bike ID)
 delete_bike(bike_id=3)

# 5. PATCH Request - Partially update a Bike (replace ID and data as needed)
# partial_update_bike(bike_id=1, partial_data={"color": "GREEN"})

# 6. List Bikes with Pagination (optional)
# list_bikes(page=1)

# 7. POST Request with Invalid Data - For testing validations
# post_invalid_bike()
