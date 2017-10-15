#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

data = {
    'i': '爱',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': 1508042272532,
    'sign': 'c6915fabebfee0ab9667fab45651f58a',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'true'
}
headers = {
    'Origin':'http//fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

src = input('请输入要翻译的内容：')
data['i'] = src

data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

target = json.loads(html)
target = target['translateResult'][0][0]['tgt']
print(target)