from django.contrib import admin
from AppDemo.models import Producto,Usuario


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'talla', 'color', 'email','estado']

# Register your models here.
admin.site.register(Producto)

class UsuarioAdmin:
    list_display = ['nombre','email','contraseña']

admin.site.register(Usuario)

