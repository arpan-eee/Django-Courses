from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField
    father_name = models.TextField(default='Rahim')

    def __str__(self):
        return f"{self.roll}  {self.name}  {self.father_name}"