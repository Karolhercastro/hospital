from django.db import models
from .user import Usuario

class Auxiliar (models.Model):
	id= models.AutoField(primary_key=True)
	cargo = models.CharField(max_length=20)
	id_usuario = models.ForeignKey(Usuario, related_name='id_usuario_auxiliar',  on_delete=models.CASCADE, unique=True)
	