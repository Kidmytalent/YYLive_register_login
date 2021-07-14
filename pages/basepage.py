# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: basepage.py
# @Date: 2021/6/26  19:34
import json
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _params = {}

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def wait(self, timeout):
        self.driver.implicitly_wait(timeout)


    def find(self, locator):
        return self.driver.find_element_by_xpath(locator)

    # 没用到
    def visibility_wait(self, timeout, by, locator):  # 定义一个显示等待方法
        wait_time = WebDriverWait(self.driver, timeout).until(
        expected_conditions.visibility_of_element_located((by, locator)))  # 注意参数是元组
        return wait_time

    def clickable_wait(self, timeout, by, locator):  # 等待可点击
        wait_for_click = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by, locator)))
        return wait_for_click


    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'   
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def keyword_drive(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:

            function = yaml.safe_load(f)

            steps: List[Dict] = function[fun_name]

            raw = json.dumps(steps)
            for key, value in self._params.items():
                raw = raw.replace("${" + key + "}", value)
            steps = json.loads(raw)

        for step in steps:   # 解析列表，列出列表中的每一个内容
            if step["action"] == "click":
                self.find(step["locator"]).click()
            elif step["action"] == "send_keys":
                self.find(step["locator"]).send_keys(step["text"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
