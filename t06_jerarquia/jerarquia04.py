class Persona:
    def __init__(self):
        self.nombre = "Martin Heidegger"
        self.__profesion = "Filósofo"


class Escritora(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.nombre = "Ada Lovelace"
        self.__profesion = "Programadora"


e = Escritora()
print(dir(e))
print(e.nombre)
print(e._Persona__profesion, e._Escritora__profesion)
