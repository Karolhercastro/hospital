from django.db import models
from .user import Usuario
from .auxiliar import Auxiliar
from .medico import Medico


class Paciente (models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, related_name='id_usuario_paciente', on_delete=models.CASCADE, unique=True)
    fecha_creacion = models.DateField('create_date')
    direccion = models.CharField('residencia', max_length=50)
    ciudad = models.CharField('ciudad', max_length=20)
    id_registro = models.ForeignKey(
        Auxiliar, related_name='id_auxiliar_registro_paciente', on_delete=models.SET_NULL)
    id_medico = models.ForeignKey(
        Medico, related_name='id_paciente_medico', on_delete=models.SET_NULL)
