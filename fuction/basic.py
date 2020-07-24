#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

from constant import AdbCommand
from constant import Default
from service.api import execute_command


def save_screen_cap_file():
        execute_command(AdbCommand.ADB_SCREEN_CAP, sd_file=Default.SD_FILE)
        execute_command(AdbCommand.ADB_PULL_FILE, sd_file=Default.SD_FILE, local_file=Default.LOCAL_FILE)



