from django.db import models


class Unit(models.TextChoices):
    ML = "ml", "Milliliter"
    GRAM = "g", "Gram"
    PIECE = "piece", "Piece"


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=10, choices=Unit.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock")
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
