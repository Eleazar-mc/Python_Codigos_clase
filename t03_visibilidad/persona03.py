class Persona:
    def __init__(self):
        self.nombre = "Martin Heidegger"
        self.__profesion = "Filósofo"


p = Persona()
print(dir(p))
print(p.nombre)
print(p._Persona__profesion)
