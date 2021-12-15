class Mariposa:
    def arrastrar(self):
        print("Larva arrastrándose")


def volar():
    print("Adulto volando")


m1 = Mariposa()
m1.arrastrar()
print(m1)

m2 = Mariposa()

del Mariposa.arrastrar

setattr(m1, "volar", volar())
m1.volar
print(m1)

# La asignación del atributo aplica sobre una instancia específica
# m2.volar

# El borrado aplica a nivel de clase
# m2.arrastrar()
# m1.arrastrar()
