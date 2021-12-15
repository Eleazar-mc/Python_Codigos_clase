class Persona:
    def __init__(self):
        self.nombre = "Martin Heidegger"
        self._edad = 87

    @property
    def edad(self):
        return self._edad


p = Persona()
print(p.nombre, p.edad)
