# coding=utf-8
from django.conf.urls import url, include
from rest_framework import routers

from .views import RotaViewSet

app_name = 'rotas'

router = routers.DefaultRouter()
router.register(r'rotas', RotaViewSet, base_name='rotas')

urlpatterns = [
    url(r'', include(router.urls)),
]
