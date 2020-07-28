import os
#####################################Клас Myopen########################################################################
class MyOpen:
    def __init__(self):
        self.address = address

    def write(self):
        with open(address,'w') as file:
            my_string = input('Input string: ')
            file.write(my_string+'\n')
            file.close()

    def writelines(self):
        n = int(input('Now many line you want to write? '))
        with open(address,'w') as file:
            for line in range(n):
                string_line = input('Input line: ')
                file.writelines(string_line)
            file.close()

    def read(address):
        with open(address,'r') as file:
            n = int(input('How many symbols must be readed? '))
            content = file.read(n)
            print(content)
            file.close()

    def readlines(self):
        with open(address,'r') as file:
            content = file.readline()
            print(content)
            file.close()

    def readlines(self):
        with open(address,'r') as file:
            line = file.readline()
            print(line)

    def seek(self):
        with open(address) as file:
            cursor = int(input('Input cursor position: '))
            file.seek(cursor)
            return cursor

    def tell(self):
        print('Cursor position is ' + str(cursor))
######################################Основна частина програми##########################################################

address = input('Input file address: ')
n = 0
cursor = 0
file = MyOpen
file.write(address)
file.read(address)
file.writelines(address)
file.readlines(address)
cursor = file.seek(address)
file.tell(cursor)
