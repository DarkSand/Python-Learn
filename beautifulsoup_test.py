#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup as bsp
import re

response = requests.get("http://www.jd.com", verify=False)
soup = bsp(response.content)


def number_span(tag):
    return tag.name == 'a' and '登录' in tag.text


print soup.find(number_span)
print soup.find(lambda tag: tag.name == 'a' and '登录' in tag.text)
print soup.find('a', class_=re.compile('.*link.*'))
