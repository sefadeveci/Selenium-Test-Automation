import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


class TestPurchaseRemove():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_purchase_and_remove(self):
        self.driver.get("https://www.testrelic.com/bugshop/")
        self.driver.set_window_size(1619, 878)
        self.driver.find_element(By.LINK_TEXT, "Women").click()
        self.driver.find_element(By.CSS_SELECTOR, "#edd_download_94 .attachment-thumbnail").click()
        self.driver.find_element(By.LINK_TEXT, "Purchase").click()
        self.driver.find_element(By.LINK_TEXT, "Women").click()
        self.driver.find_element(By.CSS_SELECTOR, "#edd_download_97 .attachment-thumbnail").click()
        self.driver.find_element(By.LINK_TEXT, "Purchase").click()
        self.driver.find_element(By.LINK_TEXT, "Remove").click()
        self.driver.find_element(By.LINK_TEXT, "Remove").click()
        self.driver.find_element(By.ID, "edd_checkout_wrap").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".edd_empty_cart").text == "Your cart is empty."
