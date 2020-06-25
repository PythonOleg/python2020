def dec1(func1):
    def wrapper1(s):
        text_b = func1(s)
        text_in_b = ('<b> ' + str(text_b) + ' </b>')
        print(text_in_b)
    return wrapper1

def dec2(func2):
    def wrapper2(s):
        text_i = func2(s)
        text_in_i = ('<i> ' + str(text_i) + ' </i>')
        print(text_in_i)
    return wrapper2

def dec3(func3):
    def wrapper3(s):
        text_u = func3(s)
        text_in_u = ('<u> ' + str(text_u) + ' </u>')
        print(text_in_u)
    return wrapper3

@dec1
@dec2
@dec3
def func(s):
    s = 'Its a text from function'
    return s


s = 0
func(s)
