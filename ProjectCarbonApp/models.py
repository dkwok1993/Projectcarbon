from django.db import models

class Lifecycle(models.Model):
    name = models.CharField(max_length=430, null=True)
    carbon_emission_factor = models.DecimalField(max_digits=6, decimal_places=3)


class Vehicles(models.Model):
    name = models.CharField(max_length=430, null=True)
    carbon_emission_factor = models.DecimalField(max_digits=6, decimal_places=3)
    
class Supplier_specific(models.Model):
    name = models.CharField(max_length=430, null=True)
    supplier_emission_factor = models.DecimalField(max_digits=6, decimal_places=3)
    
    
class Weights(models.Model):
    purchase_unit = models.CharField(max_length=430, null=True)
    purchase_unit_conversion_rate = models.DecimalField(max_digits=6, decimal_places=3)


class Item(models.Model):
    item_id = models.IntegerField(null=False)
    name = models.CharField(max_length=430, null=True)
    purchase_unit = models.CharField(max_length=430, null=True)
    units = models.DecimalField(max_digits=12, decimal_places=3)