# encoding: utf-8
from django.db import models
from dry.models import BaseModel


class Rota(BaseModel):
    u"""Armazena o mapa com os seus pontos e distâncias."""
    nome = models.CharField(max_length=5, verbose_name='Nome da rota',
                            blank=True, null=True)
    origem = models.CharField(max_length=10, verbose_name='Origem')
    destino = models.CharField(max_length=10, verbose_name='Destino')
    distancia = models.IntegerField(verbose_name='Distância')

    def __str__(self):
        return "{0} -> {1}: {2}".format(self.origem,
                                        self.destino,
                                        self.distancia)

    def save(self, *args, **kwargs):
        # Passando os pontos e o nome do mapa para maiúscolo no db.
        self.nome = self.nome.upper()
        self.origem = self.origem.upper()
        self.destino = self.destino.upper()
        super(Rota, self).save(*args, **kwargs)


