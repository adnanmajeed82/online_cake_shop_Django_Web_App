# cakes/models.py
from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='cake_images/', null=True, blank=True)

    def __str__(self):
        return self.name
