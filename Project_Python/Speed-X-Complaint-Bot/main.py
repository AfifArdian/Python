import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
X_EMAIL = os.environ["EMAIL"]
X_PASSWORD = os.environ["PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self):
        # Setup Chrome driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        sleep(5)
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        sleep(60)
        self.down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get("https://x.com/home")

        #Login Session
        sleep(5)
        username = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username.send_keys(X_EMAIL, Keys.ENTER)
        sleep(5)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys(X_PASSWORD, Keys.ENTER)

        # Tweet session
        sleep(10)
        tweet_compose= self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed{self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
        tweet_compose.send_keys(tweet)

        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
