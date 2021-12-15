from datetime import date


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def del_anio(cls, nombre, anio):
        return cls(nombre, date.today().year - anio)

    @staticmethod  # Lo más parecido a Java
    def es_adulto(edad):
        return edad > 18


persona1 = Persona('mayank', 21)
persona2 = Persona.del_anio('mayank', 1996)

print(persona1.edad)
print(persona2.edad)
print(Persona.es_adulto(22))
