import requests
import smtplib
from bs4 import BeautifulSoup
# Add the os and dotenv modules
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
live_url2 = "https://www.amazon.com/SENSARTE-Cookware-Nonstick-Induction-Non-toxic/dp/B0D2H94CD1/ref=sr_1_2_sspa?_encoding=UTF8&content-id=amzn1.sym.0f1ddd2e-dc49-404c-9cb8-157e3c873622&crid=IBML6MYDLJ4A&dib=eyJ2IjoiMSJ9.OTc83yAtAs5UAIBYbfUddX2UBmIZzcm8duN-4S_mAnEZVnaLESWvxYIFLw2UMhQU0RWwFV2G5hnU4K_WOTQXA0-9d9nycvo4dGYPWKlgFId1R2F2ENCu8jvuW5ZRGDst0llqhCFx5gAvUrr3YiGsI3q1-R6vn7aOYWEOkgCzcr9FFx3P6oh0maP_3Xdn9kenFLJfj8qApuij5aWh6nkuS0SY8En-u-lRKMG4QNgyIErPo0w3CD6vFggY--4zzC8mozo1Zrs9VcFHDC8DpDZsB_zEYGAhDrGpA8rYSzayxms.gbpk8-b3zsu5i8KQK8-8i_fGten8o9NkQ1Pw1A_FSqw&dib_tag=se&keywords=Dinnerware%2B%26%2Baccessories&pd_rd_r=2acdbdcc-de58-486c-802f-e313b25941b1&pd_rd_w=T8q0H&pd_rd_wg=Evzse&qid=1750426707&sprefix=dinnerware%2B%26%2Baccessorie%2Caps%2C190&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
# ====================== Add Headers to the Request ===========================

# Full headers would look something like this
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
#     "Dnt": "1",
#     "Priority": "u=4, i",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
# }


# A minimal header would look like this:
header = {
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
}

response = requests.get(url=live_url2, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

# Find the HTML element that contains the price

price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").getText().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        message = f"{title} is on sale for {price_as_float}"
        connection.starttls()
        connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{live_url}".encode("utf-8")
        )