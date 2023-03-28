from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField()


    def __str__(self) -> str:
        return self.name