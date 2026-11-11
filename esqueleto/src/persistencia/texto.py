import csv


def cargar_txt(ruta):
    filas = []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if not lineas:
                raise ValueError("El archivo está vacío.")

            encabezados = lineas[0].strip().split("|")

            for linea in lineas[1:]:
                valores = linea.strip().split("|")

                if len(valores) != len(encabezados):
                    raise ValueError("Una fila tiene una cantidad incorrecta de campos.")

                fila = {}

                for i in range(len(encabezados)):
                    fila[encabezados[i]] = valores[i]

                filas.append(fila)

    except (OSError, ValueError) as error:
        raise ValueError("El archivo de texto es inválido.") from error

    return filas


def guardar_txt(ruta, filas, encabezados):
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("|".join(encabezados) + "\n")

            for fila in filas:
                valores = []

                for encabezado in encabezados:
                    valores.append(str(fila[encabezado]))

                archivo.write("|".join(valores) + "\n")

    except OSError as error:
        raise ValueError("No se pudo guardar el archivo.") from error