from django.db import models

class Products(models.Model):
    class Meta:
        db_table = 'products'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=20, decimal_places=2, default = 0.0)
    category = models.CharField(max_length=150)
    description = models.TextField()
