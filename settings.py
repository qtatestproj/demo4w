# -*- coding: utf-8 -*-
'''测试项目配置文件
'''
#2019/03/22 QTAF自动生成

import os

PROJECT_NAME = "demo4w"
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_MODE = "standard"
INSTALLED_APPS = []

DRUN_TASK_ENTRY = 'task'
try:
    from drun_settings import *
except ImportError:
    pass
