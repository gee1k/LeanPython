#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Svend'

print(ord('A'))

print(ord('中'))

print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')

# bytes
print(b'ABC')

# 编码为指定的bytes
print('ABC'.encode('ascii'))

print('中文'.encode('utf-8'))

# 把bytes变为str
print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


# length
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# %
print('%5d-%02d' % (3, 1))
print('Age: %d. Gender: %s' % (25, True))