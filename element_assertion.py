import time
from appium import webdriver

des={
    "platformName":"Android",
    "platformVersion":"7.0.1",
    "deviceName":"Samsung Galaxy S9",
    "appPackage":"com.a9second.weilaixi.wlx",
    "appActivity":"io.dcloud.PandoraEntry",
    "udid":"192.168.56.103:5555",
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
time.sleep(2)
driver.find_element_by_id('android:id/button1').click()
time.sleep(2)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(2)
ele = driver.find_element_by_id('com.android.packageinstaller:id/permission_deny_button')
print(ele.is_displayed())
print(ele.is_enabled())
print(ele.is_selected())
