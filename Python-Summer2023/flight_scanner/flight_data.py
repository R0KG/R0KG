from data_manager import DataManager
import requests
import datetime

class FlightData:
    header = {"apikey" : "M-KY8bY4lZZGb5GcOnJRMDt-qCk-LICA"}
    out_date=""
    return_date= ""
    def __init__(self,fly_from,fly_to,date_from,date_to,price):
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.price = price
        
    def __str__(self):
        return f"Flight from {self.fly_from} to {self.fly_to}. Date from {self.out_date}, date to {self.return_date}.Price is {self.price}€"
    
        