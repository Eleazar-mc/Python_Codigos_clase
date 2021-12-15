class Bowl:
    def __init__(self, marker):
        print("Bowl.__init__(", marker, ")")

    def f1(self, marker):
        print("f1(", marker, ")")


class Table:
    bowl1 = Bowl(1)

    def __init__(self):
        print("Table.__init__()")
        Table.bowl2.f1(1)

    def f2(self, marker):
        print("f2(", marker, ")")

    bowl2 = Bowl(2)


class Cupboard:
    bowl4 = Bowl(4)

    def __init__(self):
        self.bowl3 = Bowl(3)
        print("Cupboard.__init__()")
        Cupboard.bowl4.f1(2)

    def f3(self, marker):
        print("f3(", marker, ")")

    bowl5 = Bowl(5)


class StaticInitialization:
    @staticmethod
    def main():
        print("Creating new Cupboard() in main")
        Cupboard()
        print("Creating new Cupboard() in main")
        Cupboard()

        StaticInitialization.table.f2(1)
        StaticInitialization.cupboard.f3(1)

    table = Table()
    cupboard = Cupboard()


if __name__ == '__main__':
    print(StaticInitialization.main())
