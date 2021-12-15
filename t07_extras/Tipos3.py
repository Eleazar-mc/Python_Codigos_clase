import abc


class Monstruo(abc.ABC):
    def amenaza(self):
        pass


class MonstruoPeligroso(Monstruo):
    def destruye(self):
        pass


class Letal(abc.ABC):
    def mata(self):
        pass


class Godzilla(MonstruoPeligroso):
    def amenaza(self):
        pass

    def destruye(self):
        pass


class Vampiro(MonstruoPeligroso, Letal):
    def bebe_sangre(self):
        pass


class VampiroMuyMalo(Vampiro):
    def amenaza(self):
        pass

    def destruye(self):
        pass

    def mata(self):
        pass

    def bebe_sangre(self):
        pass


def u(m: Monstruo):
    m.amenaza()


def v(p: MonstruoPeligroso):
    p.amenaza()
    p.destruye()


def w(le: Letal):
    le.mata()


barney: MonstruoPeligroso = Godzilla()
u(barney)
v(barney)
dracula: Vampiro = VampiroMuyMalo()
u(dracula)
v(dracula)
w(dracula)
