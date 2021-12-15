class Matematicas:
    def doble(self, x):
        return x * 2

    def triple(self, x):
        return x * 3


if __name__ == "__main__":
    m = Matematicas()
    print(m.doble(5))
    print(m.triple(5))
