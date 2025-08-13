import requests
from datetime import datetime
import os

#TODO: FIGURE OUT HOW TO PRINT EXERCISE STATS FOR PLAIN TEXT INPUT
#EXERCISE API
APPLICATION_ID = "950ace28"
APP_KEY = "3723fe0e72788c38c2282e3f87338976"
APP_ENDPOINT = "https://trackapi.nutritionix.com//v2/natural/exercise"

#SHEETY API
SHEETY_ENDPOINT = "https://api.sheety.co/95a22f2644d79067a976fd7bafc58c88/myWorkouts/workouts"
TOKEN = "c2FueXVrdGE6c2FuanUxMzI="

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