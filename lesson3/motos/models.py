from django.db import models

# Create your models here.
class Moto(models.Model):
    BRANDS = [
        ("honda", "HONDA"),
        ("bmw", "BMW"),
        ("suzuki", "SUZUKI"),
        ("boshqa", "BOSHQA")
    ]
    model = models.CharField(max_length=60)
    brand = models.CharField(max_length=50, choices=BRANDS, default="boshqa")
    year = models.DateField()
    max_speed = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    photo = models.ImageField(upload_to="motos/", default="motos/default_moto.png", blank=True, null=True)\
    
    def __str__(self):
        return self.model
    
    