from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    address = models.TextField()
    
class devicer(models.Model):
    device = models.IntegerField()