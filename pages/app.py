# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: app.py
# @Date: 2021/6/26  19:34

from appium import webdriver

from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.home_page import HomePage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps={}
        caps['platformName'] = 'Android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = '127.0.0.1:7555'
        caps['appPackage'] = 'com.duowan.mobile'
        caps['appActivity'] = 'com.yy.mobile.plugin.homepage.ui.home.HomeActivity'
        #  不清空缓存启动 app
        caps['noReset'] = 'true'
        #  设置等待页面空闲状态的时间为 0 s
        caps['settings[waitForIdleTimeout'] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def goto_home(self):
        return HomePage(self.driver)