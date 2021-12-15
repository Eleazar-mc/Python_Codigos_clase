class Persona:
    def __init__(self):
        self.nombre = "Martin Heidegger"
        self.__profesion = "Filósofo"

    @property
    def profesion(self):
        return self.__profesion

    @profesion.setter
    def profesion(self, profesion):
        self.__profesion = profesion


p = Persona()
print(dir(p))
print(p.nombre)
print(p.profesion)
