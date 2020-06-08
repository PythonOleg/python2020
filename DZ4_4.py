str1 = input('First string:')
str2 = input('Second string:')
list1 = []
list1.extend(str2)
center = round(len(str2)/2)
list1.insert(center,str1)
print(list1)
