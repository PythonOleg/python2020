import os,sys

class MyOpen():

    def __init__(self,address,prava,code):
        self.address = address
        self.prava = prava
        self.code = code
        self.cursor_position = 0
        self.line = ''

    def prava(self):
        if self.prava == 'r':
            self.prava = os.O_RDONLY
        if self.prava == 'w':
            self.prava = (os.O_WRONLY | os.O_CREAT)
        if self.prava == 'a':
            self.prava = os.O_APPEND
        if self.prava == 'ra':
            self.prava = (os.O_RDONLY | os.O_APPEND)
        if self.prava == 'rw':
            self.prava = os.O_RDWR
        if self.prava == 'b':
            self.prava = os.O_BINARY

    def write(self):
        string = input('Input line to be writed: ')
        line = file.write()
        return line
    def writelines(self):
        n = int(input('how many lines must be writed? '))
        for i in range(n):
            line = input('Input line {}: '.format(i+1))
            file.write(file_address,line)
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

file_address = input('Input file name: ')
flags = input('Input file right: ')
file = MyOpen(file_address,flags, code='utf-8')









