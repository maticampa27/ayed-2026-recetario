def busqueda_lineal(coleccion, clave, obtener_clave):
    """Devuelve el ítem cuya clave coincide, o None."""

    for item in coleccion:
        if obtener_clave(item) == clave:
            return item
    
    return None


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""

    inicio = 0
    fin = len(coleccion_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        valor = obtener_clave(coleccion_ordenada[medio])

        if valor == clave:
            return coleccion_ordenada[medio]
        elif valor < clave:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return None
