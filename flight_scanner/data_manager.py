import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = requests.get("https://api.sheety.co/7586ab1945046f235607d381a79bd598/flightScanner/tabellenblatt1").json()
        header = {"apikey" : "M-KY8bY4lZZGb5GcOnJRMDt-qCk-LICA"}
        print(self.sheet_data)
        
    def update_sheet(self,data_sheet):
        for index in range(2,11):
            param = {
                "tabellenblatt1" : {
                    "city" : data_sheet["tabellenblatt1"][index-2]["city"],
                    "iataCode" : data_sheet["tabellenblatt1"][index-2]["iataCode"],
                    "lowestPrice" : data_sheet["tabellenblatt1"][index-2]["lowestPrice"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/7586ab1945046f235607d381a79bd598/flightScanner/tabellenblatt1/{index}",json=param)
            
