from django.contrib import admin

from .models.user import User
from .models.auxiliar import Auxiliar
from .models.paciente import Paciente
from .models.familiar import Familiar
from .models.medico import Medico
from .models.enfermero import Enfermero
from .models.historia import Historia
from .models.signos import Signos



admin.site.register(User)
admin.site.register(Auxiliar)
admin.site.register(Paciente)
admin.site.register(Familiar)
admin.site.register(Medico)
admin.site.register(Enfermero)
admin.site.register(Historia)
admin.site.register(Signos)
