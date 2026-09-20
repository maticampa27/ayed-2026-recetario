# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:Recetario
- Por qué lo eligieron (5–8 líneas):sentimos que es el tema más adecuado para las capacidades del grupo y todos podemos aportar de igual forma

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

```text
Un ítem del catálogo es una entidad individual que forma parte del catálogo. en nuestro caso una receta
Un objeto mutable es uno que podemos modificar después de crearlo(Como un dict) y Un objeto inmutable no puede modificarse una vez creado(Como los str, int, float y tuple)
En nuestro recetario, cada receta es un ítem del catálogo. 
El catálogo contiene todas las recetas disponibles.
 A partir de esas recetas podemos armar el menú de la semana
, que es nuestra colección principal. La pila guarda el historial de recetas cocina das y funciona LIFO, mientras que la cola guarda las recetas pendientes de preparaci
ón y funciona .FIFO

```

## 3. Recursión (E2)

## 3. Recursión (E2)

La recursión se utiliza para recorrer las subrecetas de una receta.

```python
subrecetas = self.subrecetas.get(receta_id, [])

if len(subrecetas) == 0:
    return

for subreceta_id in subrecetas:
    self.desglosar_receta(subreceta_id)
```

**Primer caso:** la receta no tiene subrecetas, por lo que la función termina.

**Segundo caso:** la receta tiene subrecetas y la función se vuelve a llamar para cada una.

Ejemplo con la receta 10:

```text
desglosar_receta(10)
├── desglosar_receta(3) → No tiene
└── desglosar_receta(5) → No tiene
```

La relación entre recetas y subrecetas se obtiene de `data/subrecetas.csv`.

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
