class Roman(int):
    def __init__(self,number,type):
        self.num = number
        self.type = type
        #print(self.num,self.type)

    def to_dec(self,roman2):
        self.num = int(self.num,self.type)



    def __add__(self,roman2):
        res = self.num + roman2.num

        return res

    def __sub__(self,roman2):
        res = self.num - roman2.num

        return res

    def __mul__(self,roman2):
        res = self.num * roman2.num
        return res

    def __truediv__(self,roman2):
        res = self.num // roman2.num
        return res

    def __mod__(self,roman2):
        res = self.num % roman2.num
        return res

    def __neg__(self):
        res =-self.num
        return res

    def __lt__(self,roman2):
        if(self.num < roman2.num):
            return 'First integer is less than second'
        else:
            return 'First integer is not less than second'
    def __gt__(self,roman2):
        if(self.num > roman2.num):
            return True
        else:
            return False
    def __eq__(self, roman2):
        if (self.num == roman2.num):
            return True
        else:
            return False

    def __ne__(self, roman2):
        if (self.num != roman2.num):
            return True
        else:
            return False

    def __le__(self, roman2):
        if (roman.num <= roman2.num):
            return True
        else:
            return False
    def __ge__(self, roman2):
        if (roman.num >= roman2.num):
            return True
        else:
            return False

    def numToRoman(self,num):
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous = ["","M","MM","MMM","MMMM"]

        t = thous[self.num // 1000]
        h = hunds[self.num // 100 % 10]
        te = tens[self.num // 10 % 10]
        o =  ones[self.num % 10]

        return t+h+te+o

number = input('Input number: ')
number2 = input('Input second number: ')

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
roman2 = Roman(number2,type_number)
roman.to_dec(number)
roman2.to_dec(number2)
res_add = roman.__add__(roman2)
res_sub = roman.__sub__(roman2)
res_mul = roman.__mul__(roman2)
res_div = roman.__truediv__(roman2)
res_mod = roman.__mod__(roman2)
res_neg = roman.__neg__()
res_lt = roman.__lt__(roman2)
res_gt = roman.__gt__(roman2)
res_eq = roman.__eq__(roman2)
res_ne = roman.__ne__(roman2)
res_le = roman.__le__(roman2)
res_ge = roman.__ge__(roman2)




print('Res Add: '+ str(roman + roman2)+'in roman: ' + str(roman.numToRoman(res_add)))
print('Res_Sub: '+ str(roman - roman2)+'in roman: ' + str(roman.numToRoman(res_sub)))
print('Res mul: '+ str(roman * roman2)+'in roman: ' + str(roman.numToRoman(res_mul)))
print('Res div: '+ str(roman / roman2)+'in roman: ' + str(roman.numToRoman(res_div)))
print('Res modul:' + str(res_mod))
print('Res A neg:' + str(res_neg))
print('less than number: '+ str(roman.num < roman2.num))
print('more than number: '+ str(roman.num > roman2.num))
print('equal: '+ str(roman.num == roman2.num))
print('not equal: ' + str(roman.num != roman2.num))
print('<= '+ str(roman.num <= roman2.num))
print('>= '+ str(roman.num >= roman2.num))
