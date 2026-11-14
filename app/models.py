from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(null=True)
    pro_pic  = models.ImageField(upload_to='profile',blank=True)
    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.CharField(max_length=20)
    age  = models.IntegerField(null=True)
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.user


class Books(models.Model):
    title = models.CharField(max_length=50)
    des = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    total = models.IntegerField()
    available = models.IntegerField()
    def __str__(self):
        return self.user
