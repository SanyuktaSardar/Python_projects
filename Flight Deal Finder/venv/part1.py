import requests
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

SHEETY = os.getenv('SHEETY')
HEADER = {
    "Authorization":os.getenv('TOKEN')
}
#get the sheet data
response = requests.get(url=SHEETY,headers=HEADER)
data = response.json()

sheet_data =data['prices']
pprint(sheet_data)

# Check for IataCode

for row in sheet_data:
    if row['iataCode']== "TESTING":
        body = row
        body['iataCode'] = ''
        id = body['id']
        del body['id']
        print(body)
        body = {
        "price":body
        }
        response = requests.put(url=f"{SHEETY}/{id}",json=body,headers=HEADER)
        response.raise_for_status()



