# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |pasa  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |pasa  |  |
| P03 | E2      | Recorrer una receta con subrecetas    | Receta 10  | Se recorren sus subrecetas 3 y 5        | pasa |
| P04 | E2      | Recorrer una receta sin subrecetas    | Receta 3   | Termina en el caso base                 | pasa |
| P05 | E2      | Recorrer una receta con una subreceta | Receta 13  | Se recorre su subreceta 6               | pasa |
| P06 | E2      | Recorrer otra receta con subreceta    | Receta 17  | Se recorre su subreceta 8               | pasa |
| P07 | E2      | Recorrer una receta inexistente       | ID 999     | Se informa que no existe                | pasa |
| P08 | E2      | Recorrer dos recetas consecutivamente | ID 10 y 13 | Ambos recorridos terminan correctamente | pasa |
| P09 | E4      | Búsqueda lineal de un nombre existente   | Asado               | Encuentra la receta                          | pasa      |       |
| P10 | E4      | Búsqueda lineal de un nombre inexistente | Pizza inexistente   | Informa que no existe                        | pasa      |       |
| P11 | E4      | Búsqueda binaria                         | Asado               | Encuentra la receta en catálogo ordenado     | pasa      |       |
| P12 | E4      | Ordenar por nombre                       | Catálogo de recetas | Las recetas quedan ordenadas alfabéticamente | pasa      |       |
| P13 | E5 | Guardar catálogo en texto, salir y volver a cargarlo | Catálogo de recetas | Los datos siguen disponibles después de cerrar y abrir el programa | pasa |  |
| P14 | E5 | Guardar binario y modificar un registro por posición | Una receta existente | Al recargar, el campo modificado conserva el nuevo valor | pasa |  |
| P15 | E5 | Abrir un binario truncado o con magia incorrecta | Archivo binario inválido | Se produce `ArchivoInvalidoError` | pasa |  |

comprobados nuevamente luego de cambios en E6



