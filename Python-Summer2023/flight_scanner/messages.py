import requests
from twilio.rest import Client

class Messager:
    def __init__(self):
        self.client = Client("ACc23aae11400aec9cd4c3fd31f176b547","7a7e1e5f89367d227530e6eb0cee4cdf")
    def send_message(self,message):
        message = self.client.messages.create(
            body= message,
            from_='+13138804337',
            to='+436601337153'
        )
        print(message.sid)