class Base:
    def __init__(self):
        print("Súper clase")


class Derivada(Base):
    def __init__(self):
        # super().__init__()
        print("Subclase")


Derivada()
