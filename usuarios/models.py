from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Usuario'
