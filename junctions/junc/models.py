from django.db import models
from django.urls import reverse


# Create your models here.

class Junction(models.Model):
    corr = models.PositiveIntegerField()
    mark = models.CharField(max_length=6)
    status = models.CharField(max_length=20)
    needs = models.CharField(max_length=20, default='', blank=True)
    civil_works_need = models.BooleanField(default=False)
    cables_cut = models.BooleanField(default=False)
    add_info = models.TextField(max_length=110, default='', blank=True)

    class Meta:
        db_table='Junction'

    def __str__(self):
        return '{} - {}'.format(self.corr, self.mark)

    # def get_absolute_url(self):
    #     return reverse("junc:detail", kwargs={"pk": self.pk})
    
