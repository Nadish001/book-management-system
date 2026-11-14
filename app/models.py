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
    GENRE_CHOICES = [
        ('fantasy', 'Fantasy'),
        ('scifi', 'Science Fiction'),
        ('mystery', 'Mystery / Thriller'),
        ('romance', 'Romance'),
        ('history', 'History'),
        ('biography', 'Biography / Memoir'),
        ('selfhelp', 'Self-help'),
        ('business', 'Business / Finance'),
        ('tech', 'Technology / Programming'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=50)
    des = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other')
    author = models.CharField(max_length=20)
    price = models.IntegerField()
    cover_pic = models.ImageField(upload_to='coverpage',blank=True)
    def __str__(self):
        return self.user
