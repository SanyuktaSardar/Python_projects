from flight_search import FlightSearch
import os
from dotenv import load_dotenv
from smtplib import SMTP
import requests

load_dotenv()

class Email(FlightSearch):
    def __init__(self):
        super().__init__()
        # ✅ store the email list
        self.user_emails = self.access_email()

    def access_email(self):
        USER_ENDPOINT = os.getenv('USER_ENDPOINT')
        AUTHORIZATION = os.getenv('TOKEN')
        headers = {"Authorization": AUTHORIZATION}

        response = requests.get(url=USER_ENDPOINT, headers=headers)
        response.raise_for_status()
        form_data = response.json()

        # get email list from Sheety "users" sheet
        return [email['whatIsYourEmail ?'] for email in form_data.get('users', [])]

    def send_mail(self, deal):
        my_mail = os.getenv('MY_MAIL')
        password = os.getenv('MAIL_PASSWORD')

        content = f"""
        Low price alert!
        Only {deal['price']} euro to fly from {deal['origin']} to {deal['destination']}
        Departure: {deal['start_date']}
        Return: {deal['end_date']}
        """

        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            for email in self.user_emails:
                connection.sendmail(
                    from_addr=my_mail,
                    to_addrs=email,
                    msg=f"Subject: Flight Deal Alert!\n\n{content}"
                )
                print(f"Email sent to {email}")
