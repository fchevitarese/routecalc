# encoding: utf-8
from django.db import models
from dry.models import BaseModel
from dry.helpers import Mapa, menor_caminho


class Rota(BaseModel):
    origem = models.CharField(max_length=10, verbose_name='Origem')
    destino = models.CharField(max_length=10, verbose_name='Destino')
    distancia = models.IntegerField()

    def __str__(self):
        return "{0} -> {1}: {2}".format(self.origem,
                                        self.destino,
                                        self.distancia)


