from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


class InternetSpeedTwitterBot:
    def __init__(self, path_to_edge_webdriver) -> None:
        self.service = service.Service(path_to_edge_webdriver)
        self.driver = webdriver.Edge(service=self.service)
        self.down = 0 # download speed
        self.up = 0 # upload speed


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.CLASS_NAME, "start-button").click()

        time.sleep(120)

        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        return self.down, self.up
    

    def tweet_at_provider(self, twitter_email, twitter_password):
        print("The Internet Speed is slower")
        
        # self.driver.get("https://twitter.com/i/flow/login")
        # time.sleep(5)

        # email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # email.click()
        # email.send_keys(twitter_email)
        # time.sleep(3)
        # next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        # next_btn.click()
        # time.sleep(10)
        # password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        # password.send_keys(twitter_email)
        # pass_login = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        # pass_login.click()
        # time.sleep(10)

        # write = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        # time.sleep(10)
        # write.send_keys(f"My Internet speed is slow!")
        # tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
        #                                         'div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/'
        #                                         'div[3]/div/span/span')
        # time.sleep(30)
        # tweet.click()
        # time.sleep(30)