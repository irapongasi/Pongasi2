import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestTwentyFour:

    def test_ts024(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("xani@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn "
                                                                                         "btn-primary']"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Work"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Task Calendar"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[2]/td["
                                                                                  "@class='fc-widget-content']"))).click()
        time.sleep(3)
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-cancel']"))).click()
        time.sleep(3)
