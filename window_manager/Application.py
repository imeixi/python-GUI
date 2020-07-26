#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = 'Hello world\n(click me)'
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')

        # 修改widget参数方法一，初始化时赋值
        self.quit = tk.Button(self, text='QUIT', fg='red', command=self.master.destroy)
        # 方法二：直接修改属性值
        self.quit['fg'] = 'blue'
        # 方法三，使用config方法赋值
        self.quit.config(fg='yellow', bg='gray')
        self.quit.pack(side='bottom', expand=0)


    def say_hi(self):
        print('hi there, everyone!')
        print(self.hi_there.config('fg'))


root = tk.Tk()
app = Application(master=root)
app.mainloop()