class Base:
    print("Base.<clinit>")

    def __init__(self):
        print("Base.__init__()")


class Derivada(Base):
    print("Derivada.<clinit>")

    def __init__(self):
        # super().__init__()
        print("Derivada.__init__()")


Derivada()
