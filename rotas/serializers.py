# encoding: utf-8
from rest_framework import serializers
from .models import Rota


class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ('nome', 'origem', 'destino', 'distancia',
                  'created', 'updated')


class MenorRotaSerializer(serializers.Serializer):
    nome = serializers.CharField()
    origem = serializers.CharField()
    destino = serializers.CharField()
    autonomia = serializers.IntegerField()
    preco = serializers.FloatField()
    valor_frete = serializers.FloatField()
    caminho = serializers.CharField()
    distancia = serializers.IntegerField()
