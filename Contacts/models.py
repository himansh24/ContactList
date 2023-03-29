from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    owner=     models.ForeignKey(to=User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=30)
    last_name=  models.CharField(max_length=15)
    country=     models.CharField(max_length=10)
    phone_no =  models.CharField(max_length=10)


# Create your models here.
