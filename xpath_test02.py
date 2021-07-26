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
#xpath部分属性定位
driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'id/digit_9')]").click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.Button[ends-with(@resource-id,'id/del')]").click()
