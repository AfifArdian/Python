import os
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = os.environ["INSTAGRAM_USERNAME"]
PASSWORD = os.environ["INSTAGRAM_PASSWORD"]

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Login Session
        sleep(5)
        username_field = self.driver.find_element(by=By.NAME, value='username')
        password_field = self.driver.find_element(by=By.NAME, value='password')

        username_field.send_keys(USERNAME)
        password_field.send_keys(PASSWORD)

        sleep(3)
        password_field.send_keys(Keys.ENTER)

        sleep(5)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        sleep(10)
        # Find the follower popup element
        # The xpath of the scroll_popup that shows the followers will change over time. Update yours accordingly.
        scroll_popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        for _ in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_popup)
            sleep(3)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_followers_button = self.driver.find_elements(by=By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button')

        for button in all_followers_button:
            try:
                button.click()
                sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value='//button[contains(text(), "Cancel")]')
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()