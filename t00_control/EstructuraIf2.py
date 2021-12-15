import random

a = random.random()
b = random.random()
if a > b:
    print("a es mayor que b")

a = 2
b = 330
print(a, b)
print("A") if a > b else print("B")
a, b = b, a
print(a, b)
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if b < a < c:  # if a > b and c > a:
    print("Ambas condiciones son True")

if a > b or a > c:
    print("Al menos una de las condicones es True")
