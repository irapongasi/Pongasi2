import pytest
from selenium import webdriver
import time
import easygui

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_ts003(self):
        homepage = HomePage(self.driver)
        time.sleep(3)
        eMail = homepage.getEmail().send_keys(" ")
        password = homepage.getPw().send_keys("")
        homepage.getSign().click()
        easygui.msgbox("Email field: Please fill out this field", title="Error Message")
