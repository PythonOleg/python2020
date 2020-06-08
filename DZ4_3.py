#Паліндром
# Використовую Slice
str1 = input('Input first string: ')
str2 = input('Input second string:')
if str1[::1] == str2[::-1]:
    print('Strings are palyndromes')
else:
    print('Strings are not palyndromes')
