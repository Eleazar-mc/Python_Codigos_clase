class Rectangulo:
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    def area(self):
        return self._largo * self._ancho

    def perimetro(self):
        return self._largo * 2 + self._ancho * 2


class Cuadrado(Rectangulo):
    def __init__(self, largo):
        super().__init__(largo, largo)


c = Cuadrado(4)
print("Área del cuadrado:", c.area())
print("Perímetro del cuadrado:", c.perimetro())

r = Rectangulo(2, 4)
print("Área del rectángulo:", r.area())
print("Perímetro del rectángulo:", r.perimetro())
