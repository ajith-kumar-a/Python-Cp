from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
# class FoodItem(models:Model):
#     name = models.CharField(max_length=60)



class Address(models.Model):
    city = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    street_no = models.IntegerField()

class Chief(models.Model):
    first_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE,null=True)

class Dish(models.Model):
    name=models.CharField(max_length=50)
    ratings = models.IntegerField(
        validators=[ MaxValueValidator(10),MinValueValidator(5)])
    chief = models.ForeignKey(Chief,on_delete=models.CASCADE,null=True)
