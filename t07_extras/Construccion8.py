class X:
    r = 5

    def __new__(cls, *args, **kwargs):
        print("Nuevo objeto")


print(X.r)
