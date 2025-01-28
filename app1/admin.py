from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha_envio')  # Columnas visibles en el admin
    list_filter = ('fecha_envio',)  # Filtro lateral
    search_fields = ('nombre', 'email', 'mensaje')  # Barra de búsqueda