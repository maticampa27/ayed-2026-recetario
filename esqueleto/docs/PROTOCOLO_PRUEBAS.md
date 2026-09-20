# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |no corrido  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |no corrido  |  || P03 | E2      | Recorrer una receta con subrecetas    | Receta 10  | Se recorren sus subrecetas 3 y 5        | no corrido |
| P04 | E2      | Recorrer una receta sin subrecetas    | Receta 3   | Termina en el caso base                 | no corrido |
| P05 | E2      | Recorrer una receta con una subreceta | Receta 13  | Se recorre su subreceta 6               | no corrido |
| P06 | E2      | Recorrer otra receta con subreceta    | Receta 17  | Se recorre su subreceta 8               | no corrido |
| P07 | E2      | Recorrer una receta inexistente       | ID 999     | Se informa que no existe                | no corrido |
| P08 | E2      | Recorrer dos recetas consecutivamente | ID 10 y 13 | Ambos recorridos terminan correctamente | no corrido |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
