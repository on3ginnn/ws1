from django.db import models

class Catalog(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255)
    disc = models.TextField()
    price = models.FloatField()
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title