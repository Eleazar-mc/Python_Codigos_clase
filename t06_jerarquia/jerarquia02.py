class Computadora:
    def __init__(self, marca, ram):
        self.marca = marca
        self.ram = ram

    def encender(self):
        print("Computadora", self.marca, "encendiendo")


class Laptop(Computadora):
    def __init__(self, marca, ram, modelo):
        super().__init__(marca, ram)
        self.modelo = modelo


dell = Laptop("dell", 16, 555)
print("Computadora: ", dell.marca)
print("RAM: ", dell.ram)
print("Modelo: ", dell.modelo)
dell.encender()

print("¿Laptop es subclase de Computadora?", issubclass(Laptop, Computadora))
print("¿Computadora es subclase de Laptop?", issubclass(Computadora, Laptop))
