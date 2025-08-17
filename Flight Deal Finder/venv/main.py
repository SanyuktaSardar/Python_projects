from flight_search import FlightSearch
import datetime
import os
import requests
# from twilio.rest import Client
from sending_email import Email


class FlightOffer(FlightSearch):
    def __init__(self):
        super().__init__()
        self.time = datetime.datetime.now()
        self.endtime = self.time + datetime.timedelta(days=6 * 30)
        self.start_date = self.time.strftime('%Y-%m-%d')
        self.end_date = self.endtime.strftime('%Y-%m-%d')

    def cheap_flight(self):
        SHEETY = os.getenv('SHEETY')
        HEADER = {"Authorization": os.getenv('TOKEN')}
        OFFER_ENDPOINT = os.getenv("OFFER_ENDPOINT")

        # get the sheet data
        response = requests.get(url=SHEETY, headers=HEADER)
        response.raise_for_status()
        sheet_data = response.json().get('prices', [])

        for row in sheet_data:
            self.destination = row['iataCode']
            self.origin = 'CCU'
            self.adults = 1

            params = {
                "originLocationCode": self.origin,
                "destinationLocationCode": self.destination,
                "departureDate": self.start_date,
                "returnDate": self.end_date,
                "adults": self.adults,
            }
            headers = {"Authorization": f"Bearer {self._token}"}

            try:
                response = requests.get(
                    url=OFFER_ENDPOINT, params=params, headers=headers
                )
                response.raise_for_status()
                data = response.json().get('data', [])
            except Exception as e:
                print(f"Error fetching flights for {self.destination}: {e}")
                continue

            # Collect all prices
            price_list = [float(d['price']['grandTotal']) for d in data if 'price' in d]

            if not price_list:
                # No flights found, skip
                continue

            min_price = min(price_list)
            print(f"Cheapest flight {self.origin}->{self.destination}: {min_price} EUR")
            print(f"Stored lowest price: {row['lowestPrice']}")

            if min_price < float(row["lowestPrice"]):
                return {
                    "price": min_price,
                    "origin": self.origin,
                    "destination": self.destination,
                    "start_date": self.start_date,
                    "end_date": self.end_date,
                }

        return None


if __name__ == "__main__":
    flight_offer = FlightOffer()
    deal = flight_offer.cheap_flight()

    if deal:
        print("Cheaper flight found:", deal)
        email_manager = Email()
        email_manager.send_mail(deal)
    else:
        print("No new cheaper flights today.")
