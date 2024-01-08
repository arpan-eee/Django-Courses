from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/media/uploads',blank=True,null=True)

    def __str__(self):
        return f"{self.title}"