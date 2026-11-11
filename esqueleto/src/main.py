from src.config import TEMA
from src.persistencia.recetas_csv import cargar_recetas
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.persistencia.texto import cargar_txt, guardar_txt
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro
)
from src.excepciones import ArchivoInvalidoError


RUTA_TXT = "data/recetas.txt"
RUTA_BIN = "data/recetas.bin"

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

def mostrar_recetas(recetas):
    print("=======================================")
    print("              RECETARIO")
    print("=======================================")

    for receta in recetas:
        print(f"ID: {receta['id']}")
        print(f"Nombre: {receta['nombre']}")
        print(f"Tiempo: {receta['tiempo_min']} minutos")
        print(f"Dificultad: {receta['dificultad']}")
        print(f"Categoría: {receta['categoria']}")
        print("----------------------------------------")


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar en texto")
    print("10. Cargar desde texto")
    print("11. Guardar en binario")
    print("12. Cargar desde binario")
    print("13. Alta de receta")
    print("14. Baja de receta")
    print("15. Modificar receta")   
    print("0. Salir")

def buscar_lineal(recetas):
    nombre = input("Ingrese el nombre de la receta: ")

    resultado = busqueda_lineal(
        recetas,
        nombre,
        lambda receta: receta["nombre"]
    )

    if resultado is None:
        print("Receta no encontrada.")
    else:
        print(f"Encontrada: {resultado['nombre']}")

def buscar_binaria(recetas):
    recetas_ordenadas = ordenar_insercion(
        recetas,
        lambda receta: receta["nombre"]
    )

    nombre = input("Ingrese el nombre de la receta: ")

    resultado = busqueda_binaria(
        recetas_ordenadas,
        nombre,
        lambda receta: receta["nombre"]
    )

    if resultado is None:
        print("Receta no encontrada.")
    else:
        print(f"Encontrada: {resultado['nombre']}")

def ordenar_recetas_seleccion(recetas):
    return ordenar_seleccion(
        recetas,
        lambda receta: receta["nombre"]
    )


def ordenar_recetas_insercion(recetas):
    return ordenar_insercion(
        recetas,
        lambda receta: receta["nombre"]
    )

def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    recetas = cargar_recetas()

    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
            mostrar_recetas(recetas)

        elif opcion in {"2", "3", "4", "5", "6", "7", "8"}:
            pendiente()

        elif opcion == "9":
            guardar_recetas_txt(recetas)

        elif opcion == "10":
            recetas = cargar_recetas_txt()

        elif opcion == "11":
            guardar_recetas_binario(recetas)

        elif opcion == "12":
            recetas = cargar_recetas_binario()

        elif opcion == "13":
            alta_receta(recetas)

        elif opcion == "14":
            baja_receta(recetas)

        elif opcion == "15":
            modificar_receta(recetas)

        else:
            print("Opción inválida.")

def guardar_recetas_txt(recetas):
    encabezados = [
        "id",
        "nombre",
        "tiempo_min",
        "dificultad",
        "categoria"
    ]

    guardar_txt(RUTA_TXT, recetas, encabezados)

    print("Recetas guardadas correctamente en texto.")

def cargar_recetas_txt():
    recetas = cargar_txt(RUTA_TXT)

    print("Recetas cargadas correctamente desde texto.")

    return recetas

def guardar_recetas_binario(recetas):
    guardar_binario(RUTA_BIN, recetas)

    print("Recetas guardadas correctamente en binario.")

def cargar_recetas_binario():
    try:
        recetas = cargar_binario(RUTA_BIN)

        print("Recetas cargadas correctamente desde binario.")

        return recetas

    except ArchivoInvalidoError as error:
        print(f"Error: {error}")

        return []

def alta_receta(recetas):
    nuevo_id = str(len(recetas) + 1)

    nombre = input("Nombre: ")
    tiempo = input("Tiempo en minutos: ")
    dificultad = input("Dificultad: ")
    categoria = input("Categoría: ")

    receta = {
        "id": nuevo_id,
        "nombre": nombre,
        "tiempo_min": tiempo,
        "dificultad": dificultad,
        "categoria": categoria
    }

    recetas.append(receta)

    guardar_txt(
        RUTA_TXT,
        recetas,
        ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
    )

    guardar_binario(RUTA_BIN, recetas)

    print("Receta agregada y guardada.")

def baja_receta(recetas):
    id_buscar = input("ID de la receta a eliminar: ")

    for receta in recetas:
        if receta["id"] == id_buscar:
            recetas.remove(receta)

            guardar_txt(
                RUTA_TXT,
                recetas,
                ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
            )

            guardar_binario(RUTA_BIN, recetas)

            print("Receta eliminada y cambios guardados.")
            return

    print("No se encontró la receta.")

def modificar_receta(recetas):
    id_buscar = input("ID de la receta a modificar: ")

    for posicion in range(len(recetas)):
        receta = recetas[posicion]

        if receta["id"] == id_buscar:
            print(f"Receta actual: {receta['nombre']}")

            nuevo_nombre = input(
                "Nuevo nombre (Enter para mantener): "
            )

            if nuevo_nombre != "":
                receta["nombre"] = nuevo_nombre

            nuevo_tiempo = input(
                "Nuevo tiempo (Enter para mantener): "
            )

            if nuevo_tiempo != "":
                receta["tiempo_min"] = nuevo_tiempo

            guardar_txt(
                RUTA_TXT,
                recetas,
                ["id", "nombre", "tiempo_min", "dificultad", "categoria"]
            )

            actualizar_registro(
                RUTA_BIN,
                posicion,
                receta
            )

            print("Receta modificada y guardada.")
            return

    print("No se encontró la receta.")

if __name__ == "__main__":
    main()
