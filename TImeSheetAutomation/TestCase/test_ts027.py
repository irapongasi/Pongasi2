from datetime import datetime

import pytest
from selenium import webdriver
import time
import datetime as dt

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestTwentySeven:

    def test_ts027(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("xani@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn "
                                                                                         "btn-primary']"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Work"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Task Calendar"))).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='fc-content']/div[2]").click()
        time.sleep(6)

        mytime = dt.datetime.strptime('130000', '%H%M%S').time()
        mydatetime = str(dt.datetime.combine(dt.date.today(), mytime))

        self.driver.find_element_by_xpath("//input[@name='startTime']").clear()
        self.driver.find_element_by_xpath("//input[@name='startTime']").send_keys(mydatetime)
        time.sleep(2)

        mystime = dt.datetime.strptime('200000', '%H%M%S').time()
        stptime = str(dt.datetime.combine(dt.date.today(), mystime))

        self.driver.find_element_by_xpath("//input[@name='stopTime']").clear()
        self.driver.find_element_by_xpath("//input[@name='stopTime']").send_keys(stptime)
        time.sleep(2)

        self.driver.find_element_by_id("description").clear()
        time.sleep(2)
        self.driver.find_element_by_id("description").send_keys('Timesheet Testing Edited')
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)

