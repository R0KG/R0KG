import requests


lat= 48.208176
lng= 16.373819
paramaeters = {
    "lat":lat,
    "lng":lng
}
response = requests.get("https://api.sunrise-sunset.org/json?lat=48.208176&lng=16.373819&formatted=1")
response.raise_for_status()
data = response.json()                                  
print(data) 