def func2(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                list3.append(list1[i])
    return list3

list1 = [2,3,5,6,8]
list2 = [3,56,76,8]
list3 = []
list3 = func2(list1,list2)
print(list3)
