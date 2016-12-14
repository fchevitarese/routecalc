# encoding: utf-8
from django.shortcuts import render

from rest_framework import viewsets

from .models import Rota
from .serializers import RotaSerializer


class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer


class MenorFreteViewSet()