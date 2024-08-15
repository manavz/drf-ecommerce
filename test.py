import requests

url = "http://localhost:8000/admin/accounts/signup/"

payload = {
    "email": "test@gmail.com",
    "first_name": "testFirsttname",
    "last_name": "testSurname",
    "role": "customer",
    "username": "testUsername",
}
files = []
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
