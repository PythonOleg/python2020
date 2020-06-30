class change_string:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def func1(self,a,b):
        s = '{0}''/''{1}'.format(self.a,self.b)
        return s

    def func2(self,a,b):
        s = '{0}''@''{1}'.format(self.a,self.b)
        return s


a = 'mail'
b = 'gmail'
change = change_string(a,b)
res = change.func1(a,b)
res2 = change.func2(a,b)
print(res)
print(res2)
