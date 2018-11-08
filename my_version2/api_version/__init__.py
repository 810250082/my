# -*- coding=utf-8 -*-
"""
每添加一个蓝图模块，在这里添加一个
"""
from my_version2.api_version.version_base import BaseVersion
from . import user
from . import money


# 在上面添加模块
# 版本基类所有的子类
all_subclasses = BaseVersion.all_subclasses_fun()
