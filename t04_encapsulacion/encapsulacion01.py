class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.equis = x
        self.ye = y

    @property
    def x(self):
        return self.equis

    @property
    def y(self):
        return self.ye

    @x.setter
    def x(self, x):
        self.equis = x

    @y.setter
    def y(self, y):
        self.ye = y

    def __str__(self):
        return str(self.x) + "," + str(self.y)


p = Punto()
p.x = 333
print(p)
q = Punto(0.23, -1.69)
print(q)
