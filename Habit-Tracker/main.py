import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "SID"
auth_token = "TOKEN"
appid =  "API KEY"

lat = 22.673380
long = 88.327469
#number = +14148773680


parameter = {
    "lat" :lat,
    "lon":long,
    "appid":appid,
    "cnt":4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)

data = response.json()

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https':os.environ['https_proxy']}

    client = Client(account_sid, auth_token,http_client=proxy_client)

    message = client.messages.create(
        body="It's going to rain today.Remember to bring an umbrella🌂.",
        from_="whatsapp:NUMBER",
        to="whatsapp:your NUMBER",
    )
    print(message.status)
