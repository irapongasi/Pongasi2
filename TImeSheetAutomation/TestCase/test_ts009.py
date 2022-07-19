import pytest
from selenium import webdriver
import time

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestNine:

    def test_ts009(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("towo@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        homepage.getSign().click()
        time.sleep(5)
