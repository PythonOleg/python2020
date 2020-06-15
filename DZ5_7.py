def func7(n):
    if n == 0:
        return n
    else:
        return n + func7(n - 1)


n = int(input('Input integer: '))
recurs = func7(n)
print(recurs)
