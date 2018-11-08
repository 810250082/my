# -*- coding: utf-8 -*-
from my_version2.api_version.version_base import BaseVersion


class V0V0V1(BaseVersion):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V0V0V2(V0V0V1):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V0V1V1(V0V0V2):
    def info(self, *args, **kwargs):
        return type(self).__name__


class V0V1V2(V0V1V1):
    def info(self, *args, **kwargs):
        return type(self).__name__



