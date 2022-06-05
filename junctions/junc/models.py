from django.db import models

# Create your models here.

class Junction(models.Model):
    corr = models.CharField(max_length=2)
    mark = models.CharField(max_length=4)
    status = models.CharField(max_length=20)
    needs = models.CharField(max_length=20)
    civil_works_need = models.BooleanField(default=False)
    add_info = models.TextField(max_length=110)

    def __str__(self):
        return '{} - {}'.format(self.corr, self.mark)
    
