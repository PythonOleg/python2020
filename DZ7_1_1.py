class Roman(int):
    def __init__(self,number,type):
        self.num = number
        self.type = type
        
    def toDec(self):
        if self.type == 2:
            n = int(self.num,2)
            res = self.numToRoman(n)
            return res

        if self.type == 8:
            n = int(self.num,8)
            res = self.numToRoman(n)
            return res

        if self.type == 16:
            n = int(self.num,16)
            res = self.numToRoman(n)
            return res

        if self.type == 10:
            n = int(self.num,10)
            res = self.numToRoman(n)
            return res

    def numToRoman(self,n):
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous = ["","M","MM","MMM","MMMM"]
    
        t = thous[n // 1000]
        h = hunds[n // 100 % 10]
        te = tens[n // 10 % 10]
        o =  ones[n % 10]
     
        return t+h+te+o
       
number = input('Input number: ')


if number.startswith('0b'):
    type_number = 2
elif number.startswith('0o'):
    type_number = 8
elif number.startswith('0x'):
    type_number = 16
elif number.isdigit:
    type_number = 10
else:
    print('It is not a number!')

roman = Roman(number,type_number)
result = roman.toDec()

print('Number was printed in {} system '.format(type_number) + 'In roman number is: '+ result)
