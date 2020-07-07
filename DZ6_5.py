def repeat(r = 1):
    def _repeat(func): 
        def wrapper(message):
            for i in range(r):
               func(message)
            return func
        return wrapper
    return _repeat



n = 0
try:
    n = int(input('input parametr: '))
except BaseException:
    n = 1 

@repeat(n)
def func(message):
    print(message)


message = 'Hello'
d = func(message)
print(d)
