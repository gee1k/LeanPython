#!/usr/bin/python3
# _*_ coding:utf-8 _*_

__author__ = 'Svend'

import tkinter as tk


class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.hi_there = tk.Button(frame, text='打招呼', fg='white', bg='black', command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        print('hi......')


root = tk.Tk()
app = APP(root)

root.mainloop()