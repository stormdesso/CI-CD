import copy

def fibonacci(n):
    fib1 = fib2 = 1
    a = []
    a.append(fib1)
    a.append(fib2)

    for i in range (2 , n) :
        fib1 , fib2 = fib2 , fib1 + fib2
        a.append(fib2)
    return a

def bubble_sort(array):
    N = len(array)
    a = []
    a = copy.deepcopy(array)

    for i in range (N - 1) :
        for j in range (N - i - 1) :
            if a[j] > a[j + 1] :
                a[j] , a[j + 1] = a[j + 1] , a[j]

    return a

def calc(n1, n2, sign):
    if sign == "-":
        return n1 - n2
    if sign == "+":
        return n1 + n2
    if sign == "*":
        return n1 * n2
    if sign == "/":
        return n1 / n2
