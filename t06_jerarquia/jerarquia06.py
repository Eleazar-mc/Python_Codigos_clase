from abc import ABC, abstractmethod


class Abstracta(ABC):
    @abstractmethod
    def metodo(self):
        print("hola método abstracto")


class Concreta(Abstracta):
    def metodo(self):
        # super().metodo()
        print("hola método concreto")


# a = Abstracta()
# a.metodo()

c = Concreta()
c.metodo()

# Quitar el decorador y observar si es posible instanciar
