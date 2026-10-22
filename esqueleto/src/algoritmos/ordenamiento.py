def ordenar_seleccion(coleccion, clave):
    """Ordenamiento por selección. Devuelve una nueva secuencia."""

    resultado = list(coleccion)

    for i in range(len(resultado)):
        posicion_minima = i

        for j in range(i + 1, len(resultado)):
            if clave(resultado[j]) < clave(resultado[posicion_minima]):
                posicion_minima = j

        resultado[i], resultado[posicion_minima] = (
            resultado[posicion_minima],
            resultado[i]
        )

    return resultado


def ordenar_insercion(coleccion, clave):
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""
    
    resultado = list(coleccion)

    for i in range(1, len(resultado)):
        elemento = resultado[i]
        j = i - 1

        while j >= 0 and clave(resultado[j]) > clave(elemento):
            resultado[j + 1] = resultado[j]
            j -= 1

        resultado[j + 1] = elemento

    return resultado
