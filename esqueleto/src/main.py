from src.config import TEMA
from src.persistencia.recetas_csv import cargar_recetas
from src.persistencia.texto import cargar_txt, guardar_txt
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro
)

from src.algoritmos.busqueda import (
    busqueda_lineal,
    busqueda_binaria
)

from src.algoritmos.ordenamiento import (
    ordenar_seleccion,
    ordenar_insercion
)

from src.tads.lista_enlazada import ListaEnlazada
from src.tads.pila import Pila
from src.tads.cola import Cola

from src.excepciones import (
    ArchivoInvalidoError,
    PilaVaciaError,
    ColaVaciaError
)


RUTA_TXT = "data/recetas.txt"
RUTA_BIN = "data/recetas.bin"

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

ENCABEZADOS = [
    "id",
    "nombre",
    "tiempo_min",
    "dificultad",
    "categoria"
]


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")

    print()
    print("=======================================")
    print(f"     {nombre} — AyED C2 2026")
    print("=======================================")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Menú de la semana")
    print("7. Historial de recetas cocinadas")
    print("8. Cola de preparación")
    print("9. Guardar en texto")
    print("10. Cargar desde texto")
    print("11. Guardar en binario")
    print("12. Cargar desde binario")
    print("13. Alta de receta")
    print("14. Baja de receta")
    print("15. Modificar receta")
    print("0. Salir")


def lista_python(coleccion):
    return list(coleccion)


def buscar_por_id(coleccion, id_buscar):
    for receta in coleccion:
        if str(receta["id"]) == str(id_buscar):
            return receta

    return None


def mostrar_receta(receta):
    print()
    print("------------- DETALLE -------------")
    print(f"ID: {receta['id']}")
    print(f"Nombre: {receta['nombre']}")
    print(f"Tiempo: {receta['tiempo_min']} minutos")
    print(f"Dificultad: {receta['dificultad']}")
    print(f"Categoría: {receta['categoria']}")
    print("-----------------------------------")


def listar_catalogo(coleccion):
    print()
    print("============= RECETARIO =============")

    # usa iterador
    for receta in coleccion:
        print(
            f"{receta['id']} - "
            f"{receta['nombre']} - "
            f"{receta['tiempo_min']} min - "
            f"{receta['dificultad']} - "
            f"{receta['categoria']}"
        )

    print("=====================================")


def ver_detalle(coleccion):
    id_buscar = input("Ingrese el ID de la receta: ").strip()

    receta = buscar_por_id(coleccion, id_buscar)

    if receta is None:
        print("Receta no encontrada.")
        return

    mostrar_receta(receta)


def buscar_lineal_menu(coleccion):
    nombre = input("Ingrese el nombre de la receta: ").strip()

    resultado = busqueda_lineal(
        coleccion,
        nombre,
        lambda receta: receta["nombre"]
    )

    if resultado is None:
        print("Receta no encontrada.")
    else:
        mostrar_receta(resultado)


def buscar_binaria_menu(coleccion):
    nombre = input("Ingrese el nombre de la receta: ").strip()

    recetas = lista_python(coleccion)

    recetas = ordenar_insercion(
        recetas,
        lambda receta: receta["nombre"]
    )

    resultado = busqueda_binaria(
        recetas,
        nombre,
        lambda receta: receta["nombre"]
    )

    if resultado is None:
        print("Receta no encontrada.")
    else:
        mostrar_receta(resultado)


def buscar_menu(coleccion):
    print()
    print("1. Búsqueda lineal")
    print("2. Búsqueda binaria")

    opcion = input("> ").strip()

    if opcion == "1":
        buscar_lineal_menu(coleccion)

    elif opcion == "2":
        buscar_binaria_menu(coleccion)

    else:
        print("Opción inválida.")


def ordenar_menu(coleccion):
    recetas = lista_python(coleccion)

    print()
    print("1. Ordenar por nombre")
    print("2. Ordenar por tiempo")

    opcion = input("> ").strip()

    if opcion == "1":
        resultado = ordenar_insercion(
            recetas,
            lambda receta: receta["nombre"]
        )

    elif opcion == "2":
        resultado = ordenar_seleccion(
            recetas,
            lambda receta: int(receta["tiempo_min"])
        )

    else:
        print("Opción inválida.")
        return

    print()
    print("========= RECETAS ORDENADAS =========")

    for receta in resultado:
        print(
            f"{receta['id']} - "
            f"{receta['nombre']} - "
            f"{receta['tiempo_min']} min"
        )


def cargar_subrecetas():
    relaciones = {}

    try:
        with open(
            "data/subrecetas.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            lineas = archivo.readlines()

            for linea in lineas[1:]:
                partes = linea.strip().split(",")

                if len(partes) != 2:
                    continue

                receta_id = partes[0]
                subreceta_id = partes[1]

                if receta_id not in relaciones:
                    relaciones[receta_id] = []

                relaciones[receta_id].append(subreceta_id)

    except OSError:
        print("No se pudo cargar subrecetas.csv.")

    return relaciones


def desglosar_receta(
    receta_id,
    recetas_por_id,
    relaciones,
    nivel=0
):
    receta = recetas_por_id.get(str(receta_id))

    if receta is None:
        print("  " * nivel + "Receta no encontrada.")
        return

    print("  " * nivel + f"- {receta['nombre']}")

    subrecetas = relaciones.get(str(receta_id), [])

    # CASO BASE
    if len(subrecetas) == 0:
        return

    # RECURSIVA
    for subreceta_id in subrecetas:
        desglosar_receta(
            subreceta_id,
            recetas_por_id,
            relaciones,
            nivel + 1
        )


def recursion_menu(coleccion):
    id_buscar = input(
        "Ingrese el ID de la receta a desglosar: "
    ).strip()

    recetas = lista_python(coleccion)

    recetas_por_id = {}

    for receta in recetas:
        recetas_por_id[str(receta["id"])] = receta

    relaciones = cargar_subrecetas()

    if id_buscar not in recetas_por_id:
        print("Receta no encontrada.")
        return

    print()
    print("========= DESGLOSE =========")

    desglosar_receta(
        id_buscar,
        recetas_por_id,
        relaciones
    )


def menu_semana():
    menu = ListaEnlazada()

    while True:
        print()
        print("========= MENU DE LA SEMANA =========")
        print("1. Agregar receta")
        print("2. Eliminar receta")
        print("3. Mostrar menú")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            id_receta = input("ID de receta: ").strip()

            if menu.buscar(id_receta) is not None:
                print("La receta ya está en el menú.")
                continue

            menu.insertar_al_final(id_receta)

            print("Receta agregada al menú.")

        elif opcion == "2":
            id_receta = input("ID de receta: ").strip()

            if menu.eliminar(id_receta):
                print("Receta eliminada del menú.")
            else:
                print("La receta no estaba en el menú.")

        elif opcion == "3":
            print()
            print("Menú de la semana:")

            if menu.esta_vacia():
                print("El menú está vacío.")
            else:
                for id_receta in menu:
                    print(f"- Receta ID: {id_receta}")

        else:
            print("Opción inválida.")


def historial_menu(historial):
    while True:
        print()
        print("====== HISTORIAL DE COCINADAS ======")
        print("1. Cocinar receta (push)")
        print("2. Deshacer última receta (pop)")
        print("3. Ver última receta")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            id_receta = input("ID de receta cocinada: ").strip()

            historial.apilar(id_receta)

            print("Receta agregada al historial.")

        elif opcion == "2":
            try:
                id_receta = historial.desapilar()
                print(f"Última receta retirada: {id_receta}")

            except PilaVaciaError as error:
                print(f"Error: {error}")

        elif opcion == "3":
            try:
                id_receta = historial.ver_tope()
                print(f"Última receta: {id_receta}")

            except PilaVaciaError as error:
                print(f"Error: {error}")

        else:
            print("Opción inválida.")


def cola_menu(cola):
    while True:
        print()
        print("========= COLA DE PREPARACION =========")
        print("1. Encolar receta")
        print("2. Desencolar receta")
        print("3. Ver próxima receta")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return

        elif opcion == "1":
            id_receta = input("ID de receta: ").strip()

            cola.encolar(id_receta)

            print("Receta agregada a la cola.")

        elif opcion == "2":
            try:
                id_receta = cola.desencolar()
                print(f"Receta retirada de la cola: {id_receta}")

            except ColaVaciaError as error:
                print(f"Error: {error}")

        elif opcion == "3":
            try:
                id_receta = cola.ver_frente()
                print(f"Próxima receta: {id_receta}")

            except ColaVaciaError as error:
                print(f"Error: {error}")

        else:
            print("Opción inválida.")


def guardar_recetas_txt(coleccion):
    recetas = lista_python(coleccion)

    guardar_txt(
        RUTA_TXT,
        recetas,
        ENCABEZADOS
    )

    print("Recetas guardadas correctamente en texto.")


def cargar_recetas_txt():
    recetas = cargar_txt(RUTA_TXT)

    coleccion = ListaEnlazada()

    for receta in recetas:
        coleccion.insertar_al_final(receta)

    print("Recetas cargadas correctamente desde texto.")

    return coleccion


def guardar_recetas_binario(coleccion):
    recetas = lista_python(coleccion)

    guardar_binario(
        RUTA_BIN,
        recetas
    )

    print("Recetas guardadas correctamente en binario.")


def cargar_recetas_binario():
    recetas = cargar_binario(RUTA_BIN)

    coleccion = ListaEnlazada()

    for receta in recetas:
        coleccion.insertar_al_final(receta)

    print("Recetas cargadas correctamente desde binario.")

    return coleccion

def alta_receta(coleccion):
    ids = []

    for receta in coleccion:
        ids.append(int(receta["id"]))

    nuevo_id = str(max(ids) + 1)

    nombre = input("Nombre: ").strip()
    tiempo = input("Tiempo en minutos: ").strip()
    dificultad = input("Dificultad: ").strip()
    categoria = input("Categoría: ").strip()

    receta = {
        "id": nuevo_id,
        "nombre": nombre,
        "tiempo_min": tiempo,
        "dificultad": dificultad,
        "categoria": categoria
    }

    coleccion.insertar_al_final(receta)

    guardar_recetas_txt(coleccion)
    guardar_recetas_binario(coleccion)

    print("Receta agregada y guardada.")


def baja_receta(coleccion):
    id_buscar = input(
        "ID de la receta a eliminar: "
    ).strip()

    receta = buscar_por_id(
        coleccion,
        id_buscar
    )

    if receta is None:
        print("No se encontró la receta.")
        return

    coleccion.eliminar(receta)

    guardar_recetas_txt(coleccion)
    guardar_recetas_binario(coleccion)

    print("Receta eliminada y cambios guardados.")


def modificar_receta(coleccion):
    id_buscar = input(
        "ID de la receta a modificar: "
    ).strip()

    recetas = lista_python(coleccion)

    posicion = -1
    receta = None

    for i in range(len(recetas)):
        if str(recetas[i]["id"]) == id_buscar:
            posicion = i
            receta = recetas[i]
            break

    if receta is None:
        print("No se encontró la receta.")
        return

    print()
    print(f"Receta actual: {receta['nombre']}")

    nuevo_nombre = input(
        "Nuevo nombre (Enter para mantener): "
    ).strip()

    if nuevo_nombre != "":
        receta["nombre"] = nuevo_nombre

    nuevo_tiempo = input(
        "Nuevo tiempo (Enter para mantener): "
    ).strip()

    if nuevo_tiempo != "":
        receta["tiempo_min"] = nuevo_tiempo

    nueva_dificultad = input(
        "Nueva dificultad (Enter para mantener): "
    ).strip()

    if nueva_dificultad != "":
        receta["dificultad"] = nueva_dificultad

    nueva_categoria = input(
        "Nueva categoría (Enter para mantener): "
    ).strip()

    if nueva_categoria != "":
        receta["categoria"] = nueva_categoria

 
    guardar_recetas_txt(coleccion)

  
    actualizar_registro(
        RUTA_BIN,
        posicion,
        receta
    )

    print("Receta modificada correctamente.")



def main():

    if TEMA not in TEMAS:
        print(
            "Seteá TEMA en src/config.py: "
            "'pokedex', 'recetario' o 'musica'."
        )
        return

    recetas_iniciales = cargar_recetas()

    
    coleccion = ListaEnlazada()

    for receta in recetas_iniciales:
        coleccion.insertar_al_final(receta)

    
    historial = Pila()
    cola = Cola()

    opcion = None

    while opcion != "0":

        mostrar_menu()

        opcion = input("> ").strip()

        try:

            if opcion == "0":
                print("Chau.")

            elif opcion == "1":
                listar_catalogo(coleccion)

            elif opcion == "2":
                ver_detalle(coleccion)

            elif opcion == "3":
                buscar_menu(coleccion)

            elif opcion == "4":
                ordenar_menu(coleccion)

            elif opcion == "5":
                recursion_menu(coleccion)

            elif opcion == "6":
                menu_semana()

            elif opcion == "7":
                historial_menu(historial)

            elif opcion == "8":
                cola_menu(cola)

            elif opcion == "9":
                guardar_recetas_txt(coleccion)

            elif opcion == "10":
                coleccion = cargar_recetas_txt()

            elif opcion == "11":
                guardar_recetas_binario(coleccion)

            elif opcion == "12":
                coleccion = cargar_recetas_binario()

            elif opcion == "13":
                alta_receta(coleccion)

            elif opcion == "14":
                baja_receta(coleccion)

            elif opcion == "15":
                modificar_receta(coleccion)

            else:
                print("Opción inválida.")

        except ArchivoInvalidoError as error:
            print(f"Archivo inválido: {error}")

        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

    # cambio para usar ListaEnlazada.__iter__() y diez operaciones