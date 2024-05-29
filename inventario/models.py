from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    azure_image_url = models.URLField(max_length=500, default='')

    def __str__(self):
        return self.name
