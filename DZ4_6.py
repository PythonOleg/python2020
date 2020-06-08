str1 = input('Input string:')
if str1.isdigit() == True:
    print('String consist from digits')
elif str1.isalpha() == True:
    print('String consist from letters')
else:
    print(type(str1))

