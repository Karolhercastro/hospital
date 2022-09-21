from django.db import models
from .user import Usuario
from .auxiliar import Auxiliar


class Familiar (models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, related_name='id_usuario_familiar', on_delete=models.CASCADE, unique=True)
    create_date = models.DateField('create_date')
    relacion = models.CharField(max_length=20)
    id_registro = models.ForeignKey(
        Auxiliar, related_name='id_auxiliar_registro_familiar', on_delete=models.CASCADE)
