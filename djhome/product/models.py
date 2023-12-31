from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name