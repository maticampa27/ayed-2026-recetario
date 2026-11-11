import struct

from src.excepciones import ArchivoInvalidoError


FORMATO_HEADER = "<4s1sI"
FORMATO_REGISTRO = "<I50sI10s20s"

TAMAÑO_HEADER = struct.calcsize(FORMATO_HEADER)
TAMAÑO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)

MAGIA = b"AYED"
TEMA = b"R"


def convertir_bytes(texto, tamaño):
    datos = texto.encode("utf-8")

    if len(datos) > tamaño:
        raise ValueError(
            f"El texto '{texto}' supera los {tamaño} bytes."
        )

    return datos.ljust(tamaño, b"\x00")


def convertir_texto(datos):
    return datos.split(b"\x00", 1)[0].decode("utf-8")


def empaquetar_receta(receta):
    return struct.pack(
        FORMATO_REGISTRO,
        int(receta["id"]),
        convertir_bytes(receta["nombre"], 50),
        int(receta["tiempo_min"]),
        convertir_bytes(receta["dificultad"], 10),
        convertir_bytes(receta["categoria"], 20)
    )


def desempaquetar_receta(datos):
    id_receta, nombre, tiempo, dificultad, categoria = struct.unpack(
        FORMATO_REGISTRO,
        datos
    )

    return {
        "id": str(id_receta),
        "nombre": convertir_texto(nombre),
        "tiempo_min": str(tiempo),
        "dificultad": convertir_texto(dificultad),
        "categoria": convertir_texto(categoria)
    }


def guardar_binario(ruta, items):
    try:
        with open(ruta, "wb") as archivo:
            header = struct.pack(
                FORMATO_HEADER,
                MAGIA,
                TEMA,
                len(items)
            )

            archivo.write(header)

            for item in items:
                registro = empaquetar_receta(item)
                archivo.write(registro)

    except (OSError, ValueError) as error:
        raise ArchivoInvalidoError(
            "No se pudo guardar el archivo binario."
        ) from error


def cargar_binario(ruta):
    try:
        with open(ruta, "rb") as archivo:
            datos_header = archivo.read(TAMAÑO_HEADER)

            if len(datos_header) != TAMAÑO_HEADER:
                raise ArchivoInvalidoError(
                    "El header del archivo es demasiado corto."
                )

            magia, tema, cantidad = struct.unpack(
                FORMATO_HEADER,
                datos_header
            )

            if magia != MAGIA:
                raise ArchivoInvalidoError(
                    "La magia del archivo no es válida."
                )

            if tema != TEMA:
                raise ArchivoInvalidoError(
                    "El tema del archivo no corresponde al recetario."
                )

            recetas = []

            for _ in range(cantidad):
                datos = archivo.read(TAMAÑO_REGISTRO)

                if len(datos) != TAMAÑO_REGISTRO:
                    raise ArchivoInvalidoError(
                        "El archivo binario está truncado."
                    )

                receta = desempaquetar_receta(datos)
                recetas.append(receta)

            return recetas

    except OSError as error:
        raise ArchivoInvalidoError(
            "No se pudo abrir el archivo binario."
        ) from error


def actualizar_registro(ruta, posicion, item):
    try:
        with open(ruta, "r+b") as archivo:
            datos_header = archivo.read(TAMAÑO_HEADER)

            if len(datos_header) != TAMAÑO_HEADER:
                raise ArchivoInvalidoError(
                    "El header del archivo es demasiado corto."
                )

            magia, tema, cantidad = struct.unpack(
                FORMATO_HEADER,
                datos_header
            )

            if magia != MAGIA or tema != TEMA:
                raise ArchivoInvalidoError(
                    "El archivo binario no es válido."
                )

            if posicion < 0 or posicion >= cantidad:
                raise IndexError("La posición no existe.")

            posicion_archivo = (
                TAMAÑO_HEADER
                + posicion * TAMAÑO_REGISTRO
            )

            archivo.seek(posicion_archivo)

            archivo.write(empaquetar_receta(item))

    except OSError as error:
        raise ArchivoInvalidoError(
            "No se pudo actualizar el archivo."
        ) from error