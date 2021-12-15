from t05_modularidad.modulo02 import mod01 as modulo
from t05_modularidad.modulo02 import mod02 as figuras

modulo.saludar("Ulises")

p = figuras.Punto()
q = figuras.Punto(3, 4)
print(p.x, p.y)
print(q.x, q.y)
