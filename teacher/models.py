from django.db import models


# Create your models here.
class Teacher_dashboard(models.Model):
    link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
class Teacher_profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    course = models.CharField(max_length=50, default='Default Course')


    def __str__(self):
        return self.username