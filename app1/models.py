from django.db import models

# Create your models here.
class ProductModel(models.Model):
     no=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100)
     price=models.IntegerField()
     quantity=models.IntegerField()