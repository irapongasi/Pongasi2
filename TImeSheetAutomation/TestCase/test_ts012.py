import pytest

import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestTwelve:

    def test_ts012(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("towo@mailinator.net")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn "
                                                                                         "btn-primary']"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Work"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Task Calendar"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='fc-button-group']/button[1]"))).click()

        time.sleep(3)