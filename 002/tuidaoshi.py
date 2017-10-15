#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

# 列表推导式
a = [i for i in range(100) if not (i % 2) and i % 3]
print(a)

# 字典推导式
b = {i: i % 2 == 0 for i in range(10)}
print(b)

# 集合推导式
c = {i for i in [1, 2, 3, 4, 5, 6, 5, 4, 3, 2]}
print(c)

# 生成器推导式
g = (i for i in range(10))
for i in g:
    print(i, end='--')

sum(i for i in range(100) if i % 2)