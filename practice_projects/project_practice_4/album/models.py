from django.db import models
from musician.models import Musician

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=20,choices=(('1','1'), ('2','2'), ('3','3'), ('4','4'),('5','5')))

    def __str__(self):
        return self.name
