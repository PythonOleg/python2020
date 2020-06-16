def func9(a,b):
    x = b / a
    return x

a = int(input('Input a: '))
b = int(input('Input b: '))
kor = func9(a,b)
print('Коренем цього рівняння є число: '+ str(kor))