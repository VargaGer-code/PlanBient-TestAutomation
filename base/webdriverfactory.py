"""
It creates a webdriver instance based on browser
"""

from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser


    def getWebdriverInstance(self):
        """
        Get webdriver instance based on the browser type
        Returns:
            WebDriver instance
        """
        #baseURL = "https://sandbox.sensomedia.hu/hatvani-admin/login"
        baseURL = "https://sandbox.sensomedia.hu:3000/login"

        if self.browser == "firefox":
            self.driver = webdriver.Firefox(executable_path="C:\\webdrivers\\geckodriver.exe")

        if self.browser == "chrome":
            self.driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")

        if self.browser == "edge":
            self.driver = webdriver.Edge(executable_path="C:\\webdrivers\\msedgedriver.exe")
            

        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get(baseURL)

        return self.driver
