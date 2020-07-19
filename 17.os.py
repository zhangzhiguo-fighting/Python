#!/usr/bin/env python
# coding=utf-8

'''os模块'''

import os

#打开文件
path = '/home/zhangzhiguo/'
dirs = os.listdir(path)

for file in dirs:
    print(file)

#创建多级目录
path = './test/git/a/b/c'
#os.makedirs(path)

#判断路径是否存在
if os.path.exists(path) == True:
    print(path, 'is exist!')
else:
    dirs = os.makedirs(path)
    print("创建 {} successful!".format(path))
