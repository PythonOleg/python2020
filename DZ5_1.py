def func1(list1,n):
    min = 0
    while n > 0:
        number = max(list1)#отримую найбільше значчення
        list2.append(number)#додаю до нового списку
        del_num = list1.index(number)#отримую індекс найбільшого значення
        list1[del_num] = min #значення за вказаним індексом обнуляю (можна привязати до значення min) для вичислення нового на найбільшого значення
        n -= 1
    return list2

list1 = [1,5,7,5,8,9,4,89,12,45,67,78,89,23]
list2 = []
n = int(input('Input how many the biggest meanings I should find: '))
list2 = func1(list1,n)
print(list2)

