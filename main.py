#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tkinter as tk  # 使用 tkinter 前需要先导入
from fuction.basic import save_screen_cap_file

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('800x500')

# 第4步，在图形界面上设定标签

# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# label = tk.Label(window, text='hello, world!', bg='green', font=('Arial', 12), width=30, height=2)

var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
label = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=100, height=10)
# Label内容content区域放置位置，自动调节尺寸
# 放置label的方法有：1）l.pack(); 2)l.place();
label.pack()


# 第5步，放置标签
button_connect = tk.Button(window, text='保存截图到本地', font=('Arial', 12), width=10, height=1,
                           command=save_screen_cap_file())
button_connect.pack()


# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
