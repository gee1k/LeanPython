#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'


def fibs(m=20):
    n1 = 0
    n2 = 1

    while True:
        n1, n2 = n2, n1 + n2
        if n1 > m:
            raise StopIteration
        yield n1


for i in fibs():
    print(i)
