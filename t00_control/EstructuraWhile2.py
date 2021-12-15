import random


def condicion():
    resultado = random.random() < 0.99
    return resultado

i = 0
while condicion():
    print("Dentro de un while: ", i)
    i += 1
else:
    print("Fin del while")

print("Fuera del while")
