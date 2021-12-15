class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


p = Punto()
print(p.x, p.y)
q = Punto(5, 2.1)
print(q.x, q.y)
r = Punto(7)
print(r.x, r.y)
s = Punto(5, 2.1)
print(s.x, s.y)
t = Punto(y=2.1)
print(t.x, t.y)
t = Punto(y=2.1, x=-0.99)
print(t.x, t.y)
