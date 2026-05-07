from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=22, decimal_places=3)
    