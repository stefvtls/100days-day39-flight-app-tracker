from dotenv import load_dotenv
import os
from data_manager import DataManager
import datetime as dt
from flight_search import FlightSearch
import requests
from notification_manager import NotificationManager

load_dotenv()
flyfrom = "LON"
adults = 1


get_destinations = DataManager()
destination_dictionary = {}
if len(destination_dictionary) == 0:
    destination_dictionary = get_destinations.get_prices()
# full_message = ""
# print(destination_dictionary)
for key, value in destination_dictionary.items():
    search_engine = FlightSearch(flyfrom=flyfrom, flyto=key, adults=adults, price_limit=value)
    message = search_engine.search_for_flights()
    if len(message) > 10:
        telegram_bot = NotificationManager(message)
        telegram_bot.send_text()
        print(message)
    # full_message += q
# print(full_message)
# telegram_bot = NotificationManager(full_message)
# telegram_bot.send_text()

