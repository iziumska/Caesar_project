class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_title_name(self):
        return self.driver.title
