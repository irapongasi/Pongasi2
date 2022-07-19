from datetime import datetime

import pytest
from selenium import webdriver
import time
import datetime as dt

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestThirty:

    def test_ts030(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("xani@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn "
                                                                                         "btn-primary']"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Work"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Task Calendar"))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='fc-content']/div[2]"))).click()

        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click = "
                                                                                  "'deleteSingle()']"))).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@ng-click = 'yes()']").click()
        time.sleep(3)


