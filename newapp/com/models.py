from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=500)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    date = models.DateField()
    image = models.URLField(default="")

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name