def cache(func):
    memo = {}
    def wrapper(a):
        if a in memo:
            return memo[a]
        else:
            s = func(a)
            memo[a] = s
        print('cache is' + str(memo[a]))
        return memo[a]
    return wrapper

@cache
def func(a):
    a = a + 2
    return a

a = int(input('Input a: '))
s = func(a)
print('func is '+ str(s))
