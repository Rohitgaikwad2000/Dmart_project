from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    packaging_date = models.DateField()
    expire_product = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.name}"
    

    class Meta:
        db_table = "Product"



    

