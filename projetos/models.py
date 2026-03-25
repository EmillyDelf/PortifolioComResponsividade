from django.db import models
from usuario.models import Usuario

class Projeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    link = models.URLField(blank=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo