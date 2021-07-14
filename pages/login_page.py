# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: login_page.py
# @Date: 2021/6/26  19:35

from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.basepage import BasePage
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.quit_login_page import QuitLogin
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.register_page import RegisterPage


class LoginPage(BasePage):

    def goto_register(self):
        '''
        没有账号，去注册
        :return:
        '''
        self.keyword_drive('../pages/login_page.yaml', 'goto_register')

        return RegisterPage(self.driver)


    def straight_login(self, u_info, p_info):
        '''
        有账号，直接登录
        :return:
        '''
        self._params['user'] = u_info['username']
        self._params['pass'] = p_info['password']
        self.keyword_drive('../pages/login_page.yaml', 'straight_login')

        return QuitLogin(self.driver)
