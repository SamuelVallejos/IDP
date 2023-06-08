from rest_framework import serializers
from LineApp.models import Lineup


class LineupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lineup
        fields = ['idLine', 'titulo', 'descripcion', 'agente', 'mapa', 'bando',
        'incorporacion', 'like', 'dislike', 'fecha', 'usuario']