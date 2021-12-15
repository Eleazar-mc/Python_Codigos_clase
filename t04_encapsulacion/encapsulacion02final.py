class Punto:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x

    @y.setter
    def y(self, y):
        self._y = y

    def __str__(self):
        return str(self.x) + "," + str(self.y)


class Circulo:
    def __init__(self, c=Punto(), r=1.0):
        self._c = c
        self._r = r

    # def __init__(self, x=0.0, y=0.0, r=1.0):
    #     self._c = Punto(x, y)  # Composición
    #     self._r = r

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        if r < 0:
            raise Exception("El radio no debe tener valor negativo")
        else:
            self._r = r

    @property
    def x(self):
        return self._c.x

    @x.setter
    def x(self, x):
        self._c.x = x

    @property
    def y(self):
        return self._c.y

    @y.setter
    def y(self, y):
        self._c.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "):" + str(self._r)


p = Punto()
p.x = 333
print(p)
q = Punto(0.23, -1.69)
print(q)

cir = Circulo()
print(cir)
cir = Circulo(q)
print(cir)
cir = Circulo(r=5.36)
print(cir)
cir = Circulo(q, 6.32)
print(cir)
cir = Circulo(r=6.37, c=q)
print(cir)
cir.r = -1
