from django.contrib import admin
from .models import Cliente, Automovil, EspacioEstacionamiento, Tarifa, AutoEspacio
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','cedula','direccion')

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Automovil)
admin.site.register(EspacioEstacionamiento)
admin.site.register(Tarifa)
admin.site.register(AutoEspacio)
