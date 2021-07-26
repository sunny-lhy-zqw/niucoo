import time
from appium import webdriver

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
time.sleep(3)
# driver.tap([(720,2308)])
# ele1 = driver.find_element_by_xpath('//*[@text="声音"]')
# ele2 = driver.find_element_by_xpath('//*[@text="更多"]')
# driver.scroll(ele1,ele2)
# driver.drag_and_drop(ele1,ele2)
# [0,2208][1440,2424],	[0,1416][1440,1632]
# driver.flick(720,2308,0,768)
# driver.swipe(0,2308,0,1516)
# x = driver.get_window_size()['width']
# y = driver.get_window_size()['height']
# print(x,y)
# driver.swipe(x/2,y/2,x/2,y/4)

time.sleep(4)
driver.quit()
