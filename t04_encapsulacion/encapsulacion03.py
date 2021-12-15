import math


class Circulo:
    def __init__(self, r=0.0):
        self._r = r

    @property
    def area(self):
        return math.pi * math.pow(self._r, 2)  # math.pi * self._r ** 2

    def area2(self):
        return self.area


c = Circulo(2.36)
print(c.area)  # Una propiedad no requiere paréntesis
print(c.area2)  # Un método normal requiere paréntesis
