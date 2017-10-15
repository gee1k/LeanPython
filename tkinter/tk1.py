#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import tkinter as tk

app = tk.Tk()
app.title('TK Demo')

theLabel = tk.Label(app, text='tkinter')
theLabel.pack()

app.mainloop()