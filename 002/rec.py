#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(key, value)

    def get_area(self):
        return self.width * self.height


r1 = Rectangle(4, 5)
print(r1.get_area())

r1.square = 10
print(r1.width)
print(r1.height)
print(r1.get_area())


class MyDecriptor:
    def __get__(self, instance, owner):
        print('geting...', self, instance, owner)


class T:
    x = MyDecriptor()