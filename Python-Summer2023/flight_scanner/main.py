# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Twilio
# account_sid = 'ACc23aae11400aec9cd4c3fd31f176b547'
# auth_token = '7a7e1e5f89367d227530e6eb0cee4cdf'
import requests
from data_manager import DataManager
from flight_data import FlightData
from twilio.rest import Client
from flight_search import FlightSearch
from datetime import *
import smtplib

data_sheet = DataManager()
flight_data = FlightSearch(data_sheet.sheet_data)
new_data = flight_data.update_flight_data()
data_sheet.update_sheet(new_data)   












# header = {"apikey": "M-KY8bY4lZZGb5GcOnJRMDt-qCk-LICA"}
# param = {
#     "fly_from": "LON",
#     "fly_to": "PAR",
#     "date_from": "20/08/2023",
#     "date_to": "20/02/2024",
# }
# data_kiwi = requests.get(
#     url="https://api.tequila.kiwi.com/v2/search", headers=header,params=param
# ).json()
# kiwi_min_price = data_kiwi["data"][0]["price"]
# print(kiwi_min_price)
