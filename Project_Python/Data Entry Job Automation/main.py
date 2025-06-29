import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf4QG7WBkw0OtOXybykGMYk3IOwIK0LrSVhRrYvvUiNIYmz5w/viewform?usp=header"
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=ZILLOW_URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_link_property = [link.get('href') for link in soup.find_all(name="a", class_="property-card-link")]
# print(all_link_property)

all_price_property = [price.getText().strip('+ 1bd +/mo') for price in soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")]
# print(all_price_property)

all_address_property = [address.getText().replace('|', '').strip() for address in soup.find_all(name="address")]
# print(all_address_property)


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