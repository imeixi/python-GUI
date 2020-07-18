#!/usr/bin/env python
# -*- coding:utf-8 -*-

from service import *

if __name__ == '__main__':
    print(os.environ['HOME'])
    print(os.path.expandvars('$HOME'))
    print(os.path.expanduser('~'))
