import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import smtplib

MY_LAT = -6.175110
MY_LONG = 106.865036
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_keys = "a8f9113e0896dd0c4132a15e50a115dc"

account_sid = "AC610bb270f99a70e307a5ffbe4d0949fb"
auth_token = "88d14a5c9af89b7630c039c0bae6e098"

# MY_EMAIL = "akanoyui9@gmail.com"
# MY_PASSWORD = "dgdwsffmmydqmdkg"

parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid" : api_keys,
        "cnt" : 4,
    }

response = requests.get(url=OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_list = [weather_data["list"][data]["weather"][0]["id"] for data in range(4)]

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
# if you want to use twilio
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+6281295463018",
    )
    print(message.status)

# if you want to use smtplib
# if will_rain:
#     # with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     #     connection.starttls()
#     #     connection.login(MY_EMAIL, MY_PASSWORD)
#     #     connection.sendmail(from_addr=MY_EMAIL,
#     #                         to_addrs=MY_EMAIL,
#     #                         msg=f"Subject:weather conditions\n\nIt's going to rain today. Remember to bring an Umbrella")

