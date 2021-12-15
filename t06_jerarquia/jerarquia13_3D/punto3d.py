from t06_jerarquia.jerarquia13_2D.punto import Punto


class Punto3D(Punto):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z

    def __str__(self):
        return super().__str__() + "," + str(self.z)
