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
ele = driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.FrameLayout')
print(ele.get_attribute('resourceId'))
# print(ele.tag_name)
print(ele.size)
print(ele.location)
print(ele.rect)
