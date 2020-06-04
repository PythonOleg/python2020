list1 = [2,3,4,7,6,9,8,11]
for value in list1:
    if value % 2 == 0:
        value = 0
    elif value % 2 == 1:
        value = value * value
    print(value, end=' ')
