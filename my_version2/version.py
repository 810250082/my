# -*- coding: utf-8 -*-
"""
版本管理模块
"""
from flask import request
from functools import wraps
import os
from importlib import import_module
from my_version2.api_version.version_base import BaseVersion
from my_version2.api_version import all_subclasses
import logging
import re


def version(method):
    @wraps(method)
    def swap(*args, **kwargs):
        ver = request.args.get('api_version', '')
        if ver:
            # 版本号 必须以小写v开头，三个数字以'.'号连接，例如 v0.9.8, 数字大小不做限制，
            # 从左到右，第一个数字代表大版本号，第二个数字中版本号，第三个数字为小版本号, 每次发版，版本号往上加
            if not re.match(r'v\d+\.\d+\.\d+', ver):
                return 'api_version error'
            endpoint = request.url_rule.endpoint
            blueprint, func = endpoint.split('.')
            if blueprint and func:
                # 构造一个版本管理器
                version_manager = VersionManager(blueprint, func, ver)
                # 获取该蓝图下第一个小于等于给定版本号的版本类
                cls = version_manager.select_version()
                if cls:
                    f = getattr(cls(), func, None)
                    if f:
                        return f(*args, **kwargs)

        return method(*args, **kwargs)
    return swap


class VersionManager(object):
    """
    版本管理器
    版本号
        必须以小写v开头，三个数字以'.'号连接，例如 v0.9.8, 数字大小不做限制，
        从左到右，第一个数字代表大版本号，第二个数字中版本号，第三个数字为小版本号, 每次发版，版本号往上加

    版本模块目录结构
         版本包名  存放所有版本类的包， 可有类属性 version_module  指定
            |
            |---- __init__.py
            |---- version_base.py   所有的版本类都继承它，存放所有版本类的公共部分
            |---- 用蓝图名称建的包
            |          |
            |          |----- __init__.py
            |          |----- 大版本 1.py
            |          |           |----- class V1V0V1  版本类 数字以三个"V"分割 ，第一个数字要和大版本数字一致
            |          |           |               |———— 要迭代的方法
            |          |           |               |———— 要迭代的方法
            |          |           |                .......
            |          |           |
            |          |           |----- class V1V0V2  版本类
            |          |           |----- class V1V0V3  版本类
            |          |           .......
            |          |
            |          |----- 大版本 2.py
            |          |           |----- class V2V0V1  版本类
            |          |           |----- class V2V0V2  版本类
            |          |           |----- class V2V0V3  版本类
            |          |----- 大版本 3.py
            |          .........
            |
            .........
    """
    # 版本模块名
    version_module = 'api_version'

    def __init__(self, blueprint=None, func=None, version=None):
        """
        :param blueprint:   定义蓝图时的名称
        :param func:        要版本迭代的接口方法名称
        :param version:     版本格式类似于 v0.0.1， 否则会解析错误
        """
        self.blueprint = blueprint
        self.func = func
        self.version = version

    def select_version(self):
        """
        选择一个合适的版本类
        1、获取该蓝图最后一级类，获取所有的父类
        2、倒叙循环每一个类，生成每个类的版本号，同时与给定的版本号作比较，小于等于该版本号，则返回该类，如果没有找到，则返回False
        :return:    匹配成功则返回   合适的类
                    匹配失败        False
        """

        # 获取该蓝图最后一级类
        # last_cls = all_subclasses.get(self.blueprint, []).pop()
        last_cls = all_subclasses.get(self.blueprint, []).pop()
        if not last_cls:
            return None
        # 获取最后一级版本类后，倒叙遍历其所有的父类
        select_cls = None
        for item in last_cls.__mro__:
            if issubclass(item, BaseVersion) and item is not BaseVersion:
                # 将类名转化为版本号，与给定的版本号进行比较，找到第一个小于等于它的版本类
                cls_str = '{}.{}'.format(item.__module__, item.__name__)
                cls_path_list = cls_str.split('.')
                index = -len(cls_path_list[-1])
                version_str = self.format_version(cls_str[index:])
                if self.version_cmp(self.version.lstrip('v'), version_str.lstrip('v')) in [0, 1]:
                    select_cls = item
                    break
        return select_cls

    def last_level_cls(self):
        """
        获取该蓝图最后一版本最后一级的类
        :return:    成功： 最后一级的类
                    失败： None
        """
        # 获取所有的大版本文件列表
        try:
            blueprint_module = import_module("{}.{}".format(self.version_module, self.blueprint))
        except ImportError:
            logging.error('%s blueprint import error', "{}.{}".format(self.version_module, self.blueprint))
            # 如果导入错误，让其执行默认视图
            return None
        # 获取蓝图的绝对路径
        blueprint_path = os.path.dirname(blueprint_module.__file__)
        # 或蓝图内所有的大版本, 筛选所有以v开头，并且以.py 结尾的文件名，然后去重
        all_big_visions = set([os.path.splitext(x)[0].strip() for x in os.listdir(blueprint_path)
                           if x.startswith('v') and x.endswith('.py')])
        if not all_big_visions:
            return None
        # 倒叙，从最后一个大版本开始查找
        all_big_visions = sorted(all_big_visions, key=lambda x: int(x.replace('v', '')), reverse=True)
        last_cls = None
        for item in all_big_visions:
            # 导入模块
            vision_module = import_module("{}.{}.{}".format(self.version_module, self.blueprint, item))
            # 获取大版本中所有符合条件的类
            clses = [cls for cls in dir(vision_module)
                     if cls.startswith('V') and issubclass(getattr(vision_module, cls), BaseVersion)
                     and (getattr(vision_module, cls)).__module__.split('.')[-1] == item]
            if not clses:
                continue
            # 将所有的类按照版本号正序排列
            clses = sorted(clses, cmp=lambda x, y: self.version_cmp(self.format_version(x), self.format_version(y)))
            # 获取最大的那个版本类
            last_cls = clses.pop()
            last_cls = getattr(vision_module, last_cls)
            break
        return last_cls

    def version_cmp(self, first_version, second_version):
        """
        比较两个版本号，两个版本号必须格式一致
        :param first_version:   第一个版本号  格式类似 0.0.1
        :param second_version:  第二个版本号  格式类似 0.0.1
        :return: 1>2  返回1 ， 1=2 返回0， 1<2 返回-1
        """
        first_version_list = first_version.split(".")
        second_version_list = second_version.split(".")
        for i in range(0, len(second_version_list)):
            if int(second_version_list[i]) > int(first_version_list[i]):
                return -1
            elif int(second_version_list[i]) < int(first_version_list[i]):
                return 1
        return 0

    def format_version(self, version_str):
        """
        将模块.类名, 或类名  转化为版本号  v0.0.1形式
        :return:
        """
        return version_str.replace('V', '.').replace('..', '.').lstrip('.')


class VersionManager2(VersionManager):
    def last_level_cls(self):
        pass


if __name__ == "__main__":
    version_manager = VersionManager('user', 'info', 'v0.0.1')
    cls = version_manager.select_version()
    f = getattr(cls, 'info', None)
    b = 1

