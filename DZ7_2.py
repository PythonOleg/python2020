class Iter:
    def __init__(self,first,second,step):
        
        self.slice_data = data[first:second:step]
        self.counter = -1
        self.max = len(self.slice_data)-1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1    
        if self.counter < self.max:
            return self.slice_data[self.counter]
        else:
            raise StopIteration
        

data = input('Input data')
first = int(input('Input first integer: '))
second = int(input('Input second integer: '))
step = int(input("Input step: "))

iterator = Iter(first,second,step)
for i in iterator:
    print(i,end=' ')