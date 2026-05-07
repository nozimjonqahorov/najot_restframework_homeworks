from django.db import models

# Create your models here.
class Student(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.f_name