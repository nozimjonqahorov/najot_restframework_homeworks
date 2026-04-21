from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    profession = models.CharField()
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name