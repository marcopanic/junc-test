from django.db import models


# Create your models here.

class Pedal(models.Model):
    pedal_name=models.CharField(max_length=22)
    pedal_cat=models.CharField(max_length=15)
    pedal_year=models.PositiveIntegerField(blank=True, default='')

    class Meta:
        db_table='Pedal'

    def __str__(self):
        return self.pedal_name
    