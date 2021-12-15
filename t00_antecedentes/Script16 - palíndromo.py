cadena = input("Escribe una cadena: ")
reversa = ''

for i in range(len(cadena)-1, -1, -1):
    reversa += cadena[i]

if cadena == reversa:
    print('La cadena es un palíndromo')
else:
    print('La cadena no es palíndromo')
