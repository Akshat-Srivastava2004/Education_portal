from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student_profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50, default='Default Course')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"