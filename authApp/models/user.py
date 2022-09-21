
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
#manager para perfiles de usuario, sirven para procesar nuestros usuarios
#especificar funciones que sirven para manipular lo que tenemos adentro
#de los objetos de UserProfile, para crear usuarios a traves de la linea
#de comandos

	def create_user (self, username, password=None):
		#crear nuevo perfil de usario
		if not username:
			raise ValueError('Usuario debe tener un nombre de usuario')

		user = self.model(username=username)		
		user.set_password(password)
		user.save(using=self._db)
   
		return user

	def create_superuser(self, username, password):
		user= self.create_user(
      	username = username,
        password= password,
        )
  
		user.is_admin= True
		user.save(using=self._db)

		return user
     

class User(AbstractBaseUser, PermissionsMixin):
    #modelo Base de datos para usuarios en el sistema
    id= models.BigAutoField(primary_key=True)
    username= models.CharField('Username', max_length=20, unique=True)
    password= models.CharField('Password',max_length=20 )
    create_date= models.DateField('Create date')
    activo = models.BooleanField(default=True)
    nombre= models.CharField('nombre',max_length=30 )
    apellido = models.CharField('apellidos',max_length=30 )
    correo= models.EmailField('correo',max_length=100)
    telefono= models.CharField('telefono', max_length=30)
    

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'
