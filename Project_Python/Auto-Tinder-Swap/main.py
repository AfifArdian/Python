import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

load_dotenv()

FB_EMAIL = os.environ["EMAIL"]
FB_PASSWORD = os.environ["PASSWORD"]
PHONE_NUMBER = os.environ["NUMBER2"]

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")

# Allow cookies
sleep(3)
cookie_button = driver.find_element(by=By.XPATH, value='//*[@id="u964729768"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_button.click()

# Login section
sleep(5)
login_button = driver.find_element(by=By.XPATH, value='//*[text()="Log in"]')
login_button.click()

# Login with Facebook
sleep(3)
fb_login = driver.find_element(by=By.XPATH, value='//*[@id="u-763651308"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[3]/button')
fb_login.click()

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
sleep(5)
email_field = driver.find_element(by=By.NAME, value='email')
email_field.send_keys(FB_EMAIL)
password_field = driver.find_element(by=By.NAME, value='pass')
password_field.send_keys(FB_PASSWORD, Keys.ENTER)

sleep(5)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value='div[aria-label="Lanjutkan sebagai Yuki"]')
submit_button.click()

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Verified Number
sleep(5)
number_field = driver.find_element(by=By.NAME, value='phone_number')
number_field.send_keys(PHONE_NUMBER)
next_button = driver.find_element(by=By.XPATH, value='//*[@id="u-763651308"]/div/div/div[2]/div/div[3]/button')
next_button.click()
input("Press Enter when you have solved the Verified number")

# Allow location
sleep(3)
location_button = driver.find_element(by=By.XPATH, value='//*[@id="u-763651308"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_button.click()

# Disallow notifications
sleep(3)
notification_button = driver.find_element(by=By.XPATH, value='//*[@id="u-763651308"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification_button.click()

for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

    driver.quit()