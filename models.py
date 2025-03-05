from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name