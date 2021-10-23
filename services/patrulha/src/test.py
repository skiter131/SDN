import requests
import json

IP_ADRESS = "10.10.20.161"

request_data = {
    "username": "developer",
    "password": "C1sco12345"
}


req = requests.post(f'https://{IP_ADRESS}/api/v0/authenticate', headers={'authorization':\
'2j3k3o5p5i3p1p3oi', 'Content-Type': 'application/json',},\
    data=json.dumps(request_data), verify = False)

print(req.text)