def fibon(n):
    fibon_list = list()
    if n == 0:
        return None
    if n == 1:
        return [1]
    fib1 = fib2 = 1
    fibon_list.append(fib1)
    fibon_list.append(fib2)
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fibon_list.append(fib2)

    return fibon_list

def sorted_bubble(a):
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def calculator(x, y, symbol):
    if symbol == '+':
        return x+y
    if symbol == '-':
        return x-y
    if symbol == '*':
        return x*y
    if symbol == '/':
        return x/y
