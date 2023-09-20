import requests
from datetime import datetime
import os

API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]
headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
    "x-remote-user-id" : "0"
}
params = {
 "query":input("Hey,write: ")
}

endpoint_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/7586ab1945046f235607d381a79bd598/myWorkouts/workouts"
response = requests.post(url= endpoint_API,json= params,headers=headers)
data_exercises = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
for data in data_exercises["exercises"]:
    sheet_data = {
        "workout" : {
            "date" : today_date,
            "time" : time,
            "exercise" : data["name"].title(),
            "duration" : data["duration_min"],
            "calories" : data["nf_calories"]
        }
    }
    sheety_r = requests.post(url= sheety_url,json= sheet_data,headers={"Authorization": "Bearer w2w12w12we12e12222222222e12e12e12e1e"})
    print(sheety_r)


