import requests
from datetime import datetime
import os

os.environ['APPLICATION_ID'] = "950ace28"
os.environ["APP_KEY"] = "3723fe0e72788c38c2282e3f87338976"
os.environ["APP_ENDPOINT" ]= "https://trackapi.nutritionix.com//v2/natural/exercise"

#SHEETY API
os.environ['SHEETY_ENDPOINT'] = "https://api.sheety.co/95a22f2644d79067a976fd7bafc58c88/myWorkouts/workouts"
os.environ['TOKEN'] = "c2FueXVrdGE6c2FuanUxMzI="
#TODO: FIGURE OUT HOW TO PRINT EXERCISE STATS FOR PLAIN TEXT INPUT
#EXERCISE API
APPLICATION_ID = os.environ.get('APPLICATION_ID')
APP_KEY = os.environ.get('APP_KEY')
APP_ENDPOINT = os.environ.get('APP_ENDPOINT')

#SHEETY API
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
TOKEN = os.environ.get('TOKEN')
print(APP_ENDPOINT)
today = datetime.now()
date_time = today.strftime("%d/%m/%Y %H:%M:%S")
date=date_time.split()[0]
time = date_time.split()[1]

user_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id":APPLICATION_ID,
    "x-app-key":APP_KEY,
}
params = {
    "query": user_input,
}
response = requests.post(url=APP_ENDPOINT,json=params,headers=headers)

data = response.json()
exercise_list = [{'date':date,
                  'time':time,
                  "exercise":exercise['name'].title(),
                  "duration":exercise['duration_min'],
                  "calories":exercise['nf_calories']
                  } for exercise in data['exercises']]
# print(exercise_list)

# TODO: Sheety Api Access and post 

header = {
    "Content-Type":"application/json",
    "Authorization":f"Basic {TOKEN}",
}

for exercise in exercise_list:
    body = {"workout":exercise}
    response = requests.post(SHEETY_ENDPOINT,json=body,headers=header)
    print(response.raise_for_status())
    # print(response.json())

# {'date': '21/07/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}