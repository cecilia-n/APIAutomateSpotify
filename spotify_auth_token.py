import requests
import json

"""
Searched Up How to access spotify Web API with Secret and client_id (Stack Overflow)
"""

CLIENT_ID = "0deb4ced4e56411dbd7b02f98be8a2e4"
CLIENT_SECRET = "786bfd1359074105a6609253c13900dc"

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

token_raw = json.loads(response.text)
token = token_raw["access_token"]

#Request with Endpoint a string type
def request_endpoint(endpoint_id):
    if isinstance(endpoint_id, str):
        headers = {"Authorization": "Bearer {}".format(token)}
        r = requests.get(url=f"https://api.spotify.com/v1/albums/{endpoint_id}", headers=headers)
        return print(r.text)
    else:
        return print(f"Please Change endpoint url")

request_endpoint('4aawyAB9vmqN3uQ7FjRGTy')