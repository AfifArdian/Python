import requests
import os
from twilio.rest import Client

VIRTUAL_TWILIO_NUMBER = os.environ["ENV_VIRTUAL_TWILIO_NUMBER"]
VERIFIED_NUMBER = os.environ["ENV_VERIFIED_NUMBER"]

STOCK_NAME = "IBM"
COMPANY_NAME = "IBM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_APIKEY = "demo"
NEWS_APIKEY = os.environ["ENV_NEWS_APIKEY"]
account_sid = os.environ["ENV_ACCOUNT_SID"]
auth_token = os.environ["ENV_AUTH_TOKEN"]

stock_parameter = {
    "function" : "TIME_SERIES_DAILY",
    "symbol"  : STOCK_NAME,
    "apikey" : STOCK_APIKEY,
}

news_parameter = {
    "language" : "en",
    "apiKey" : NEWS_APIKEY,
    "qInTitle": COMPANY_NAME,
}

def calculate_stock(a:float, b:float):

    return round(((a - b) / b) * 100)

response1 = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
response1.raise_for_status()
response2 = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
response2.raise_for_status()

stock_data = response1.json()
articles = response2.json()["articles"]

price_close1 = stock_data["Time Series (Daily)"]["2025-06-06"]["4. close"]
price_close2 = stock_data["Time Series (Daily)"]["2025-06-05"]["4. close"]

price_now = float(price_close1)
price_yesterday = float(price_close2)

three_articles = articles[:3]

diff_percent = calculate_stock(price_now, price_yesterday)
up_down = None


def send_message():
    formatted_articles = [f"{STOCK_NAME} {up_down}{diff_percent}%\nHeadline: {articles['title']}\nBrief: {articles['description']}" for articles in three_articles]
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER,
        )
        print(message.status)

if diff_percent > 0:
    up_down = "🔺+"
    send_message()
else:

    up_down = "🔻"
    send_message()
