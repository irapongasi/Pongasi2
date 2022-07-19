import pytest
import time

from pageObjects.HomePage import HomePage

@pytest.mark.usefixtures("setup")
class TestSeven:

    def test_ts007(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("xani@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        homepage.getSign().click()
        time.sleep(4)









