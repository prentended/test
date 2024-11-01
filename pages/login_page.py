# login_page.py
from study123.pages.base_page import BasePage
import time
times =2
class LoginPage(BasePage):
    login_button1 = {"text": "登录"}
    username_input = {"text": "用户账号/服务商账号"}
    password_input = {"text": "请输入密码"}
    agree = {"className": "android.widget.ImageView", "instance": 3}
    login_button2 = {"text": "登录"}

    def login(self, username, password):
        self.click(self.login_button1)
        time.sleep(times)
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        time.sleep(times)
        self.click(self.agree)
        time.sleep(times)
        self.click(self.login_button2)
        time.sleep(times)