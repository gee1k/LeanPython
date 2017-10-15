#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import urllib.request

req = urllib.request.Request('http://placekitten.com/g/500/600')
response = urllib.request.urlopen(req)
cat_img = response.read()
print(response.geturl())
print(response.info())
print(response.getcode())

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_img)
