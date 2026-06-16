# Simulación del Algoritmo de Boruvka

Escenario E1 - Ciclovías UNI (Perú)

### estado inicial
- vertices:  26
- peso: 4022
- cantidad aristas: 31
  |u|v|peso (m)|
  |-|-|-|
  |0|12|206|
  |0|2|207|
  |0|1|149|
  |1|17|145|
  |1|2|118|
  |1|5|263|
  |2|3|283|
  |3|5|109|
  |3|9|128|
  |5|6|126|
  |5|18|161|
  |6|19|135|
  |6|9|114|
  |6|7|144|
  |7|20|77|
  |7|8|31|
  |8|21|97|
  |8|13|85|
  |9|11|120|
  |9|10|89|
  |10|4|102|
  |10|11|132|
  |11|8|142|
  |11|14|170|
  |13|22|88|
  |13|15|126|
  |14|15|30|
  |14|23|124|
  |15|16|61|
  |16|25|40|
  |16|24|226|

### ejecucion

`python3 caso_prueba.py`

```
--- Iteración 1 ---
  Se agrega arista 0-1 con peso 149
  Se agrega arista 1-2 con peso 118
  Se agrega arista 3-5 con peso 109
  Se agrega arista 10-4 con peso 102
  Se agrega arista 6-9 con peso 114
  Se agrega arista 7-8 con peso 31
  Se agrega arista 9-10 con peso 89
  Se agrega arista 9-11 con peso 120
  Se agrega arista 0-12 con peso 206
  Se agrega arista 8-13 con peso 85
  Se agrega arista 14-15 con peso 30
  Se agrega arista 16-25 con peso 40
  Se agrega arista 1-17 con peso 145
  Se agrega arista 5-18 con peso 161
  Se agrega arista 6-19 con peso 135
  Se agrega arista 7-20 con peso 77
  Se agrega arista 8-21 con peso 91
  Se agrega arista 13-22 con peso 88
  Se agrega arista 14-23 con peso 124
  Se agrega arista 16-24 con peso 226

--- Iteración 2 ---
  Se agrega arista 1-5 con peso 263
  Se agrega arista 5-6 con peso 126
  Se agrega arista 13-15 con peso 126
  Se agrega arista 15-16 con peso 61

--- Iteración 3 ---
  Se agrega arista 11-8 con peso 142

=== Árbol de Expansión Mínima (MST) ===
  0 - 1 : 149
  1 - 2 : 118
  3 - 5 : 109
  10 - 4 : 102
  6 - 9 : 114
  7 - 8 : 31
  9 - 10 : 89
  9 - 11 : 120
  0 - 12 : 206
  8 - 13 : 85
  14 - 15 : 30
  16 - 25 : 40
  1 - 17 : 145
  5 - 18 : 161
  6 - 19 : 135
  7 - 20 : 77
  8 - 21 : 91
  13 - 22 : 88
  14 - 23 : 124
  16 - 24 : 226
  1 - 5 : 263
  5 - 6 : 126
  13 - 15 : 126
  15 - 16 : 61
  11 - 8 : 142

Número de aristas seleccionadas: 25 (esperado N-1 = 25)
Peso total del MST: 2958
Peso total del grafo original: 4022
Reducción: 26.45%
```

### resultados
- vertices:  26
- peso: 2958
- cantidad aristas: 25
  |u|v|peso (m)|
  |-|-|-|
  |0|1|149|
  |1|2|118|
  |3|5|109|
  |10|4|102|
  |6|9|114|
  |7|8|31|
  |9|10|89|
  |9|11|120|
  |0|12|206|
  |8|13|85|
  |14|15|30|
  |16|25|40|
  |1|17|145|
  |5|18|161|
  |6|19|135|
  |7|20|77|
  |8|21|91|
  |13|22|88|
  |14|23|124|
  |16|24|226|
  |1|5|263|
  |5|6|126|
  |13|15|126|
  |15|16|61|
  |11|8|142|

### reducción 26.45%
