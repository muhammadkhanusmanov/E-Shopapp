from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    name = models.CharField(max_length=50)
    img_url = models.TextField()

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=70)
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    description = models.TextField()
    image_url = models.TextField()
    image_url2 = models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class UsersProduct(models.Model):
    product = models.ManyToManyField(Products)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quanity = models.CharField(max_length=75)
    extra_number = models.CharField(max_length=25)
    longitude = models.CharField(max_length=75)
    latitude = models.CharField(max_length=75)
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username} {self.product.name}'

class MarketProduct(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.URLField(max_length=175)
    products = models.ManyToManyField(Products)

    def __str__(self) -> str:
        return self.name

class RecomntsProduct(models.Model):
    products = models.ManyToManyField(Products)




