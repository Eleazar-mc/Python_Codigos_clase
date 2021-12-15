import random


def condicion():
    resultado = random.random() < 0.99
    return resultado

i = 0
while condicion():
    print("Dentro de un while: ", i)
    i += 1

print("Fuera del while")

i = 1
while i < 6:
    print(i)
    i += 1
