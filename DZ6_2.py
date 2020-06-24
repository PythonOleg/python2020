def dec2(func9):
    def wrapper(a,b):
        print('The first argument is'+str(a))
        print('The second argument is'+str(b))
        rez = func9(a,b)
        return rez
        
    return wrapper
    
@dec2
def func9(a,b):
    x = b / a
    return x

a = int(input('input a: '))
b =int(input('input b: '))
res = func9(a,b)
print('Result is:'+str(res))
