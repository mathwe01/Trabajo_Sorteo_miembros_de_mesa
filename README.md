# Sorteo y asignación de miembros de mesa y observadores

Prototipo en **Python** para el desafío final de *Fundamentos de Programación* (CIIN1205P, UPN).

El sistema reemplaza el armado manual de las mesas de sufragio: registra electores,
valida sus datos, los busca por DNI, los ordena y **sortea** los miembros de mesa
(3 titulares y 6 suplentes) y los observadores de cada mesa. Todo queda guardado
en archivos de texto.

> Los datos de `data/electores.txt` son **ficticios**. No corresponden a personas reales.

## Cómo ejecutarlo

Requisitos: Python 3.8 o superior. No necesita instalar nada más.

```
python main.py                       # programa con menú
python pruebas/casos_prueba.py       # casos de prueba
```

## Estructura

```
main.py                 menú y flujo del programa
src/validaciones.py     validación de DNI, nombre, edad, mesa, etc.
src/archivos.py         lectura y escritura de archivos de texto
src/electores.py        registrar, buscar (secuencial y binaria), ordenar (burbuja y selección)
src/sorteo.py           preselección, sorteo de miembros, asignación de observadores
pruebas/casos_prueba.py casos de prueba automáticos
data/electores.txt      padrón de ejemplo (datos ficticios)
docs/pseudocodigo.md    pseudocódigo de los algoritmos
```

Archivos que genera el programa dentro de `data/`:

- `asignaciones.txt`: resultado de los sorteos (`MESA|ROL|DNI`).
- `registro_sorteos.txt`: fecha, alcance y semilla de cada sorteo (auditoría).

## Reglas del sorteo (simplificadas)

- Cada mesa: 3 titulares (presidente, secretario, tercer miembro) y 6 suplentes.
- No pueden ser miembros: observadores acreditados ni quienes sirvieron 2 o más veces en 5 años.
- Se preselecciona hasta 25 electores por mayor grado de instrucción y menos veces servidas; luego se sortea entre ellos con igual probabilidad.
- Cada observador se asigna a una mesa distinta de la suya, repartidos de forma equilibrada.
- Cada sorteo guarda su semilla: con la misma semilla y los mismos datos se obtiene el mismo resultado.

## Formato de los archivos

```
electores.txt:   DNI|APELLIDOS Y NOMBRES|EDAD|MESA|INSTRUCCION|VECES_MIEMBRO|OBSERVADOR
asignaciones.txt: MESA|ROL|DNI
```

Grado de instrucción: 1 Primaria, 2 Secundaria, 3 Técnica, 4 Universitaria.

## Integrantes

Completar con los nombres del grupo y el rol de cada uno.
