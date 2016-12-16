# encoding: utf-8
from django.db import models
from dry.models import BaseModel
from dry.helpers import Mapa, menor_caminho


class Rota(BaseModel):
    nome = models.CharField(max_length=5, verbose_name='Nome da rota',
                            blank=True, null=True)
    origem = models.CharField(max_length=10, verbose_name='Origem')
    destino = models.CharField(max_length=10, verbose_name='Destino')
    distancia = models.IntegerField(verbose_name='Distância')

    def __str__(self):
        return "{0} -> {1}: {2}".format(self.origem,
                                        self.destino,
                                        self.distancia)


