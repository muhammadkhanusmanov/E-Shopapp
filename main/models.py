from django.db import models

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


