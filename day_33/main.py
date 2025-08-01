import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

json_file = response.json()
print(json_file)

satellite_latitude = json_file['iss_position']['latitude']
satellite_longitude = json_file['iss_position']['longitude']

print(satellite_latitude,satellite_longitude)