from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Generic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mtypes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')
    brandName = models.CharField(max_length=100, default='')
    generic = models.CharField(max_length=100, default='')
    pricePerTablet = models.FloatField(default=0.0)
    mtype = models.CharField(max_length=100, default='tablet')
    expireDate = models.DateField(auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name

