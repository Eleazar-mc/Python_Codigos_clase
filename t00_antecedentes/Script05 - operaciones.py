x = y = 10
z = 2 * x + y
print(z) #30

z = z ** (y - 1)
print(z) #19683000000000

x = 42
b = 15 < (x / 2) < 25
print(b) #True

print(type(b)) #<class 'bool'>

x = 42
y = str(x)
x *= 2 #x = x * 2
y *= 2 #y = y * 2, concatenación
print(x) #84
print(y) #4242
