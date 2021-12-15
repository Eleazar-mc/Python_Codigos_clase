import math

# import math as m

# from math import pi
# from math import pow


class Circulo:
    def __init__(self, r):
        self._r = r

    def area(self):
        return math.pi * math.pow(self._r, 2)


c = Circulo(5.03)
print("Área del círculo: ", c.area())
