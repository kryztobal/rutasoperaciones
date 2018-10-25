from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models.functions import Lower
from .models import Ruta, Operador, Despacho, Gasolina
from django.utils.html import format_html

class OperadorAdmin(admin.ModelAdmin):
    list_display = ('nombres','cedula')
    search_fields = ['nombres', 'cedula']

    def get_ordering(self, request):
        return [Lower('nombres')] 

class DespachoAdmin(admin.ModelAdmin):

    def getStatus(self, obj):
      if obj.status:
        return format_html('<p>Activo</p>')
      else:
        return format_html('<p>No activo</p>')

    getStatus.short_description = 'Status'

    list_display = ('id','getStatus', 'create_at', 'hora','unidad','ruta', 'operador','observacion',)
    list_filter = ['create_at', 'operador']
    search_fields = ('id',)
    change_list_template = 'admin/despachos/despachos_change_list.html'


admin.site.site_header = 'RUTAS OPERACIONES ADMIN'
admin.site.register(Ruta)
admin.site.register(Operador, OperadorAdmin)
admin.site.register(Despacho, DespachoAdmin)
admin.site.register(Gasolina)

admin.site.unregister(User)
admin.site.unregister(Group)