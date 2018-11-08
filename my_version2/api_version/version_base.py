# -*- coding: utf-8 -*-
"""
版本基类
"""
from collections import defaultdict, OrderedDict


class BaseVersion(object):
    """
    版本基类，存放各种版本公共部分
    """
    all_subclasses ={}

    @classmethod
    def all_subclasses_fun(cls):
        """
        获取该类的所有子类
        :return:
        """
        if not cls.all_subclasses:
            def subclass(cls, order_subs=OrderedDict(), blue_subs=defaultdict(list)):
                """
                获取一个类的所有子类，并且按照蓝图名字进行分组，每一分组，子类按照继承关系，顺序排列
                :param cls:         指定的基类
                :param order_subs:  为了排除加载同一个基类， 引入顺序字典
                :param blue_subs:   存放结果
                :return:
                """
                for item in cls.__subclasses__():
                    # 获取蓝图
                    blue = item.__module__.split('.')[-2].strip()
                    order_key = blue + '_' + item.__name__
                    # 排除相同的类
                    if order_key not in order_subs:
                        blue = item.__module__.split('.')[-2].strip()
                        order_subs[order_key] = item
                        blue_subs[blue].append(item)
                        subclass(item, order_subs, blue_subs)

                return blue_subs
            cls.all_subclasses = subclass(cls)

        return cls.all_subclasses


if __name__ == "__main__":
    from user.v0 import *
    from user.v1 import *
    from money.v0 import *
    from money.v1 import *
    aa = BaseVersion.all_subclasses_fun()
    bb = 1