class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " , " + str(self.y)


p = Punto()
print(p)
q = Punto(5, 2.1)
print(q)
r = Punto(7)
print(r)

print(Punto(5, 2.1))
print(Punto(y=2.1))
print(Punto(y=2.1, x=-0.99))
