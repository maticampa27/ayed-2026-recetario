class Receta:
    def __init__(self, id, nombre, tiempo_min, dificultad, categoria):
        self.id = int(id)
        self.nombre = nombre
        self.tiempo_min = int(tiempo_min)
        self.dificultad = dificultad
        self.categoria = categoria

    def __str__(self):
        return self.nombre