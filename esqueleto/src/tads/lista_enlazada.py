from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
         self.__primero = None
         self.__tamanio = 0

    def esta_vacia(self):
        return self.__primero is None

    def tamanio(self):
        return self.__tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.__primero)
        self.__primero = nuevo
        self.__tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.__primero = nuevo
        else:
            actual = self.__primero

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self.__tamanio += 1

    def insertar_ordenado(self, dato, clave):
        nuevo = Nodo(dato)

        if self.esta_vacia() or clave(dato) <= clave(self.__primero.dato):
            nuevo.siguiente = self.__primero
            self.__primero = nuevo
            self.__tamanio += 1
            return

        actual = self.__primero

        while (
            actual.siguiente is not None
            and clave(actual.siguiente.dato) < clave(dato)
        ):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        self.__tamanio += 1

    def eliminar(self, dato):
        if self.esta_vacia():
            return False

        if self.__primero.dato == dato:
            self.__primero = self.__primero.siguiente
            self.__tamanio -= 1
            return True

        anterior = self.__primero
        actual = self.__primero.siguiente

        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self.__tamanio -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def buscar(self, dato):
        actual = self.__primero

        while actual is not None:
            if actual.dato == dato:
                return actual.dato

            actual = actual.siguiente

        return None

    def __iter__(self):
        actual = self.__primero

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
