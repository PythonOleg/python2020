import os,sys

class MyOpen():

    def __init__(self,address,prava,code='utf-8'):
        self.address = address
        self.prava = prava
        self.code = code
        self.cursor_position = 0
        self.line = ''

    def write(self):
        string = input('Input line to be writed: ')
        line = file.write(string)
        return line
    def writelines(self):
        n = int(input('how many lines must be writed? '))
        for i in range(n):
            line = input('Input line {}: '.format(i+1))
            file.write(line)
        return line
    def read(self):
        file.read(self)
        file.close(self,file_address, prava,code)
    def readline(self):
        file.readline(self)

    def readlines(self):
        file.readlines(self)
    def read_write(self):
        file.read(self)
        line = input('Input line to be writed: ')
        file.write(line)
    def seek(self,line):
        if self.prava == 'a':
            return None
        else:
            self.cursor_position = input('Input cursor position: ')
            return self.cursor_position

    def tell(self,line):
         print(line[self.cursor_position])

    def close(self,file_address, prava,code):
        file.close(self,file_address, prava,code)

file_address = input('Input file address: ')
flags = input('Input file flag: ')
file = MyOpen(file_address,flags, code='utf-8')

if flags == 'w':
   file.write()
if flags == 'a':
   file.write(file_address,os.O_APPEND)
if flags == 'ra':
   file.read_write(os.O_RDONLY | os.O_APPEND)
if flags == 'rw':
   file.read_write(file_address,os.O_RDWR)
if flags == 'b':
   file.write(file_address,os.O_BINARY)
if flags == 'r':
   file.read(file_address,os.O_RDONLY)
file.close()









