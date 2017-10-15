#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import os
import urllib.request
import urllib.error
import random
import re
from bs4 import BeautifulSoup


def url_open(url):
    print('open url --> %s' % url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    proxies = ['116.199.115.78:80', '180.153.58.154:8088', '182.92.189.44:8888']
    proxy = random.choice(proxies)

    proxy_support = urllib.request.ProxyHandler({'http': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)

    try:
        response = urllib.request.urlopen(req)
        html = response.read()
    except urllib.error.URLError as e:
        html = ''

    return html


def get_page(url):
    html = url_open(url).decode('utf-8')

    bs_obj = BeautifulSoup(html, "lxml")
    span = bs_obj.find('span', {'class': 'current-comment-page'}).text
    cur_page = int(span[1:len(span)-1])
    print('current page num --> %d' % cur_page)
    return cur_page


def find_imgs(page_url):
    html = url_open(page_url).decode('utf-8')

    p = r'<img src="([^"]+\.jpg)"'

    img_adds = re.findall(p, html)

    img_adds = map(lambda img_add: 'http:' + img_add if img_add.startswith('//') else img_add, img_adds)
    img_adds = list(img_adds)

    return img_adds


def save_imgs(img_adds):
    for img_add in img_adds:
        filename = os.path.basename(img_add)
        with open(filename, 'wb') as f:
            img = url_open(img_add)
            f.write(img)
            print('save img --> %s' % filename)


def download_mm(folder='OOXX', pages=10):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx'
    page_num = get_page(url)

    for i in range(pages):
        page_num -= i
        page_url = url + '/page-' + str(page_num) + '#comments'
        img_adds = find_imgs(page_url)
        save_imgs(img_adds)


if __name__ == '__main__':
    download_mm(pages=1)
