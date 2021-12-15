class Klase:
    def __new__(cls):
        print(cls)
        return 19


print(Klase() + 5)


class Qlass:
    print("Sentencia de clase")

    def __new__(cls):
        print("__new__()")
        return super(Qlass, cls).__new__(cls)

    def __init__(self):
        print("__init__()")


Qlass()
