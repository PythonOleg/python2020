list1 = [8,2,54,5,9,12,34]
min = list1[0]
max = list1[0]
for ind in range(0,len(list1)):
        if list1[ind] < min:
            min = list1[ind]
        elif list1[ind] > max:
            max = list1[ind]
print('max: ' + str(max))
print('min: ' + str(min))
