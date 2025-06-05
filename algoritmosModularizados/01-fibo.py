def fibonacci(n):
    if n<0:
        return 'INVALID0'
    elif n==0:
        return 1
    elif n ==1:
        return 1
    else:
        a, b = 0,1
        for i in range(2, n+1):
            a, b = b, b+a
            return b
            return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)



