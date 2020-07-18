#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from constant import AdbCommand

# 设备编号
serial_list = []
# 包名
package_name = 'com.jingdong.app.mall'

sd_file = '/sdcard/sc.png'
local_file = os.path.join(os.path.expandvars('$HOME'), '/Desktop/')


def execute_command(cmd, **kwargs):
    if not serial_list:
        init_serial_list()
    if serial_list:
        # 替换命令行参数
        for key, value in kwargs.items():
            cmd = cmd.replace('{' + key + '}', value)

        # 替换 serial 参数
        for serial_name in serial_list:
            cmd = cmd.replace('{}', serial_name)
            result = os.popen(cmd).read()
            # res = os.system(cmd)
            return result
    else:
        print('当前没有连接设备，请检查。。。')


def init_serial_list():
    global serial_list
    cmd = AdbCommand.ADB_DEVICE
    result = os.popen(cmd).read()
    for row in result.split('\n')[1:]:
        serial_name = row.split('	')[0]
        if serial_name:
            serial_list.append(serial_name)


def save_screen_cap_file():
    execute_command(AdbCommand.ADB_SCREEN_CAP, sd_file=sd_file)
    execute_command(AdbCommand.ADB_PULL_FILE, sd_file=sd_file, local_file=local_file)


