#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False


def hit_me():
    global on_hit
    if not on_hit:
        on_hit = True
        res = os.popen('adb devices')
        var.set(res.read())
    else:
        on_hit = False
        var.set('')