from django.db import models

# Create your models here.

class EleProduct(models.Model):
    name = models.CharField(max_length = 50)
    qunetity = models.IntegerField()
    price = models.FloatField()


    def __str__(self):
        return f"{self.name}"
    
    