import time
from appium import webdriver

des={
    "platformName": "Android",
    "platformVersion": "7.0.1",
    "deviceName": "Samsung Galaxy S9",
    "appPackage": "com.android.dialer",
    "appActivity": "com.android.dialer.DialtactsActivity",
    "udid": "192.168.56.103:5555",
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
time.sleep(2)
# driver.lock(1)
# print(driver.is_locked())
# driver.lock(1)
# time.sleep(1)
# driver.unlock()
# time.sleep(2)
# driver.open_notifications()
# driver.orientation='LANDSCAPE'
# print(driver.orientation)
# time.sleep(2)
# driver.orientation='PORTRAIT'
# time.sleep(2)
# print(driver.orientation)
# print(driver.get_window_size())
# print(driver.network_connection)
# driver.save_screenshot('./picture/test.png')
print(driver.get_device_time(format='YYYY-MM-DDTHH'))
driver.quit()


