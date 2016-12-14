# encoding: utf-8
from rest_framework import serializers
from .models import Rota


class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ('origem', 'destino', 'distancia', 'created', 'updated')


class MenorRotaSerializer(serializers.Serializer):
    origem = serializers.CharField()
    destino = serializers.CharField()
    autonomia = serializers.IntegerField()
    preco = serializers.IntegerField()

