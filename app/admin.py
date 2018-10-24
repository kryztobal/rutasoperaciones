from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models.functions import Lower
from .models import Ruta, Operador, Activa, Gasolina

class OperadorAdmin(admin.ModelAdmin):
    list_display = ('nombres','cedula')
    search_fields = ['nombres', 'cedula']

    def get_ordering(self, request):
        return [Lower('nombres')] 

class ActivaAdmin(admin.ModelAdmin):
    list_display = ('hora','unidad','ruta', 'operador', 'kilometraje', 'gasolina', 'servicio','create_at')
    list_filter = ['create_at']
    search_fields = ('create_at','unidad', 'ruta', 'operador')

admin.site.site_header = 'RUTAS OPERACIONES ADMIN'
admin.site.register(Ruta)
admin.site.register(Operador, OperadorAdmin)
admin.site.register(Activa, ActivaAdmin)
admin.site.register(Gasolina)

admin.site.unregister(User)
admin.site.unregister(Group)