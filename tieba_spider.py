#!/usr/bin/env python
# coding=utf-8
import re
import requests

name = input('请输入关键字:')
begin = int(input('开始页数:'))
end =int(input('结束页数:'))

cnt = 0
for i in range(begin, end + 1):
    url = "https://tieba.baidu.com/f?kw="+name+"&ie=utf-8&pn="+str(i * 50)
    html = requests.get(url)
    html.encoding = 'utf-8'
    p = "http.*?\.jpg"
    pic_urls = re.findall(p, html.text);
    #print(pic_urls)
    """下载"""
    for pic_url in pic_urls:
        try:
            pic = requests.get(pic_url)
            string = './data/tieba/images/' + str(cnt + 1) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(cnt + 1), str(pic_url)))
            cnt += 1
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(cnt + 1), str(pic_url)))
            print(e)
            continue
