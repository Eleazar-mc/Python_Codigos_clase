import math

for i in range(10):
    print(math.pow(i, 2))

frutas = ["manzana", "plátano", "fresa"]
for x in frutas:
    print(x)

for c in "murciélago":
    print(c)

for x in frutas:
    print(x)
    if x == "plátano":
        break

for x in frutas:
    if x == "plátano":
        continue
    print(x)

for i in range(2, 30, 4):
    print(i)
