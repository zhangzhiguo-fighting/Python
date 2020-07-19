#!/usr/bin/env python
# coding=utf-8
'''urllib的使用'''
import urllib.request

#向指定一个URL发送请求，获取回应
response = urllib.request.urlopen("http://www.haizeix.com")
#获取响应内容
content = response.read().decode('utf-8')
fo = open('./haizei.html', 'w', encoding = 'utf-8')
print(content, file = fo)
#print(content)
fo.close()

#响应头信息
print(response.headers)
#响应码
print(response.status)

