def decorator(func):
    def wrapper(s):
        text_b = func(s)
        text_i = func(s)
        text_u = func(s)
        
        text_in_b = ('<b> ' + str(text_b) + ' </b>')
        text_in_i = ('<i> ' + str(text_i) + ' </i>')
        text_in_u = ('<u> ' + str(text_u) + ' </u>')
        print(text_in_b)
        print(text_in_i)
        print(text_in_u)
    return wrapper


@decorator
def func(s):
    s = 'Its a text from function'
    return s

s = 0
func(s)
