# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    # Adicione campos personalizados, se necessário

    def __str__(self):
        return self.username

    # Aqui você pode adicionar os relacionamentos ManyToManyField com as permissões e grupos personalizados,
    # mas não defina novamente a classe Meta, já que ela é herdada de AbstractUser

    # Exemplo: adicionar relacionamento ManyToManyField para permissões personalizadas
    custom_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_permissions')

    # Exemplo: adicionar relacionamento ManyToManyField para grupos personalizados
    custom_groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_groups')
