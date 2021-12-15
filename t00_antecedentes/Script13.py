'''
contraseña = ""
while contraseña != "secreto":
    contraseña = input('Escribe la contraseña: ')
    if contraseña == "secreto":
        print('¡Bienvenido!')
    else:
        print('Contraseña incorrecta, intenta de nuevo.')
'''


'''
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1
'''


'''
for numero in range(1, 21):
    if numero % 2 != 0:      #Prueba por número non
        if numero % 3 == 0:  #Prueba por múltiplo de 3
            continue
        print(numero)
'''



for i in range(1,11):
    for j in range(1,11):
        print('{} * {} = {}'.format(i, j, i * j))

