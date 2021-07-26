import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
des = {
    'platformName': 'Android',
    'platformVersion': '7.0.1',  #填写android虚拟机的系统版本
    'deviceName': 'Samsung Galaxy S9',   #填写安卓虚拟机的设备名称
    'appPackage': 'com.android.calculator2',   #填写被测试包名
    'appActivity': 'com.android.calculator2.Calculator',    #填写被测试app入口
    'udid': '192.168.56.102:5555',  # 填写通过命令行 adb devices 查看到的 uuid（指定已连接在MAC上的虚拟机）
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
#uiautomator定位
time.sleep(3)
#通过父元素定位到属性不唯一的子元素，用到了instance标识父元素下的第n个元素
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/pad_numeric").childSelector(className("android.widget.Button").instance(1))').click()
#通过子元素定位到父元素，再去找父元素下的兄弟元素
time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.calculator2:id/digit_7").fromParent(text("4"))').click()
driver.fin
