from django.contrib import admin
from .models import CustomUser  # Importe o modelo de usuário personalizado

# Registre o modelo de usuário personalizado
admin.site.register(CustomUser)
