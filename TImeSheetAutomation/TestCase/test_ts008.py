import pytest
from selenium import webdriver
import time

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestEight:

    def test_ts008(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("cevuq@mailinator.com")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        homepage.getSign().click()
        time.sleep(5)
