from django.db import models
from .user import Usuario
from .auxiliar import Auxiliar

class Medico (models.Model):
	id= models.AutoField(primary_key=True)
	id_usuario=models.ForeignKey(Usuario, related_name='id_usuario_medico', on_delete=models.CASCADE, unique=True)
	especialidad= models.CharField(null=True, max_length=15)
	registro=models.CharField(null=True, max_length=15)
	id_registro= models.ForeignKey( Auxiliar, related_name='id_auxiliar_registro_medico', on_delete=models.SET_NULL)
	