from src.excepciones import PilaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Pila:
    """Pila implementada sobre ListaEnlazada."""

    def __init__(self):
        self.__datos = ListaEnlazada()

    def apilar(self, dato):
        self.__datos.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")

        dato = next(iter(self.__datos))
        self.__datos.eliminar(dato)
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")

        return next(iter(self.__datos))

    def esta_vacia(self):
        return self.__datos.esta_vacia()