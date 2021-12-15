for x in range(10):
    print(x, end = ' ')
print()

for x in range(0, 10):
    print(x, end = ' ')
print()

for x in range(1,7):
    print(x, end = ' ')
print()

for x in range(0, 30, 7): #inicio, fin, paso
    print(x, end = ' ')
print()

for x in range(10, -1, -1):
    print(x, end = ' ')
print()

for x in range(1, 10, 3):
    print(x, end = ' ')
print()

#Obtener los números nones entre el 1 y el 200
nones = []
for x in range(1, 200):
    if x % 2 != 0:
        print(x)
        nones.append(x)
print(nones)

