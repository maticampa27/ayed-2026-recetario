class LibroRecetas:
    def __init__(self, recetas, subrecetas):
        self.recetas = recetas
        self.subrecetas = subrecetas

    def desglosar_receta(self, receta_id):
        receta = self.recetas.get(str(receta_id))

        if receta is None:
            return

        print(receta["nombre"])

        subrecetas = self.subrecetas.get(
            str(receta_id),
            []
        )
        
        # si NO tiene 
        if len(subrecetas) == 0:
            return
        # si tiene 
        for subreceta_id in subrecetas:
            self.desglosar_receta(subreceta_id)