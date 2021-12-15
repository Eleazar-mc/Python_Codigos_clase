class Klase:
    print("Inicialización de clase")
    var_clase = 3

    def __init__(self):
        print("Inicialización de objeto")
        self.var_instancia = 8

    @classmethod
    def met_clase(cls):
        print("Método de clase")

    print("Sentencia al final de la clase")


print(Klase.var_clase)
print(Klase().var_instancia)
Klase.met_clase()
