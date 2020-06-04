num = int(input('Input number of rows: '))
x = 0
y = 0
count = num
while x < num:
    x += 1
    while y < count:
        y += 1
        print(y, end=" ")
    y = 0
    count -= 1
    print()






