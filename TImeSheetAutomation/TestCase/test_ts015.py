import pytest
from selenium import webdriver
import time


from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestFifteen:

    def test_ts015(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("towo@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        time.sleep(5)
        homepage.getSign().click()
        time.sleep(6)
        self.driver.find_element_by_link_text("My Work").click()
        time.sleep(6)
        self.driver.find_element_by_link_text("My Task Calendar").click()
        time.sleep(6)
        self.driver.find_element_by_xpath("//div[@class='fc-right']/button").click()
        time.sleep(6)