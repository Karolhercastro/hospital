from django.db import models
from .user import Usuario
from .auxiliar import Auxiliar


class Enfermero (models.Model):
    id = models.AutoField(primary_key=True)
    id_usuarios = models.ForeignKey(
        Usuario, related_name='id_usuario_enfermero', on_delete=models.CASCADE, unique=True)
    id_registro = models.ForeignKey(
        Auxiliar, related_name='id_registro_auxiliar_enfermero', on_delete=models.SET_NULL)
