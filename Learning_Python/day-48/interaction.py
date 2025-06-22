from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome Webdriver
driver = webdriver.Chrome(chrome_options)

# Practice Link
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Wikipedia link
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

# Find element By Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by name
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

# Find the first name, last name, email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("sadasdasd")
last_name.send_keys("sadasdasd")
email.send_keys("sadasdasd@asdad.com")

# Locate the "Sign Up" button. Then click on it
button = driver.find_element(By.TAG_NAME, value="button")
button.click()

# driver.quit()
