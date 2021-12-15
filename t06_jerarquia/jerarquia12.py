class Volador:
    def defender(self):
        print("Defendiendo al volar")


class Extraterrestre:
    def defender(self):
        print("Defendiendo a la humanidad")


class Superman(Extraterrestre, Volador):
    # pass

    def defender(self):
        super().defender()
        print("Superman defiende al mundo")
        super().defender()
        super()


s = Superman()
s.defender()
