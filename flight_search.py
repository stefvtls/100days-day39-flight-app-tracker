import requests
import datetime as dt
from dotenv import load_dotenv
import os


load_dotenv()


class FlightSearch:
    def __init__(self, flyfrom, flyto, adults, price_limit):
        self.kiwi_api = os.getenv("KIWI_API")
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.kiwi_headers = {"apikey": self.kiwi_api, "Content-Type": "application/json"}
        self.fly_from = flyfrom
        self.fly_to = flyto
        self.adults = adults
        self.price = price_limit
        self.date_from = dt.datetime.now()
        self.date_to = self.date_from + dt.timedelta(6*365/12)
        self.date_from = self.date_from.strftime("%d/%m/%Y")
        self.date_to = self.date_to.strftime("%d/%m/%Y")
        self.params = {
            "fly_to": self.fly_to,
            "fly_from": self.fly_from,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "adults": self.adults,
            "selected_cabins": "M",
            "curr": "EUR",
            "price_to": self.price,
            "max_stopovers": 0,
            "sort": "price",
            "asc": 1,
            "limit": 400,
            "flight_type": "oneway",
        }
        self.search_result = {}
        self.num = 0
        self.data = []

    def search_for_flights(self):
        response_kiwi = requests.get(url=self.kiwi_endpoint, params=self.params, headers=self.kiwi_headers)
        response_kiwi.raise_for_status()
        # print(self.response_kiwi.status_code)
        self.search_result = response_kiwi.json()["data"]
        self.num = len(self.search_result)
        # print(search_result)
        for times in range(0, self.num):
            price_ticket = self.search_result[times]['price']
            price_luggage = self.search_result[times]['bags_price']["1"]
            sum_price = int(price_ticket) + int(price_luggage)
            if self.search_result[times]["availability"]["seats"] != "null":
                if sum_price <= self.price:
                    self.data.append(self.search_result[times])
        if len(self.data) > 0:
            bonuses = ""
            for times in range(0, len(self.data)):
                bonuses += f"date: {self.data[times]['route'][0]['local_departure'].replace('T', ' ').replace(':00.000Z', '')}\n link: {self.data[times]['deep_link']}\n"
            mess = f"Special occasion! {len(self.data)} connections available from {self.fly_from} to {self.fly_to}\n" + bonuses
            return mess
        else:
            return ""



