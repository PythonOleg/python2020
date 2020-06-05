list1 = [11,3,11,3,11,12,3,11,11,12,14]
ind = 0
list1.sort()
print(list1)
while ind < len(list1)-1:
    for value in list1:
        if value == list1[ind]:
            list1.remove(list1[ind])
    ind += 1
print(list1)
