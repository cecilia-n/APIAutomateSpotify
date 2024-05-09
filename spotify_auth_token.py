import requests
import json

"""
Searched Up How to Access Spotify Web API 
with Secret and client_id in Python (Stack Overflow)
"""
#Get Token
CLIENT_ID = "0deb4ced4e56411dbd7b02f98be8a2e4"
CLIENT_SECRET = "786bfd1359074105a6609253c13900dc"

def get_client_token(CLIENT_ID, CLIENT_SECRET):
    grant_type = 'client_credentials'
    body_params = {'grant_type' : grant_type}

    url='https://accounts.spotify.com/api/token'
    response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

    token_raw = json.loads(response.text)
    token = token_raw["access_token"]
    
    return  token #tuple

#Request with Endpoint a string type
def request_endpoint(endpoint_id, token):
    if isinstance(endpoint_id, str):
        headers = {"Authorization": "Bearer {}".format(token)}
        r = requests.get(url=f"https://api.spotify.com/v1/albums/{endpoint_id}", headers=headers)
        return print(r.text)
    else:
        return print(f"Please Change Endpoint url")

""""
Unit Tests
"""
##Get Specific Spotify Album
# token = get_client_token(CLIENT_ID,CLIENT_SECRET)
# request_endpoint('4aawyAB9vmqN3uQ7FjRGTy', token)