# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: home_page.py
# @Date: 2021/6/26  19:35
import time

from appium.webdriver.common.mobileby import MobileBy

from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.basepage import BasePage
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.person_info_page import PersonInforPage
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.quit_login_page import QuitLogin


class HomePage(BasePage):
    def goto_person_center(self):


        self.keyword_drive('../pages/home_page.yaml', 'goto_person_center')

        return PersonInforPage(self.driver)

    def goto_click_quit(self):

        self.clickable_wait(15, MobileBy.XPATH, "//*[@text='登录YY']")
        self.keyword_drive('../pages/home_page.yaml', 'goto_click_quit')

        return QuitLogin(self.driver)

