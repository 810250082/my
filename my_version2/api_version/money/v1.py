# -*- coding: utf-8 -*-
from v0 import V0V1V2


class V1V0V1(V0V1V2):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V1V0V2(V1V0V1):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V1V1V1(V1V0V2):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V1V1V2(V1V1V1):
    def info(self, *args, **kwargs):
        return type(self).__name__


if __name__ == "__main__":
    a = dir()
    b = 1
