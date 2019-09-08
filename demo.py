from appium import webdriver

desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'iOS'
desired_caps['deviceName'] = 'iPhone 8'
# udid
desired_caps['udid'] = '613A9BFB-FA81-4C30-A4DC-2DC1DB589571'
# app信息
desired_caps["app"] = "com.itfeat.testDemo"

desired_caps["automationName"] = "XCUITest"


driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % "4723", desired_caps)
