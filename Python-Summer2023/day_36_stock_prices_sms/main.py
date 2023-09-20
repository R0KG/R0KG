STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCK_PRICES = "LCGXPTYGMOIPB3UR"
API_KEY_NEWS = "51c538c30dc04107ad2b40c082402386"
#7u0p9fewrasTeph2@?-3
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

#########################  STEP 1
import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_KEY_STOCK_PRICES}'
response = requests.get(url)
data = response.json()["Time Series (Daily)"]
close_prices = [entry["4. close"] for date, entry in list(data.items())[:2]]
procent_difference = (float(close_prices[0]) - float(close_prices[1]))
procent_difference = round(procent_difference/float(close_prices[1])* 100,3)

# print(procent_difference)
# print(close_prices)

#########################  STEP 2
url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={API_KEY_NEWS}"
response = requests.get(url) 
data = response.json()["articles"]
last_news = data[:3]
keys_to_extract = ["author","description"]
filtered_list = [{key: entry[key] for key in keys_to_extract} for entry in last_news]


# #########################  STEP 3
account_sid = 'ACc23aae11400aec9cd4c3fd31f176b547'
auth_token = '7a7e1e5f89367d227530e6eb0cee4cdf'
from twilio.rest import Client

account_sid = 'ACc23aae11400aec9cd4c3fd31f176b547'
auth_token = '7a7e1e5f89367d227530e6eb0cee4cdf'
client = Client(account_sid, auth_token)
for text in filtered_list:
    author = text.get('author', 'Unknown Author')
    description = text.get('description', 'No Title')
    message = client.messages.create(
    from_='+13138804337',
    body=f"\nTSLA ▼{procent_difference}\nAuthor: {author}\nDescription:{description}",
    to='+436601337153'
    )





# print(message.status)

