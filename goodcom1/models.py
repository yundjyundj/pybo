from django.db import models


class Comtextbook(models.Model):
    title1 = models.CharField(max_length=20)
    title2 = models.CharField(max_length=30)
    title3 = models.CharField(max_length=40)
    text1 = models.TextField()
    quiz1 = models.TextField()
    
# Create your models here.
