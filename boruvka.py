

class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}

    def encontrar(self, v):
        if self.padre[v] != v:
            self.padre[v] = self.encontrar(self.padre[v])
        return self.padre[v]

    def unir(self, u, v):
        raiz_u, raiz_v = self.encontrar(u), self.encontrar(v)
        if raiz_u == raiz_v:
            return False
        if self.rango[raiz_u] < self.rango[raiz_v]:
            raiz_u, raiz_v = raiz_v, raiz_u
        self.padre[raiz_v] = raiz_u
        if self.rango[raiz_u] == self.rango[raiz_v]:
            self.rango[raiz_u] += 1
        return True


def boruvka(vertices, aristas):
    uf = UnionFind(vertices)
    mst = []
    num_componentes = len(vertices)
    iteracion = 0

    while num_componentes > 1:
        iteracion += 1
        print(f"\n--- Iteración {iteracion} ---")
        mas_barata = {v: None for v in vertices}

        # Buscar la arista más barata de cada componente
        for arista in aristas:
            u, v, peso = arista
            raiz_u, raiz_v = uf.encontrar(u), uf.encontrar(v)
            if raiz_u == raiz_v:
                continue
            if mas_barata[raiz_u] is None or mas_barata[raiz_u][2] > peso:
                mas_barata[raiz_u] = arista
            if mas_barata[raiz_v] is None or mas_barata[raiz_v][2] > peso:
                mas_barata[raiz_v] = arista

        # Fusionar componentes con sus aristas más baratas
        for v in vertices:
            arista = mas_barata[v]
            if arista is None:
                continue
            u, w, peso = arista
            if uf.unir(u, w):
                mst.append(arista)
                num_componentes -= 1
                print(f"  Se agrega arista {u}-{w} con peso {peso}")

    return mst