from django.contrib import admin
from .models import Rota


class AdminRota(admin.ModelAdmin):
    list_display = ('nome', 'origem', 'destino', 'distancia')
    list_filter = ('nome', )
admin.site.register(Rota, AdminRota)