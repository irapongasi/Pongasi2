from selenium.webdriver.common.by import By

from selenium import webdriver


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.NAME, "email")
    pw = (By.ID, "inputPassword")
    sign = (By.CSS_SELECTOR, "button[class='btn btn-primary']")

    # successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPw(self):
        return self.driver.find_element(*HomePage.pw)

    def getSign(self):
        return self.driver.find_element(*HomePage.sign)
