from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(url=os.getenv("url"), headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Try different selectors for price
price_tag = soup.find("span", class_="a-price-whole")
if not price_tag:
    price_tag = soup.find("span", class_="a-offscreen")  # fallback

price = price_tag.get_text().strip()

# Remove commas, currency symbols
clean_price = price.replace(",", "").replace("₹", "").replace("$", "")
without_currency_price = float(clean_price)
print(without_currency_price)

# Get product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 12000

if without_currency_price < BUY_PRICE:
    message = f"{title} is on sale for {price}"

    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=os.getenv("my_mail"),
            password=os.getenv("password")
        )
        connection.sendmail(
            from_addr=os.getenv("my_mail"),
            to_addrs=os.getenv("my_mail"),
            msg=f"Subject: Price Drop Alert!\n\n{message}"
        )
