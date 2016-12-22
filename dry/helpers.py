# encoding: utf-8
from collections import defaultdict, deque


class Mapa(object):
    def __init__(self):
        self.pontos = set()
        self.rotas = defaultdict(list)
        self.distancias = {}

    def add_ponto(self, valor):
        """Adiciona o ponto."""
        self.pontos.add(valor)

    def add_rota(self, origem, destino, distancia):
        """Adiciona a rota de origem, destino e distância"""
        self.rotas[origem].append(destino)
        self.rotas[destino].append(origem)
        self.distancias[(origem, destino)] = distancia


def dijkstra(mapa, inicio):
    visited = {inicio: 0}
    path = {}

    pontos = set(mapa.pontos)

    while pontos:
        menor_ponto = None
        for ponto in pontos:
            if ponto in visited:
                if menor_ponto is None:
                    menor_ponto = ponto
                elif visited[ponto] < visited[menor_ponto]:
                    menor_ponto = ponto
        if menor_ponto is None:
            break

        pontos.remove(menor_ponto)
        distancia_atual = visited[menor_ponto]

        for rota in mapa.rotas[menor_ponto]:
            try:
                distancia = distancia_atual + mapa.distancias[(menor_ponto,
                                                               rota)]
            except KeyError:
                continue
            if rota not in visited or distancia < visited[rota]:
                visited[rota] = distancia
                path[rota] = menor_ponto

    return visited, path


def menor_caminho(mapa, origem, destino):
    """Função que retorna o percurso com menor distância entre 2 pontos."""
    visitados, caminhos = dijkstra(mapa, origem)
    caminho_completo = deque()
    _destination = caminhos[destino]

    while _destination != origem:
        caminho_completo.appendleft(_destination)
        _destination = caminhos[_destination]

    caminho_completo.appendleft(origem)
    caminho_completo.append(destino)

    return visitados[destino], list(caminho_completo)
