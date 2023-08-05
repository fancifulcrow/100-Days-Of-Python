# most of the selenium has changed from the time of recording of the video
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Make sure your browser version and web driver version are same
service = service.Service(r"..\msedgedriver.exe")
driver = webdriver.Edge(service=service)



### Finding an element on a website ###

# Scraping on Amazon to get the price of a particular item
amazon_url = "https://www.amazon.com/dp/B0C7FYRWF9/"
driver.get(amazon_url)

amazon_item_price = float(f"{driver.find_element(By.CLASS_NAME, 'a-price-whole').text}.{driver.find_element(By.CLASS_NAME, 'a-price-fraction').text}")
print(amazon_item_price)

amazon_search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
print(amazon_search_bar.get_attribute("placeholder"))

amazon_item_availability = driver.find_element(By.XPATH, "//*[@id='availability']/span")
print(amazon_item_availability.text)

# Scraping Python's oficial website to get the upcoming events
python_docs_url = "https://www.python.org/"
driver.get(python_docs_url)

event_times = [event_time.text for event_time in driver.find_elements(By.CSS_SELECTOR, ".event-widget time")]
event_names = [event_name.text for event_name in driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")]

upcoming_events = {}

for n in range(len(event_times)):
    upcoming_events[n] = {
        "time" : event_times[n],
        "name" : event_names[n],
    }

print(upcoming_events)

# Scraping Wikipedia to find the number of articles in English
wikipedia_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wikipedia_url)
article_count = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")

print(article_count.text)



### Filling Out Forms and Clicking Buttons with Selenium ###

# we will continue to scrape Wikipedia's main page
all_portals = driver.find_element(By.LINK_TEXT, "Site news")
all_portals.click()

try:
    driver.find_element(By.CLASS_NAME, "search-toggle").click()
except:
    pass

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(5)

# Scraping London App Brewery Example Login
example_website_login = "http://secure-retreat-92358.herokuapp.com/"
driver.get(example_website_login)

driver.find_element(By.NAME, "fName").send_keys("John")
driver.find_element(By.NAME, "lName").send_keys("Doe")
driver.find_element(By.NAME, "email").send_keys("example@gmail.com")

driver.find_element(By.TAG_NAME, "button").click()

time.sleep(5)

driver.quit()