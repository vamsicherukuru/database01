from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registration(models.Model):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'))

    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128,unique=False)
    age = models.PositiveIntegerField(unique=False)
    profession = models.CharField(max_length=256)
    location = models.CharField(max_length=600)
