from abc import ABCMeta, abstractmethod
import six
import io

@six.add_metaclass(ABCMeta)
class IStream():
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

    def my_print(self):
        print('nihao')

# a = IStream()

class MyStream(IStream):
    def read(self, maxbytes=-1):
        pass
    def write(self, data):
        pass

stream = MyStream()
stream.my_print()

class B(object):
    pass
s = B()

# IStream.register(B)


IStream.register(io.IOBase)
f = open('./myPool.py')

isinstance(f, io.IOBase)


if isinstance(f, IStream):
    print(1)
else:
    print(2)




