def fact(n):
    f = 1
    for i in range(1, n + 1): 
        f = f * i
    return f

val = int(input('Valor para factorial con for: '))
print('Factorial: {}'.format(fact(val)))
