# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: quit_login_page.py
# @Date: 2021/6/27  0:36
from appium.webdriver.common.mobileby import MobileBy

from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.basepage import BasePage


class QuitLogin(BasePage):

    def quit_login(self):

        self.keyword_drive('../pages/quit_login.yaml', 'quit_login')

