import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestNineteen:

    def test_ts019(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("towo@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        homepage.getSign().click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Work"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Task Calendar"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[2]/td["
                                                                                  "@class='fc-widget-content']"))).click()
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='startTime']"))).clear()
        self.driver.find_element_by_xpath("//input[@name='startTime']").send_keys(" 2017-10-30 07:30:00")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='stopTime']"))).clear()
        self.driver.find_element_by_xpath("//input[@name='stopTime']").send_keys(" 2017-10-30 06:30:00")
        time.sleep(5)