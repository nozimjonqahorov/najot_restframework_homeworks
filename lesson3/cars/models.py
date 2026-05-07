from django.db import models

# Create your models here.
class Car(models.Model):
    BRANDS = [
        ("mers", "MERS"),
        ("bmw", "BMW"),
        ("audi", "AUDI"),
        ("boshqa", "BOSHQA")
    ]
    model = models.CharField(max_length=70)
    brand = models.CharField(max_length=50, choices=BRANDS, default="boshqa")
    year = models.DateField()
    max_speed = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return self.model
    