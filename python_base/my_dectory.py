def log(func):
    def middle(*args , **kw):
        print('-' * 50)
        func(*args , **kw)
        print('-' * 50)
    return middle



@log
def getSum(a, b):
    print(a + b)


getSum(1 , 2)

#log(getSum)(1,2)