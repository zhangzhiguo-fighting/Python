#!/usr/bin/env python
# coding=utf-8

import re

str1 = '<a rel="noreferrer" href="/p/3582435386" title="【科比绝伦】科吧你好，安琪还在。" target="_blank" class="j_th_tit " clicked="true">【科比绝伦】科吧你好，安琪还在。</a>'
str2 = '<a rel="noreferrer" href="/p/6470878284" title="【科比绝伦】What Can I Say" target="_blank" class="j_th_tit ">【科比绝伦】What Can I Say</a>'

pattern = re.compile(r'<a rel="noreferrer" href="/p/\d+?" title=".+?" target="_blank" class="j_th_tit">(.+?)</a>')
