import csv

from src.excepciones import ArchivoInvalidoError


def cargar_txt(ruta):
    filas = []

    try:
        with open(
            ruta,
            "r",
            encoding="utf-8",
            newline=""
        ) as archivo:

            lector = csv.DictReader(archivo)

            if lector.fieldnames is None:
                raise ArchivoInvalidoError(
                    "El archivo no tiene encabezado."
                )

            for fila in lector:
                if not fila:
                    continue

                filas.append(dict(fila))

    except FileNotFoundError as error:
        raise ArchivoInvalidoError(
            f"No existe el archivo: {ruta}"
        ) from error

    except (
        OSError,
        UnicodeError,
        csv.Error
    ) as error:

        raise ArchivoInvalidoError(
            f"El archivo de texto es inválido: {ruta}"
        ) from error

    return filas


def guardar_txt(ruta, filas, encabezados):
    try:
        with open(
            ruta,
            "w",
            encoding="utf-8",
            newline=""
        ) as archivo:

            escritor = csv.DictWriter(
                archivo,
                fieldnames=encabezados
            )

            escritor.writeheader()

            for fila in filas:
                escritor.writerow(fila)

    except OSError as error:
        raise ArchivoInvalidoError(
            f"No se pudo guardar el archivo: {ruta}"
        ) from error