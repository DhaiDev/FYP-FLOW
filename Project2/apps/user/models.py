from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserInfo(AbstractUser):
    id = models.AutoField(primary_key=True) #pk
    username = models.CharField(
        'username',
        max_length=26,
        unique=True
    )
    password = models.CharField(
        'password',
        max_length=128
    )
    created = models.DateTimeField(auto_now_add=True)
    matrix = models.CharField(max_length=128,null=True,blank=True,default=None, db_column='pmj_id')
