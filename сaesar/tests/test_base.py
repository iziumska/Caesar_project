import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import *


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        self.driver.get(PathUrl().URL_SITE)
        self.login_page = LogInPage(self.driver)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
