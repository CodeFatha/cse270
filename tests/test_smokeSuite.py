# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class TestSmokeTest():
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_home(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1371, 1087)
        elements = self.driver.find_elements(By.CSS_SELECTOR, 
                                             ".header-logo img")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".header-title > h1").text == "Teton Idaho"
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".header-title > h2").text == "Chamber of Commerce"
        assert self.driver.title == "Teton Idaho CoC"
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
        assert len(elements) > 0
        self.driver.find_element(By.LINK_TEXT, "Join Us").click()

    def test_directory(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/directory.html")
        self.driver.set_window_size(1391, 1080)
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"

    def test_admin(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/admin.html")
        self.driver.set_window_size(1391, 1080)
        self.driver.find_element(By.ID, "username").send_keys("incorrect")
        self.driver.find_element(By.ID, "password").send_keys("incorrect")
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".mysubmit:nth-child(4)").click()
        WebDriverWait(self.driver, 30).until
        (expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".errorMessage"), "Invalid username and password."))

    def test_join(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/join.html")
        self.driver.set_window_size(1391, 1080)
        elements = self.driver.find_elements(By.NAME, "fname")
        assert len(elements) > 0
        self.driver.find_element(By.NAME, "fname").send_keys("Bheki")
        self.driver.find_element(By.NAME, "lname").send_keys("Ncube")
        self.driver.find_element(By.NAME, "bizname").send_keys("Legacy")
        self.driver.find_element(By.NAME, "biztitle").send_keys("CEO")
        self.driver.find_element(By.NAME, "submit").click()
        elements = self.driver.find_elements(By.NAME, "email")
        assert len(elements) > 0
