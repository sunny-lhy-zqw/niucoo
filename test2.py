from appium import webdriver

des={
    "platformName": "android",
    "platformVersion": "6.0.1",
    "deviceName":"mumu",
    "appPackage":"cn.niucoo.niucooapp",
    "appActivity":"cn.niucoo.niucooapp.main.MainActivity",
    "udid":"emulator-5554",
    "newCommendTimeout":10,#新命令的超时时长
    "noReset":True,
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',des)
