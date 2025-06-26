import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from time import sleep

load_dotenv()

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

EMAIL = os.environ["ACCOUNT_EMAIL"]
PASSWORD = os.environ["ACCOUNT_PASSWORD"]
PHONE_NUMBER = "12345678"

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4239099920&f_AL=true&geoId=101165590&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Click Sign in Button
sleep(2)
signin_button = driver.find_element(By.XPATH, value="//*[@id='base-contextual-sign-in-modal']/div/section/div/div/div/div[2]/button")
signin_button.click()

# Sign in
sleep(3)
email_field = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# Save jobs
# sleep(3)
# save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
# text_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button/span[1]')
# if text_button.text == "Save":
#     save_button.click()
# else:
#     print("you have saved the job")

# Get Listings
sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

#Locate the apply button
for listing in all_listings:
    print("Opening Listing")
    try:
        close_toast = driver.find_element(By.CSS_SELECTOR, "#artdeco-toasts .artdeco-toasts_toasts div button")
        close_toast.click()
        sleep(5)
    except:
        pass  # Jika tidak ada tombol close, lanjut saja
    sleep(5)
    listing.click()
    sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(By.XPATH, value='//*[@id="jobs-apply-button-id"]')
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        sleep(5)
        phone = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4248588222-21315709508-phoneNumber-nationalNumber"]')
        if phone.text == "":
            phone.send_keys(PHONE_NUMBER)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()


    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

sleep(5)
driver.quit()