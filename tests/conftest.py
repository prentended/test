# conftest.py
import pytest
import uiautomator2 as u2
import time

#scope='session'
#cope='module'
"""
你可以通过 scope 参数控制 fixture 的生命周期，常用的作用域有：
function（默认）：每个测试用例调用前都会创建一个新的 fixture 实例。
class：每个测试类的实例调用前只创建一次。
module：每个测试模块调用前只创建一次。
session：在整个测试会话中只创建一次。
"""

times = 2
@pytest.fixture(scope='session')
def setup_device():
    # 重试连接，确保设备连接成功
    retries = 3
    for attempt in range(retries):
        try:
            device = u2.connect('192.168.8.83')
            print('connect success')
            print(device.info)
            break
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(2)  # 每次重试等待2秒
    device.app_start("com.pairlink.insona.bluebee")
    yield device
    device.app_stop("com.pairlink.insona.bluebee")
    device.disconnect()


@pytest.fixture(scope='function', autouse=True)
def ensure_app_in_foreground(setup_device):
    # 确保应用在前台
    device = setup_device
    if not device.app_wait("com.pairlink.insona.bluebee", front=True):
        device.app_start("com.pairlink.insona.bluebee")
    yield