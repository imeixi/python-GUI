#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tkinter import Frame, Entry, StringVar
import tkinter as tk


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.entry = Entry()
        self.entry.pack()

        self.constants = StringVar()
        self.constants.set("this is a variable")

        self.entry['textvariable'] = self.constants

        self.entry.bind('<Key-Return>', self.print_constants)

    def print_constants(self, event):
        print('Hi,constants of entry is now ---->', self.constants.get())


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.master.title('My Do-Nothing Applicate')
    app.master.maxsize(1000, 400)
    root.mainloop()
