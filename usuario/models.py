from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)

    def __str__(self):
        return self.nome
    
"-----------------------------------------------------"

class Habilidade(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nome