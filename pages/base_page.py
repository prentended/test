# base_page.py
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver(**locator)

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        self.find_element(locator).set_text(text)