import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
location = response.json()
print(location["iss_position"])