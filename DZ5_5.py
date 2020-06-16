def func5(list1):
    for i in range(len(list1)):
        value = list1.count(list1[i])
        d1.setdefault(list1[i]) 
        d1[list1[i]] = value
    return d1


list1 = ['q','w','q','w','q','s','s','s','r']
d1 = {}
value = 0
d1 = func5(list1)
print(d1)