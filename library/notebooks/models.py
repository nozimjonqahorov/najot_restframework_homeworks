from django.db import models


class Notebook(models.Model):
    BRANDS = [
        ("hp", "HP"),
        ("lenovo", "LENOVO"),
        ("acer", "ACER"),
        ("dell", "DELL"),
        ("mac", "MAC")
    ]
    brand = models.CharField(max_length=50, choices=BRANDS)
    model = models.CharField(max_length=50)
    year = models.DateField()
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.model
    
    