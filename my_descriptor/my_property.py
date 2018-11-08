class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if self.fget is not None:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is not None:
            self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is not None:
            self.fdel(instance)

    def getter(self, fn):
        self.fget = fn

    def setter(self, fn):
        self.fset = fn

    def deler(self, fn):
        self.fdel = fn

    # def __call__(self, a):
    #     return a


class Spam(object):
    def __init__(self, val):
        self.__val = val

    @Property
    def val(self):
        return self.__val

    @val.setter
    def set_val(self, value):
        self.__val = value

# pp = Property(lambda x: x.__val)
# ss = Spam(3)
# bb = pp(ss)

# @Property
# def ss(a):
#     return  a
#
# b = ss(1)

s = Spam(4)

print(s.val)

s.val = 3

print(s.val)