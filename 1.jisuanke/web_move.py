#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import json
import os
import time

class CodeSpider:
        url = ""
        coockie_file = './cookie_file'
        data_path = './data'
        lesson_name = ''
        lesson_url = []
        num = 0
        course = {'数据结构' : 792, "C语言" : 786}

        def __init__(self, lesson_name = "数据结构", url = 'https://www.jisuanke.com/course/792'):
            print('__init__')
            self.lesson_name = lesson_name
            self.url = url
            driver = webdriver.Chrome()
            driver.set_script_timeout(30)
            driver.get("https://www.jisuanke.com") #没有密码，所以先到未登录主页
            
            #导入cookie
            with open(self.coockie_file, 'r') as f:
                cookies = json.load(f) #cookie是json结构，解析json
                for cookie in cookies:
                    driver.add_cookie(cookie)

            driver.get(self.url)
            time.sleep(3)
            self.driver = driver #为后面接口做准备

        def get_url(self):
            """获取URL"""

        def get_code(self):
            """定位到【程序设计】代码位置"""

        def save_code(self):
            """保存代码"""

        def destroy(self):
            """关闭浏览器"""

if __name__ == "__main__":
    test = CodeSpider()
    test.get_url()
    test.get_code()
    test.destroy()
