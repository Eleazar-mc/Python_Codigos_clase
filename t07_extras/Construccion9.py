import math


class Instancia:
    def __call__(self, *args, **kwargs):
        print("Hola")
        return math.pi
    pass


print(Instancia())
i = Instancia()
print(i)
i()
print(i())