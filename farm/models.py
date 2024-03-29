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

class Question(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()