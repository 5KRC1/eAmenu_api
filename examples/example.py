import requests

headers = {
        "username": "",
        "password": "",

        "disliked_foods": [],
        "preferred_menu": "",

        "favourite_foods": [],
        "default_menu": ""
        }

response = requests.post(url="localhost:5000/api/service", headers=headers)
print(response)
