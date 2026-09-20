def desglosar_receta(self, receta_id):
    receta = self.recetas[receta_id]

    print(receta.nombre)

    subrecetas = self.subrecetas.get(receta_id, [])

    # si NO tiene 
    if len(subrecetas) == 0:
        return

    # si tiene 
    for subreceta_id in subrecetas:
        self.desglosar_receta(subreceta_id)