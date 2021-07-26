import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

des={
    "platformName": "Android",
    "platformVersion": "7.0.1",
    "deviceName": "Samsung Galaxy S9",
    "appPackage": "com.android.settings",
    "appActivity": "com.android.settings.Settings",
    "udid": "192.168.56.103:5555",
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
time.sleep(2)
touch = TouchAction(driver)
ele = driver.find_element_by_xpath('//*[@text="屏幕锁定"]')
touch.tap(element=ele).release().perform()
time.sleep(2)
ele2 = driver.find_element_by_xpath('//*[@text="图案"]')
touch.press(el=ele2).release().perform()
time.sleep(2)
touch.press(x=241,y=1037)\
    .wait(100).move_to(x=237,y=1517)\
    .wait(100).move_to(x=719,y=1517)\
    .wait(100).move_to(x=719,y=1996)\
    .wait(100).move_to(x=1203,y=1996).release().perform()
time.sleep(2)
driver.quit()