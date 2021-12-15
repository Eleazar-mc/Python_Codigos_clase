'''
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
'''


'''
numeros = [7, 2, 8, -2.2, -1, 3]
minimo = numeros[0]
for numero in numeros:
    if numero < minimo:
        minimo = numero
print(minimo, 'es el número menor')
'''



dinosaurio = 'paquicefalosaurio'
print('paquicefalosaurio se deletrea así:')
for c in dinosaurio:
    #print(c)
    print(c, end = ' ')

