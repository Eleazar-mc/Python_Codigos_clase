'''
x = int(input('¿Cuánto es 2 + 5? '))
if x == 7:
    print("Tu aritmética básica es correcta")
else:
    print("Vuelve a intentarlo")
'''


'''
edad = int(input('Teclee tu edad: '))
if edad <= 25:
    print("Tu edad es de primavera inocente")
elif edad <= 50:
    print("Tu edad es de verano peligroso")
elif edad <= 75:
    print("Tu edad es de otoño relajado")
else:
    print("Tu edad invernal es un privilegio negado a muchos")
'''



'''
numero = input("Teclea un número: ")
if numero.isnumeric():
    numero = int(numero)
    if numero > 20:
        print('Tecleaste: ' + str(numero) + ' > 20')
    if numero > 10:
        print('Tecleaste: ' + str(numero) + ' > 10')
    if numero > 0:
        print('Tecleaste: ' + str(numero) + ' > 0')
else:
    print('La entrada no es un número o es negativo')
'''



numero = input("Teclea un número: ")
try:
    numero = int(numero)
    if numero > 20:
        print('Tecleaste: ' + str(numero) + ' > 20')
    if numero > 10:
        print('Tecleaste: ' + str(numero) + ' > 10')
    if numero > 0:
        print('Tecleaste: ' + str(numero) + ' > 0')
    if numero < 0:
        print('El número es negativo')
except ValueError as e:
    print('La entrada no es un número')

