from t06_jerarquia.jerarquia13_2D.circulo import Circulo
from t06_jerarquia.jerarquia13_2D.punto import Punto
from t06_jerarquia.jerarquia13_3D.punto3d import Punto3D


class Esfera(Circulo):
    def __init__(self, c=Punto3D(), r=1.0):
        super().__init__(Punto(c.x, c.y), r)
        self._c = c
        self._r = r

    @property
    def z(self):
        return self._c.z

    @z.setter
    def z(self, z):
        self._c.z = z

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "):" + str(self._r)
