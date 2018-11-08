# -*-coding:utf-8 -*-
from voluptuous import Schema, Required, Invalid


def convert_up(value):
    if isinstance(value, str):
        return value.upper()
    raise Invalid('无效的名字')


s = Schema({
    Required('sqy'): str,
    'page': int,
    'page_size': int,
    'name': convert_up
}, extra=False)

# print(s({'sqy': 'ghn', 'page': '10', 'page_size': 10}))
# print(s({}))
# print(s({'sqy': 'ghn', 'page': '10', 'my_page': 10}))
print(s({'sqy': 'ghn', 'page': 10, 'page_size': 10, 'name':'ghn'}))