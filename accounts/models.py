from django.db import models
from django.contrib.auth.models import AbstractUser

#MyUser 만들기
class MyUser(AbstractUser):
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
