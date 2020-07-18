#!/usr/bin/env python
# -*- coding:utf-8 -*-


class AdbCommand(object):

    # 基本命令
    ADB_VERSION = 'adb version'
    ADB_START_SERVER = 'adb start-server'
    ADB_KILL_SERVER = 'adb kill-server'
    ADB_DEVICE = 'adb devices'

    # 应用管理
    ADB_PM_LIST = 'adb -s {} shell pm list packages'
    ADB_PM_LIST_SYS = 'adb -s {} shell pm list packages -s'
    ADB_PM_LIST_THIRD = 'adb -s {} shell pm list packages -3'
    ADB_PM_LIST_JD = 'adb -s {} shell pm list packages jingdong'

    # 安装应用
    ADB_INSTALL_APK = 'adb -s {} shell install -r {apk}'
    ADB_UNINSTALL_APK = 'adb -s {} shell uninstall {apk}'

    # 清除应用数据
    ADB_CLEAR_PACKAGE = 'adb -s {} shell pm clear {package_name}'

    # 查看前台 Activity
    ADB_CHECK_CURRENT_ACTIVITY = 'adb -s {} shell dumpsys activity activities | grep mFocusedActivity'

    # 查看正在运行的Service
    ADB_CHECK_CURRENT_SERVICE = 'adb -s {} shell dumpsys activity service | {package_name}'

    # 查看应用详细信息
    ADB_CHECK_APP_INFO = 'adb -s {} shell dumpsys package {package-name}'

    # 模拟按键
    ADB_KEY_POWER = 'adb -s {} shell input keyevent 26'
    ADB_KEY_HOME = 'adb -s {} shell input keyevent 3'
    ADB_KEY_MENU = 'adb -s {} shell input keyevent 82'
    ADB_KEY_BACK = 'adb -s {} shell input keyevent 4'
    ADB_KEY_VOL_ADD = 'adb -s {} shell input keyevent 24'
    ADB_KEY_VOL_SUBTRACT = 'adb -s {} shell input keyevent 25'
    ADB_KEY_INOUT_TEXT = 'adb -s {} shell input text {text}'
    ADB_KEY_TAP_COORDINATE = 'adb -s {} shell input tap {x} {y}'
    ADB_KEY_SWIPE_BEGIN_END = 'adb -s {} shell swipe {x1} {y1} {x2} {y2}'

    # 屏幕截图
    ADB_SCREEN_CAP = 'adb -s {} shell screencap -p {sd_file}'   # sc_cap_file = /sdcard/sc.png
    ADB_SCREEN_RECORD = 'adb -s {} shell screenrecord {sd_file}'   # sc_record_file = /sdcard/sc.png

    # 推送、拉取文件
    ADB_PULL_FILE = 'adb -s {} pull {sd_file} {local_file}'
    ADB_PUSH_FILE = 'adb -s {} push {local_file} {sd_file}'



