from django.db import models

# Create your models here.

class item(models.Model):
    item_id=models.IntegerField()
    item_name=models.CharField(max_length=20)
    item_description=models.CharField(max_length=80)
    item_price=models.FloatField()
    available_stock=models.CharField()