import base64
import requests
import os
from dotenv import load_dotenv

def getAuthToken():
    load_dotenv()

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    # base64 encodinng to communicate CLIENT_ID and CLIENT_SECRET to Spotify API for authorization
    AUTH_STRING_BYTES = (CLIENT_ID + ":" + CLIENT_SECRET).encode("ascii")
    B64_AUTH_BYTES = base64.b64encode(AUTH_STRING_BYTES)
    B64_AUTH_STRING = B64_AUTH_BYTES.decode("ascii")

    # Spotify API endpoint
    TOKEN_URL = "https://accounts.spotify.com/api/token"

    # establish headers to send to spotify api to request access token
    auth_headers = {"Authorization": "Basic " + B64_AUTH_STRING}
    # establish data to send to spotify api to request access token
    auth_data = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }
    # use POST method to send post request to spotify API to request access token
    res = requests.post(TOKEN_URL, headers=auth_headers, data=auth_data)
    # store json of response in res_data so that response body is accessible
    res_data = res.json()
    # store 'access_token' from response body in variable access_token
    access_token = res_data.get("access_token")

    return access_token
