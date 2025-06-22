# Link selenium documentation = https://selenium-python.readthedocs.io/api.html#selenium.webdriver.common.by.By.CLASS_NAME
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome Webdriver
driver = webdriver.Chrome(chrome_options)

# Python.org link
driver.get("https://www.python.org/")

# By.CLASS_NAME
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

# By.name
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

#By.ID
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTOR
documentation = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation.text)

# By.XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[8]/ul/li[1]/a')
# print(bug_link.text)

# My Own Version
# upcoming_event = {}
# times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul li ")
# for T in range(len(times)):
#     date = times[T].find_element(By.CSS_SELECTOR, value="time")
#     link = times[T].find_element(By.CSS_SELECTOR, value="a")
#     upcoming_event[T] = {
#         "time": date.text,
#         "name": link.text,
#     }
# print(upcoming_event)

# Course Version
# event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
# print(events)

# with nested dictionary comprehension
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {n: {"time": event_times[n].text, "name": event_names[n].text} for n in range(len(event_times))}
print(events)



"""
.close:
    -> Only closes the current active browser tab or window.
    -> If there are multiple tabs or windows open, only one (the active one) will be closed.
    -> The WebDriver session remains running.
    Suitable if you only want to close one tab without ending the entire session.
"""
# driver.close()

""" 
.quit:
   -> Closes the entire browser and all open tabs or windows.
   -> Ends the entire WebDriver session.
   -> Cleans up resources used by WebDriver.
Typically used when a script has finished running and you want to stop everything cleanly.
"""
driver.quit()