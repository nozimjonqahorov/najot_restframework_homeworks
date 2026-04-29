from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    experience = models.PositiveIntegerField()
    age = models.PositiveIntegerField()


    def __str__(self):
        return self.full_name
    


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField()


    def __str__(self):
        return self.full_name
    
class Lesson(models.Model):
    title = models.CharField(max_length=100)   
    description = models.TextField()                
    duration = models.PositiveIntegerField()     
    is_published = models.BooleanField(default=True) 

    def __str__(self):
        return self.title