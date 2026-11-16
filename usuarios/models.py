from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)

    
    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username
