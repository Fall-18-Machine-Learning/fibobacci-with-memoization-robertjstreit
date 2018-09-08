fibstruct = {}

def fib(n):

    if n in fibstruct:
        return fibstruct[n]
    
    if (n == 0):
        fibval = 0
    elif (n == 1):
        fibval = 1
    else:
        fibval = fib(n-1) + fib(n-2)

    fibstruct[n] = fibval
    return fibval
