import os
from dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv('AMADEUS_SECRET')
        self._token = self._get_new_token()

    
    def _get_new_token(self):
        TOKEN_ENDPOINT  = os.getenv("TOKEN_ENDPOINT")
        body = {
            "grant_type":"client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(url = TOKEN_ENDPOINT,data=body,headers=headers)
        return response.json()['access_token']