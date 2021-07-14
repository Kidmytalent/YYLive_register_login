# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: register_page.py
# @Date: 2021/6/26  19:35

from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.basepage import BasePage


class RegisterPage(BasePage):

    def register(self, r_info):
        '''
        注册成功
        :return:
        '''
        self._params['phonenum'] = r_info

        self.keyword_drive('../pages/register.yaml', 'register')
