# test_main_flow.py
import pytest
import time
from study123.pages.login_page import LoginPage
from study123.pages.home_page import HomePage

"""
@pytest.fixture(scope='module')
def setup_device():
    device = u2.connect('your_device_ip')
    yield device
    device.disconnect()

def test_main_flow(setup_device):
    device = setup_device
    main_page = MainPage(device)

    # 例：点击按钮
    main_page.click_button("com.example:id/button")

    # 例：获取文本并验证
    assert main_page.get_text("com.example:id/text") == "期望文本"
"""

times = 2
#账户  和密码
account = account
password = password
#@pytest.fixture(autouse=True)
@pytest.mark.usefixtures("setup_device")
def test_login_and_navigate(setup_device):
    driver = setup_device
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    time.sleep(times)
    # 登录操作
    login_page.login(account, password)
    time.sleep(times)
    # 验证主页是否加载
    assert driver(text="连接现有系统").exists, "登录失败，未能找到连接页面"
    home_page.go_to_profile()
    time.sleep(times)