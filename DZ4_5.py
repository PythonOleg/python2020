str1 = input('Input string: ').strip()
for i in range(0,len(str1)):
    if str1[i].islower() == True:
       print(str1[i].upper(),end='')
    elif str1[i].isupper() == True:
        print(str1[i].lower(),end='')

