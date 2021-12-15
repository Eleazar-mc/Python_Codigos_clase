class Parte:
    def __new__(cls):
        r = object.__new__(cls)
        # r = super(Parte, cls).__new__(cls)
        print("Parte.__new__()")
        return r

    def __init__(self):
        print("Parte.__init__()")


class Caracteristica:
    p = Parte()

    def __new__(cls):
        r = object.__new__(cls)
        # r = super(Caracteristica, cls).__new__(cls)
        print("Caracteristica.__new__()")
        return r

    def __init__(self):
        self.q = Parte()
        print("Caracteristica.__init__()")


class Esencial(Caracteristica):
    def __new__(cls):
        r = super(Esencial, cls).__new__(cls)
        print("Esencial.__new__()")
        return r

    def __init__(self):
        super().__init__()
        print("Esencial.__init__()")


Esencial()
