from django.contrib import admin
from .models import Usuario, Categoria, Transaccion

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Transaccion)

