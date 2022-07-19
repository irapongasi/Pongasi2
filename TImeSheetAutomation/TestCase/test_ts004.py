import pytest
import time
import easygui

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestTwo:

    def test_ts004(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("sampleone@gmail.com")
        password = homepage.getPw().send_keys("12345")
        time.sleep(2)
        homepage.getSign().click()

        easygui.msgbox("We cannot find that user", title = "Error Message")



