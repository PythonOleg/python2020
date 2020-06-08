number = int(input('Input number: '))
while number <= 1000:
    print('bin','\t', 'oct','\t', 'dec','\t', 'hex')
    print(bin(number),'\t',oct(number), '\t', number, '\t','\t',hex(number))
    number = int(input('Input number: '))
else:
    print('Number is more than 1000')
