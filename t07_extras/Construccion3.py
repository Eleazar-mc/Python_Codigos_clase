class Base:
    print("Base.<clinit>")

    def __init__(self):
        print("Base.__init__()")

    def __new__(cls):
        k = super(Base, cls).__new__(cls)
        print("Base.__new__()")
        return k


class Derivada(Base):
    print("Derivada.<clinit>")

    def __new__(cls):
        k = super(Derivada, cls).__new__(cls)
        print("Derivada.__new__()")
        return k

    def __init__(self):
        super().__init__()
        print("Derivada.__init__()")


Derivada()
