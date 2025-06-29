import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Part 1 - Scrape the links, addresses, and prices of the rental properties
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf4QG7WBkw0OtOXybykGMYk3IOwIK0LrSVhRrYvvUiNIYmz5w/viewform?usp=header"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/", headers=header)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

# Create a list of all the links
all_link_property = [link.get('href') for link in soup.find_all(name="a", class_="property-card-link")]
print(f"There are {len(all_link_property)} links to individual listings in total: \n")
print(all_link_property)

# Create a list of all the prices
# Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
all_price_property = [price.getText().strip('+ 1bd +/mo') for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
print(f"\n After having been cleaned up, the {len(all_price_property)} prices now look like this: \n")
print(all_price_property)

# Create a list of all the addresses
# Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
all_address_property = [address.getText().replace('|', '').strip() for address in soup.find_all(name="address")]
print(f"\n After having been cleaned up, the {len(all_address_property)} addresses now look like this: \n")
print(all_address_property)

# Part 2 - Fill in the Google Form using Selenium

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=chrome_options)

drive.get(url=FORM_URL)

for i in range(len(all_link_property)):
    form = drive.find_elements(by=By.CLASS_NAME, value="whsOnd")
    address_property = form[0]
    price_property = form[1]
    link_property = form[2]

    address_property.send_keys(all_link_property[i])
    price_property.send_keys(all_price_property[i])
    link_property.send_keys(all_link_property[i])

    submit = drive.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    sleep(2)
    another_answer = drive.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_answer.click()
    sleep(2)