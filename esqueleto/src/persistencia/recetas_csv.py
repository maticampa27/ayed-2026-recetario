import csv

def cargar_recetas():
    recetas = []

    with open("data/recetas.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            recetas.append(fila)

    return recetas