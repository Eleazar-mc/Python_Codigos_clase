class K:
    def __init__(self):
        print("K.<init>")


class X:
    k = K()
    print("Hola")
