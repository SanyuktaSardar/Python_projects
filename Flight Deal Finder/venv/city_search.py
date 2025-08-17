import requests
from pprint import pprint
from dotenv import load_dotenv
import os
from flight_search import FlightSearch

load_dotenv()

class CitySearch(FlightSearch):
    def __init__(self):
        super().__init__()
        self.sheet_access()

    def sheet_access(self):
        SHEETY = os.getenv('SHEETY')
        HEADER = {
            "Authorization":os.getenv('TOKEN')
        }

        CITY_ENDPOINT = os.getenv("CITY_ENDPOINT")
        
        #get the sheet data
        response = requests.get(url=SHEETY,headers=HEADER)
        data = response.json()

        sheet_data =data['prices']
        pprint(sheet_data)

    # Check for IataCode

        for row in sheet_data:
            if row['iataCode']== "":
                body = row
                # city access
                parameter = {
                "keyword":body['city']
                }
                header = {
                    "Authorization": f"Bearer {self._token}"
                }
                response = requests.get(url = f"{CITY_ENDPOINT}/reference-data/locations/cities",params=parameter,headers=header)
                
                body['iataCode'] = response.json()['data'][0]['iataCode']
                id = body['id']
                del body['id']
                print(body)
                body = {
                "price":body
                }
                response = requests.put(url=f"{SHEETY}/{id}",json=body,headers=HEADER)
                response.raise_for_status()

c = CitySearch()



