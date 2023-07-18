from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.name
