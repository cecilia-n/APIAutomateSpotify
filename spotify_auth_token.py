import requests
import json

"""
Searched Up How to Access Spotify Web API 
with Secret and client_id in Python (Stack Overflow)

Note: Need to request after an hour, access token EXPIRES

Note Difficulty: - Why with Find Current User Profile, did not get access (OAuth Authentication requires 
                                                                        User to Authorize in Redirected Site, 
                                                                        Easier to use Flask API to handle oAuth user authentication and Redirect OR 
                                                                        spotipy, simpler and more user-friendly
)
            - For Find User profile, used default 'smedjan' or 'Cecilian' (Spotify Dev Account User)

"""
#(Can Alter)
CLIENT_ID = "7c358b65bcc84e51a377bf171634ad88"
CLIENT_SECRET = "7c64c533a4a14d509dbfa129fed28fac"
redirect_uri = "https:://localhost::3000"

def get_client_token(CLIENT_ID, CLIENT_SECRET):
    """
    Returns Authorization Token Requested
    """
    body_params = {'grant_type' : 'client_credentials'}
    url='https://accounts.spotify.com/api/token'
    #ERROR: No inclusion of client_id or client_secret, and post request needed!!!!

    response = requests.post(url, data = body_params,auth=(CLIENT_ID, CLIENT_SECRET)) 
    token_raw = response.json()
    return  token_raw['access_token']

def request_endpoint(endpoint, token):
    if isinstance(endpoint, str):
        header = {"Authorization": "Bearer {}".format(token)}
        response = requests.get(url=endpoint, headers=header)
        return print(response.json())
    else:
        return print(f"Please Change Endpoint url")

""""
Unit Tests
"""

token = get_client_token(CLIENT_ID,CLIENT_SECRET)
print(token)

#Get Specific Spotify Album
endpoint = "https://api.spotify.com/v1/albums/4aawyAB9vmqN3uQ7FjRGTy"

#Get User's Profile
user_id = '68y8qskwax1b3bywp8brdxwih' #Personal Spotify User ID
endpoint_user = f"https://api.spotify.com/v1/users/{user_id}/playlists"
request_endpoint(endpoint_user, token)