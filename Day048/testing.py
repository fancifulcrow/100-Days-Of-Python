# most of the selenium has changed from the time of recording of the video
from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By

# Make sure your browser version and web driver version are same
service = service.Service(r"..\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Finding an element on a website
amazon_url = "https://www.amazon.com/dp/B0C7FYRWF9/"
driver.get(amazon_url)

amazon_item_price = float(f"{driver.find_element(By.CLASS_NAME, 'a-price-whole').text}.{driver.find_element(By.CLASS_NAME, 'a-price-fraction').text}")
print(amazon_item_price)

amazon_search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
print(amazon_search_bar.get_attribute("placeholder"))

amazon_item_availability = driver.find_element(By.XPATH, "//*[@id='availability']/span")
print(amazon_item_availability.text)

# driver.quit()
