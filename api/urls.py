from django.urls import path
from .views import jogosAPIView, jogoAPIView

urlpatterns = [
    path('jogos/', jogosAPIView.as_view(), name='jogos'),
    path('jogos/<int:pk>/', jogoAPIView.as_view(), name='jogo'),
]
