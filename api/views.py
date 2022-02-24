from django.shortcuts import render
from rest_framework import generics
from .serializers import jogosSerializer
from .models import jogos
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class jogosAPIView(generics.ListCreateAPIView):
    queryset= jogos.objects.all()
    serializer_class=jogosSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['id','nome']

class jogoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = jogos.objects.all()
    serializer_class= jogosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields= ['id','nome' ]