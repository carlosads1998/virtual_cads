from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models

def upload_image_jogos(instance,filename):
    return f'{instance.nome}-{filename}'


class Base(models.Model):
    titulo= models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class jogos(Base):
    CAT_CHOICES= (
        ('Ação', 'Ação'),
        ('Esportes', 'Esportes'),
        ('Terror', 'Terror'),
        ('RPG', 'RPG'),
    )
    STS_CHOICES= (
        ('Em Estoque', 'Em Estoque'),
        ('Acabou', 'Acabou'),
    )
    nome = models.CharField(max_length=60)
    descricao=models.TextField(max_length=120, blank=True)
    category= models.CharField(max_length=1, choices=CAT_CHOICES)
    status= models.CharField(max_length=1, choices=STS_CHOICES)
    preco = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to=upload_image_jogos, blank=True, null = True)
    
    
    class Meta:
        verbose_name= 'Jogo'
        verbose_name_plural= 'Jogos'
        
        def __str__(self):
            return self.nome
        
        
        