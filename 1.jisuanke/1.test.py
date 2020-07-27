#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver
import json
import time

driver = webdriver.Chrome()
coockie_file = './cookie_file'
driver.get('https://www.jisuanke.com/')
#element_login_button = driver.find_element_by_link_text
#导入cookie
with open(coockie_file, 'r') as f:
    cookies = json.load(f) #cookie是json结构，解析json
    for cookie in cookies:
        driver.add_cookie(cookie)
driver.get('https://www.jisuanke.com/course/792')
url = driver.find_element_by_css_selector("span[class='lesson-icon-challenge']")
#time.sleep(10)
#driver.get(url)
print(url)
