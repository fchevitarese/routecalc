# encoding: utf-8
from dry.helpers import Mapa, menor_caminho
from .models import Rota

class RouteNotFound(Exception):
    pass


def calcula_menor_frete(nome, origem, destino, autonomia, preco):
    """Calcula o menor custo do frete."""
    result = {}

    try:
        distancia, caminho = calcula_menor_caminho(nome, origem, destino)
        result['nome'] = nome
        result['origem'] = origem
        result['destino'] = destino
        result['autonomia'] = autonomia
        result['preco'] = preco
        result['caminho'] = caminho
        result['distancia'] = distancia
        result['valor_frete'] = float(distancia) * float(preco) / float(autonomia)
    except TypeError:
        result['error'] = u'Distância, preço do combustível e autonomia devem ser numéricos'
    except ValueError:
        result['error'] = u'Rota não encontrada'

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
