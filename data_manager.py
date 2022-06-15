import requests
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    def __init__(self):
        self.SHEETY_API = os.getenv("SHEETY_API")
        self.SHEETY_USER = os.getenv("SHEETY_USER")
        self.SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
        self.data_to_parse = {}

    def get_prices(self):
        response = requests.get(url=self.SHEETY_API, auth=(self.SHEETY_USER, self.SHEETY_PASSWORD))
        response.raise_for_status()
        print(response.status_code)
        data = response.json()['prices']
        # print(data)
        for row in data:
            self.data_to_parse[row['iataCode']] = row['lowestPrice']
        return self.data_to_parse


