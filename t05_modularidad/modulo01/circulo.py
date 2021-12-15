from t05_modularidad.modulo01.punto import Punto


class Circulo:
    def __init__(self, c=Punto(), r=1.0):
        self._c = c
        self._r = r

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
