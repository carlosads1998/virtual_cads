from django.contrib import admin
from .models import jogos

@admin.register(jogos)
class jogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'category', 'descricao', 'status', 'preco', 'image')
