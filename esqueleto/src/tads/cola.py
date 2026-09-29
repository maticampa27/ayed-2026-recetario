from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Cola:
    """Cola implementada sobre ListaEnlazada."""

    def __init__(self):
        self.__datos = ListaEnlazada()

    def encolar(self, dato):
        self.__datos.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")

        dato = next(iter(self.__datos))
        self.__datos.eliminar(dato)
        return dato

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")

        return next(iter(self.__datos))

    def esta_vacia(self):
        return self.__datos.esta_vacia()