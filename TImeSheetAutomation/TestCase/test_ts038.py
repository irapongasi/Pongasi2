import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestThirtyEight:

    def test_ts038(self):
        homepage = HomePage(self.driver)
        eMail = homepage.getEmail().send_keys("cevuq@mailinator.com")
        password = homepage.getPw().send_keys("P@ssW0rdNgL@h@t")
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn "
                                                                                         "btn-primary']"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "Projects"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Forecast Reports"))).click()
        WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Forecast Report by "
                                                                                      "Business Unit"))).click()

        time.sleep(5)
