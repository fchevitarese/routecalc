# encoding: utf-8
from dry.helpers import Mapa, menor_caminho
from .models import Rota


def calcula_menor_frete(origem, destino, autonomia, preco):
    """Calcula o menor custo do frete."""
    distancia, caminho = calcula_menor_caminho(origem, destino)

    custo = distancia * preco / autonomia
    return "O menor frete é {0} e o caminho é {1}".format(custo, caminho)


def calcula_menor_caminho(origem, destino):
    """Retorna o menor caminho entre os dois pontos."""
    mapa = Mapa()
    rotas = Rota.objects.all()

    for rota in rotas:
        mapa.add_ponto(rota.origem)
        mapa.add_rota(rota.origem,
                      rota.destino,
                      rota.distancia)
    return menor_caminho(mapa, origem, destino)
