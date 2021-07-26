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
driver.find_element_by_xpath('//android.widget.LinearLayout/android.widget.FrameLayout').click()
driver.press_keycode(29,64,59)
time.sleep(2)
driver.long_press_keycode('3')
# driver.press_keycode('clear')
driver.press_keycode('9')
time.sleep(1)
time.sleep(2)
driver.quit()