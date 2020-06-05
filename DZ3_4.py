list1 = [2,5,4,7]
list2 = [1,2,5,4]
list3 = []
for i in range(0, len(list1)):
    for value in list2:
        if list1[i] == value:
            list3.append(list1[i])
print(list3)
