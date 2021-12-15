class Volador:
    def __init__(self):
        print("Creación de característica volar")

    def volar(self):
        print("Volando")


class Extraterrestre:
    def __init__(self):
        print("Creación de característica extraterrestre")

    def golpear(self):
        print("Peleando")


class Superman(Volador, Extraterrestre):
    def __init__(self):
        # super().__init__()
        print("Creación de Superman")

    def defender(self):
        print("Superman defiende al mundo")


s = Superman()
s.volar()
s.defender()
s.golpear()
