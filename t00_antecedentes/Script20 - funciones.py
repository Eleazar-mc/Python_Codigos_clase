def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

val = int(input('Valor para factorial: '))
print('Factorial: {}'.format(fact(val)))
