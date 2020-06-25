def dec1(func9):
    def wrapper(a,b):
        rez = func9(a,b)
        return rez
    return wrapper

@dec1
def func9(a,b):
    x = b / a
    return x

a = int(input('Input a: '))
b = int(input('Input b: '))
if(b == 0):
    print('Error')
    print('NAN')
else:
    x = func9(a,b)
    print("Корень рівняння = " + str(x))
