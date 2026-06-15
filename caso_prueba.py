"""
Simulación del Algoritmo de Boruvka
Escenario E1 - Ciclovías UNI (Perú)
"""

from boruvka import boruvka

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    aristas = [
        ('A', 'B', 7),
        ('A', 'D', 5),
        ('B', 'C', 8),
        ('B', 'D', 9),
        ('B', 'E', 6),
        ('C', 'E', 5),
        ('D', 'E', 15),
        ('D', 'F', 6),
        ('E', 'F', 8),
        ('E', 'G', 9),
        ('F', 'G', 11),
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