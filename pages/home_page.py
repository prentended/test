# home_page.py
from study123.pages.base_page import BasePage

class HomePage(BasePage):
    profile_button = {"text": "连接现有系统"}
    def go_to_profile(self):
        self.click(self.profile_button)