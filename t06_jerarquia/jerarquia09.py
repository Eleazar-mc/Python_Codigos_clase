class Mariposa:
    pass


m = Mariposa()
m.arrastrar = "Larva arrastrándose"
print(m)
print(m.__dict__)

del m.arrastrar

m.volar = "Adulto volando"
print(m)
print(m.__dict__)
