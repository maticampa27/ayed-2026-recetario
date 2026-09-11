from src.config import TEMA
from src.persistencia.recetas_csv import cargar_recetas

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
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        if opcion == "1":
            recetas = cargar_recetas()
            mostrar_recetas(recetas)
        elif opcion in {"2", "3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
