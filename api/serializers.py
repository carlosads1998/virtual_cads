from pyexpat import model
from rest_framework import serializers
from .models import jogos

class jogosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'nome',
            'category',
            'descricao',
            'status',
            'preco',
            'image',
        )
        model= jogos