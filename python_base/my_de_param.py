import functools
def log(name):
    def dec(func):
        @functools.wraps(func)
        def middel(*args , **kw):
            print(name + '*' * 50)
            func(*args , **kw)
            print(name + '*' * 50)
        return middel
    return dec




@log('sqy')
def mySum(a , b):
    print(a + b)

mySum(5 , 6)

