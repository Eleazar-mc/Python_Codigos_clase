class Punto:
    pass


p = Punto()
print(p)
print(dir(p))

p.x = 2  # El objeto p funciona como un registro (Pascal) o estructura (C)
p.y = 3.3  # https://docs.python.org/3/tutorial/classes.html#odds-and-ends
print(p)
print(dir(p))
print(p.x, p.y)

p.x = 2.2
p.y = 0
print(p.x, p.y)
