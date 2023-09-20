import requests

USERNAME = "romanj"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token" : "jqpeqxxpzszoqwal",
    "username": "romanj",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
headers = {
    "X-USER-TOKEN" :"jqpeqxxpzszoqwal"
}
# graph_config = {
#     "id" : "graph1",
#     "name": "reading tracker",
# 	"unit": "pages",
#     "type": "int",
#     "color" : "sora"
# }
graph_config = {
    "date" : "20230815",
    "quantity": "10"
}
graph_endpoint = f"https://pixe.la/v1/users/romanj"

response = requests.delete(url=graph_endpoint,headers=headers)
print(response.text)
# response = requests.post(url= pixela_endpoint,json= parameters)
# print(response.text)