from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    reenter_Password = models.CharField(max_length=20)

