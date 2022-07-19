import pytest
from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestWindow:

    def test_ts111(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("towo@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        time.sleep(2)
        homepage.getSign().click()
        time.sleep(6)

        handles = self.driver.window_handles
        size = len(handles)
        print("Size: ", size)

        for x in range(size):
            self.driver.switch_to.window(handles[x])
            print(self.driver.title)



