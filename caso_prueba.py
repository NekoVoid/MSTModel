"""
Simulación del Algoritmo de Boruvka
Escenario E1 - Ciclovías UNI (Perú)
"""

from boruvka import boruvka

if __name__ == "__main__":
    vertices = list(range(26))

    aristas = [
        (0, 12, 206),
        (0, 2, 207),
        (0, 1, 149),
        (1, 17, 145),
        (1, 2, 118),
        (1, 5, 263),
        (2, 3, 283),
        (3, 5, 109),
        (3, 9, 128),
        (5, 6, 126),
        (5, 18, 161),
        (6, 19, 135),
        (6, 9, 114),
        (6, 7, 144),
        (7, 20, 77),
        (7, 8, 31),
        (8, 21, 97),
        (8, 13, 85),
        (9, 11, 120),
        (9, 10, 89),
        (10, 4, 102),
        (10, 11, 132),
        (11, 8, 142),
        (11, 14, 170),
        (13, 22, 88),
        (13, 15, 126),
        (14, 15, 30),
        (14, 23, 124),
        (15, 16, 61),
        (16, 25, 40),
        (16, 24, 226),
    ]

    mst = boruvka(vertices, aristas)

    print("\n=== Árbol de Expansión Mínima (MST) ===")
    peso_total = 0
    for u, v, peso in mst:
        print(f"  {u} - {v} : {peso}")
        peso_total += peso

    print(f"\nNúmero de aristas seleccionadas: {len(mst)} (esperado N-1 = {len(vertices)-1})")
    print(f"Peso total del MST: {peso_total}")

    peso_original = sum(p for _, _, p in aristas)
    print(f"Peso total del grafo original: {peso_original}")
    print(f"Reducción: {100*(1 - peso_total/peso_original):.2f}%")