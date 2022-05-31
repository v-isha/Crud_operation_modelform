from django.db import models


# Create your models here.
class customer(models.Model):
    customer_id =models.IntegerField(primary_key="true")
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=80)
    password=models.CharField(max_length=90)