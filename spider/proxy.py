#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import urllib.request

url = 'http://whatismyip.com'

proxy_support = urllib.request.ProxyHandler({'socks5': '127.0.0.1:1080'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)