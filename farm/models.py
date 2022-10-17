from django.db import models
from common.models import CustomUser

class Aduino(models.Model):
    useridx = models.IntegerField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    devicer= models.IntegerField()
    temp = models.IntegerField()
    hum = models.IntegerField()
    illum = models.IntegerField()
    waterCycle= models.IntegerField()
    nowtemp = models.IntegerField()
    nowhum = models.IntegerField()
    nowillum = models.IntegerField()
    nowwaterCycle= models.IntegerField()
    