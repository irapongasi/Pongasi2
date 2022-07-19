import pytest
import time
import easygui


from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestThree:

    def test_ts005(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("stratpoint2014@gmail.com")
        password = homepage.getPw().send_keys("zyxwvut")
        time.sleep(2)
        homepage.getSign().click()

        easygui.msgbox("We cannot find that user", title = "Error Message")



