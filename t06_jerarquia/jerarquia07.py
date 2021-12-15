from abc import ABC, abstractmethod


class Ave(ABC):
    @abstractmethod
    def volar(self):
        pass

    @abstractmethod
    def nadar(self):
        pass


class Perico(Ave):
    def volar(self):
        print("Perico volando")

    def nadar(self):
        print("Un perico no nada")


class Pinguino(Ave):
    def volar(self):
        print("Un pingüino no vuela")

    def nadar(self):
        print("Pingüino nadando")


# Interfaz común
def prueba_de_vuelo(ave):
    ave.volar()


pe = Perico()
pi = Pinguino()
prueba_de_vuelo(pe)
prueba_de_vuelo(pi)

# Eliminación de objetos
# del pi
# print(pi)
