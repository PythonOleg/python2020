list1 = []
list2 = []
n = input('Input number: ')
while n != 'stop':
    if int(n) > 0:
        list1.append(n)
    if int(n) < 0:
        list2.append(n)
    n = input('Input number: ')
if n == 'stop':
    list1.sort()
    list2.sort()
    list2.reverse()
list1.extend(list2)
print(list1)
