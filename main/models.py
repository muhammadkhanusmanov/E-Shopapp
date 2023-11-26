from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='categoryimge')
