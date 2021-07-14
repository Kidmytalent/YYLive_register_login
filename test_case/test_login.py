# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_login.py
# @Date: 2021/6/26  19:36
from YY_Live_Register_Login_Key_Data_Yaml_PO.pages.app import App   # 常在这里犯错，注意导入文件名要一致


class TestLogin:
    login_user_info = {'username': '不才Damon'}
    login_pass_info = {'password': 'Eugene8955327'}
    person_info_register = '13202542294'


    def setup(self):
        self.app = App()

    def test_register(self):

        r_info = self.person_info_register
        self.app.goto_home().goto_person_center().goto_login().goto_register().register(r_info)


    def test_login(self):

        u_info = self.login_user_info  # 记住 --->  不要忘了self，不然不是全局变量，是调用不到上面的 person_information_login 的
        p_info = self.login_pass_info

        pages = self.app.goto_home().goto_person_center().goto_login()
        pages.straight_login(u_info, p_info).quit_login()

    def test_quit(self):

        self.app.goto_home().goto_click_quit().quit_login()

