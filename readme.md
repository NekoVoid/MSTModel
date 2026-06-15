# Simulación del Algoritmo de Boruvka

Escenario E1 - Ciclovías UNI (Perú)

### estado inicial
- vertices:  A, B, C, D, E, F, G
- peso: 89
- cantidad aristas: 11
  |u|v|peso|
  |-|-|-|
  |A|B|7|
  |A|D|5|
  |B|C|8|
  |B|D|9|
  |B|E|6|
  |C|E|5|
  |D|E|15|
  |D|F|6|
  |E|F|8|
  |E|G|9|
  |F|G|11|

### ejecucion

`python3 caso_prueba.py`

```python

--- Iteración 1 ---
  Se agrega arista A-D con peso 5
  Se agrega arista B-E con peso 6
  Se agrega arista C-E con peso 5
  Se agrega arista D-F con peso 6
  Se agrega arista E-G con peso 9

--- Iteración 2 ---
  Se agrega arista A-B con peso 7

=== Árbol de Expansión Mínima (MST) ===
  A - D : 5
  B - E : 6
  C - E : 5
  D - F : 6
  E - G : 9
  A - B : 7

Número de aristas seleccionadas: 6 (esperado N-1 = 6)
Peso total del MST: 38
Peso total del grafo original: 89
Reducción: 57.30%
```

### resultados
- vertices:  A, B, C, D, E, F, G
- peso: 38
- cantidad aristas: 6
  |u|v|peso|
  |-|-|-|
  |A|B|7|
  |A|D|5|
  |B|E|6|
  |C|E|5|
  |D|F|6|
  |E|G|9|

### reducción 57.3%
