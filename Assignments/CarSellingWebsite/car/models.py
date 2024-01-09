from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveBigIntegerField(null=True, blank=True)
    price = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/media/uploads/', blank = True, null = True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank = True)
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
        
    