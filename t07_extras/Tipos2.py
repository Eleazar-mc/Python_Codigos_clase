import abc


class PuedePelear(abc.ABC):
    def pelear(self):
        pass


class PuedeNadar(abc.ABC):
    def nadar(self):
        pass


class PuedeVolar(abc.ABC):
    def volar(self):
        pass


class Accion:
    def pelear(self):
        pass


class Heroe(Accion, PuedeNadar, PuedePelear, PuedeVolar):
    pass


def t(x: PuedePelear):
    x.pelear()


def u(x: PuedeNadar):
    x.nadar()


def v(x: PuedeVolar):
    x.volar()


def w(x: Accion):
    x.pelear()


h: Heroe = Heroe()
t(h)
u(h)
v(h)
w(h)

pv: PuedeVolar = h
a: Accion = h
n: PuedeNadar = "Python"
print(n)
