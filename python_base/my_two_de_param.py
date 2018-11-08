import functools , time



def sign(name):
    def dec(func):
        def swap(*args , **kw):
            print('author: %s' % name)
            print('')
            func(*args , **kw)
        return swap
    return dec

def show(func):
    def middle(*args , **kw):
        startTime = time.time()
        print('now is %s' % startTime)
        func(*args , **kw)
        endTime = time.time()
        print('run is %s' % (endTime - startTime))
    return middle

def log(name):
    def dec(func):
        @functools.wraps(func)
        def middel(*args , **kw):
            print(name + '*' * 50)
            func(*args , **kw)
            print(name + '*' * 50)
        return middel
    return dec


@sign('shitou')
@show
@log('sqy')
def mySum(a , b):
    print(a + b)

mySum(5 , 6)

#log(getSum)(1,2)
#log('sqy')(mySum)(5 , 6)
#show(log('sqy')(mySum))(5 , 6)
