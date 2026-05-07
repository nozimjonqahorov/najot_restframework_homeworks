from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=30)

   def __str__(self):
       return self.name
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title 