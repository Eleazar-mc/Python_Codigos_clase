cadena = input("Escriba una cadena: ")
reversa = ''

for j in range(len(cadena)-1, -1, -1):
    reversa += cadena[j]

print(reversa)

