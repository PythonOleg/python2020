num = int(input('Input number: '))
sum = 0
while num > 0:
    if num % 2 == 0:
        sum += num
    num -= 1
print(sum)
