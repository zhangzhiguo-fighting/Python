#!/usr/bin/env python
# coding=utf-8
import requests

src="https://imgsa.baidu.com/forum/pic/item/1a4c510fd9f9d72aa7925f19db2a2834359bbbc4.jpg"
response = requests.get(src)
with open('./data/tieba/images/1.jpg', 'wb') as f:
    f.write(response.content)
