# encoding: utf-8
from dry.helpers import Mapa, menor_caminho
from .models import Rota


def calcula_menor_frete(nome, origem, destino, autonomia, preco):
    """Calcula o menor custo do frete."""
    distancia, caminho = calcula_menor_caminho(nome, origem, destino)

    result = {}
    try:
        result['nome'] = nome
        result['origem'] = origem
        result['destino'] = destino
        result['autonomia'] = autonomia
        result['preco'] = preco
        result['caminho'] = caminho
        result['distancia'] = distancia
        result['valor_frete'] = float(distancia) * float(preco) / float(autonomia)

        return result
    except TypeError:
        result['error'] = 'Distância, preço do combustível e autonomia devem ser numéricos'
        return result


def calcula_menor_caminho(nome, origem, destino):
    """Retorna o menor caminho entre os dois pontos."""
    mapa = Mapa()
    rotas = Rota.objects.filter(nome=nome)

    for rota in rotas:
        mapa.add_ponto(rota.origem)
        mapa.add_rota(rota.origem,
                      rota.destino,
                      rota.distancia)
    return menor_caminho(mapa, origem, destino)
