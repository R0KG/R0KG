from twilio.rest import Client
from datetime import *
import flight_data
import requests
from messages import Messager


header = {"apikey" : "M-KY8bY4lZZGb5GcOnJRMDt-qCk-LICA"}

class FlightSearch:
    messager = Messager()
    FLIGHT_FROM = "LON"
    temp_from = datetime.now().date()
    temp_to = temp_from  + timedelta(days= 182)
    data_from = temp_from.strftime("%d/%m/%Y")
    data_to = temp_to.strftime("%d/%m/%Y")
    def __init__(self,data_sheet):
        self.data_sheet = data_sheet
        self.lowest_price = data_sheet["tabellenblatt1"][0]["lowestPrice"]
        for price in data_sheet["tabellenblatt1"]:
            if self.lowest_price > price["lowestPrice"]:
                self.lowest_price = price["lowestPrice"]
                
    
    def search_lowest_price(self):
        min_price = self.data_sheet["tabellenblatt1"][0]["lowestPrice"]
        for flight in self.data_sheet["tabellenblatt1"]:
            if flight["lowestPrice"] < min_price:
                min_price = flight
        return min_price
    
    def update_flight_data(self):
        for flight in self.data_sheet["tabellenblatt1"]:
            fly_to = flight["iataCode"]
            new_flight = flight_data.FlightData(self.FLIGHT_FROM,fly_to,self.data_from,self.data_to,flight["lowestPrice"])
            param = {
                "fly_from" : new_flight.fly_from,
                "fly_to" : new_flight.fly_to,
                "date_from" : new_flight.date_from,
                "date_to" : new_flight.date_to
            }
            query = {
            "fly_from": new_flight.fly_from,
            "fly_to": new_flight.fly_to,
            "date_from": new_flight.date_from,
            "date_to": new_flight.date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
            data_kiwi = requests.get(url= "https://api.tequila.kiwi.com/v2/search",headers= header,params=query).json()
            kiwi_min_price = data_kiwi["data"][0]["price"]
            new_flight.out_date=data_kiwi["data"][0]["route"][0]["local_departure"].split("T")[0],
            new_flight.return_date=data_kiwi["data"][0]["route"][1]["local_departure"].split("T")[0]
            if kiwi_min_price < flight["lowestPrice"]:
                flight["lowestPrice"] = kiwi_min_price
                new_flight.price = kiwi_min_price
                self.messager.send_message(str(new_flight))
            print(new_flight)
        self.lowest_price = self.search_lowest_price()
        
        return self.data_sheet
        