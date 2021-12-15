class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x) + " , " + str(self.y)

    def getx(self):
        return self.x

    def setx(self, x):
        self.x = x


p = Punto()
print(p)
p.setx(100)
print(p.x)
print(p.getx())
