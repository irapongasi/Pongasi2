import pytest
import time
import easygui

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestSix:

    def test_ts006(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("resignedemployee@mailinator.com")
        password = homepage.getPw().send_keys("123456")
        time.sleep(6)
        homepage.getSign().click()

        easygui.msgbox("We cannot find that user", title = "Error Message")



