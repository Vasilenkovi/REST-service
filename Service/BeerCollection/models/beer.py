from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .shop import Shop


class Beer(models.Model):
    name = models.CharField(max_length=50)
    package = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    based = models.BooleanField(default=False)
    flavorCommentary = models.TextField()
    disadvantages = models.TextField()
    mark = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    shop = models.ForeignKey(Shop, related_name="Beer", on_delete=models.CASCADE)
