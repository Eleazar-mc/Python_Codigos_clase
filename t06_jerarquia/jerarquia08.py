class Mariposa:
    pass


class Larva(Mariposa):
    def arrastrar(self):
        print("Larva arrastrándose")


class Adulto(Mariposa):
    def volar(self):
        print("Adulto volando")


m = Larva()
m.arrastrar()
print(m)

m = Adulto()
m.volar()
print(m)
