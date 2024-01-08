from django.db import models

# Create your models here.

class Musician(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    instrument = models.CharField(max_length=50)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"