# encoding: utf-8
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import Rota
from .helpers import calcula_menor_frete
from .serializers import RotaSerializer, MenorRotaSerializer


class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer

    @list_route(methods=['get'])
    def menor_frete(self, request):
        """Metodo para calcular o menor frete.

        Recebe via query_params os valores para executar os cálculos.
        Ex.:
        http://localhost:8000/api/rotas/menor_frete/?nome=MG&origem=A&destino=D&autonomia=10&preco=2.50
        """
        try:
            params = request.query_params
            nome = params['nome']
            origem = params['origem']
            destino = params['destino']
            autonomia = params['autonomia']
            preco = params['preco']

            menor_frete = calcula_menor_frete(
                nome,
                origem,
                destino,
                autonomia,
                preco
            )
            serializer = MenorRotaSerializer(menor_frete)

            return Response(serializer.data)
        except MultiValueDictKeyError:
            return Response({'result': 'Parâmetros incorretos. '})

