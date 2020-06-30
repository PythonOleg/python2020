
class MyRange:
    def __init__(self,number):
        self.num = number
        self.i = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < num:
           self.i += 1
           return self.i
           
        if self.i == num:
            raise StopIteration
       
    

num = int(input('Input number: '))
iterator = MyRange(num)
for i in iterator:
    print(i)
