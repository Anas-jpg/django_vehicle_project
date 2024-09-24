import requests
from requests.auth import HTTPBasicAuth

URL = "http://127.0.0.1:8000/cars/"  # Ensure the correct endpoint
USERNAME = 'admin'
PASSWORD = 'admin'


# 1. POST Request - Add new data
def post_data():
    data = {
        "brand": "Toyota",
        "vehicle_type": "Car",
        "color": "RED",
        "year": 2019,
        "num_doors": 4

    }

    response = requests.post(url=URL, json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


# 2. GET Request - Retrieve data (all or by ID)
def get_data(id=None):
    if id:  # Fetch specific record by ID
        response = requests.get(url=f"{URL}{id}/", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    else:  # Fetch all records
        response = requests.get(url=URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))

    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print(f"Raw Response: {response.text}")


# 3. PUT Request - Update data (complete update for a specific record by ID)
def update_data(id):
    data = {
        'name': 'Updated Name',
        'roll': 15,
        'city': 'Updated City'
    }

    response = requests.put(url=f"{URL}{id}/", json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


# 4. DELETE Request - Delete a specific record by ID
def delete_data(id):
    response = requests.delete(url=f"{URL}{id}/", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print(f"Status Code: {response.status_code}")
    if response.status_code == 204:
        print("Record deleted successfully.")
    else:
        print(f"Response: {response.json()}")


# Test the functions

# Uncomment one function at a time to test the respective CRUD operation

# 1. POST Request - Create a new student
# post_data()

# 2. GET Request - Retrieve all students
# get_data()

# 2. GET Request - Retrieve student by ID
# get_data(id=1)

# 3. PUT Request - Update an existing student (replace ID with the actual record ID)
# update_data(id=1)

# 4. DELETE Request - Delete a student (replace ID with the actual record ID)
delete_data(id=1)
