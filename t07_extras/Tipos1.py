class Fabrica:
    contador = 0  # Variable de clase

    def __init__(self):
        self.numero = __class__.contador  # self.numero es variable de instancia
        __class__.contador += 1
        self.id = 5


for x in range(10):
    f = Fabrica()
    print(f.numero, f.id)
