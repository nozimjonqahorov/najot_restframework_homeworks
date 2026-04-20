from django.db import models

# Create your models here.


class Phone(models.Model):
    BRANDS = [
        ("sumsung", "SUMSUNG"),
        ("readme", "README"),
        ("honor", "HONOR"),
        ("iphone", "IPHONE"),
        ("boshqa", "Boshqa")
    ]
    brand = models.CharField(max_length=50, choices=BRANDS)
    model = models.CharField(max_length=50)
    year = models.DateField()
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.model
    
    