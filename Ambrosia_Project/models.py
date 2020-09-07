from django.db import models

# Create your models here.
# Create your models here.


class Broker(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=10, null=True)


class Buyer(models.Model):
    vat_regno = models.CharField(max_length=30)
    name = models.CharField(max_length=50)


class Funds(models.Model):
    date = models.DateField(input_formats=['%d/%m/%Y'])
    emp_