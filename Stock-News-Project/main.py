import requests
import random
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

parameter = {
                "function": "TIME_SERIES_DAILY",
                "symbol" : STOCK,
                "apikey":"Your API key"
            }

r = requests.get(url=STOCK_ENDPOINT,params=parameter)
data = r.json()
# print(data['Time Series (Daily)'])

dates = list(data['Time Series (Daily)'].keys())
# print(dates)

today_date = dates[0]
today_stocks_open = float(data['Time Series (Daily)'][today_date]['4. close'])
# print(today_stocks_open)

yesterday = dates[1]
yesterday_stock_close = float(data['Time Series (Daily)'][today_date]['4. close'])
# print(yesterday_stock_close)

profit = ((today_stocks_open - yesterday_stock_close)/yesterday_stock_close)*100
print(profit)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if profit >= 5:
    par = {"q":COMPANY_NAME,
                "apikey":"your api key"}
    news = requests.get(NEWS_ENDPOINT,params=par)
    news_data = news.json()

    first_4_title = [news_data['articles'][i]['title'] for i in range(4)]
    # print(first_4_title)

    first_4_description = [news_data['articles'][i]['description'] for i in range(4)]
    # print(first_4_description)
    first_4_content = [news_data['articles'][i]['content'].split(". ")[0] for i in range(4)]
    choice = random.randint(0,3)

    if profit < 0:
        sticker = "🔽"
    else:
        sticker = "🔼"
    message = f'''
    TSLA: {sticker} {abs(round(profit))}
    Headline: {first_4_title[choice]}
    Brief : {first_4_description[choice]}
    '''
    print(message)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.

    # Download the helper library from https://www.twilio.com/docs/python/install


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "twillio sid"
    auth_token = "your token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_="your send from number",
        to="Your number",
    )
    print(message.status)


    #Optional: Format the SMS message like this: 
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

