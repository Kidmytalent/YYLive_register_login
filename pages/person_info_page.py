# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: person_info_page.py
# @Date: 2021/6/26  19:35

import time
from appium.webdriver.common.mobileby import MobileBy as By, MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.basepage import BasePage
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.login_page import LoginPage


class PersonInforPage(BasePage):
    def goto_login(self):

        self.clickable_wait(20, MobileBy.XPATH, "//*[@text='登录YY']")

        self.keyword_drive('../pages/person_info.yaml', 'goto_login')

        return LoginPage(self.driver)

