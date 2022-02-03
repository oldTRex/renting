from pyexpat import model
from django.db import models

# Create your models here.


class Vehicle(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name  


class Rental(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=30)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle + "-"+self.city + "-" + self.date

    class Meta:
        ordering = ['date']
