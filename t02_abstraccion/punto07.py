class Punto:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    @property  # Decorador, especificado por la @
    def getx(self):
        return self._x

    @property  # Una propiedad permite y exige la omisión de () al usarla
    def gety(self):
        return self._y

    def __str__(self):
        return str(self.getx) + " , " + str(self.gety)


p = Punto()
print(p)

"""
No hay restricciones para acceder al valor de una variable.
El caracter _ permite indicar a un programador que la variable
es solo para uso interno.

Las miembros con _ se deben tratar como una parte no pública
de la API = detalle de implementación que cambia sin previo aviso.
"""
