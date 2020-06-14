def func4(d1):
    list1 = list(d1.items())#Переводжу у строку
    list1.reverse()#Використовую метод reverse
    d2 = dict(list1)#Перетворюю на словник
    return d2

d1 = {'one':1, 'two':2,'three': 3}
d2 = {}
print(d1)
d2  = func4(d1)
print(d2,type(d2))#type(d2) - Перевіряю що словник
