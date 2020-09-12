from django.db import models

class Product(models.Model):
    name = models.CharField('Name', max_length=30, help_text="Máximum of 30 Characters")
    description = models.TextField('Description', max_length=100, blank=True, help_text="Máximum of 100 Characters")
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

