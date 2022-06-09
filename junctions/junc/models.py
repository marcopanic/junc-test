from django.db import models
from django.urls import reverse


# Create your models here.

# class Status(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("junc:detail", kwargs={"pk": self.pk})




class Junction(models.Model):
    PUN_REZIM = 'Pun Rezim'
    PART_TIME = 'Part Time'
    NEMA_STRUJE = 'Nema Struje'
    UGASENA = 'Ugasena'
    
    STATUS_CHOICES=[
                (PUN_REZIM, 'Pun Rezim'),
                (PART_TIME, 'Part Time'),
                (NEMA_STRUJE, 'Nema Struje'),
                (UGASENA, 'Ugasena'),
       ]
    corr = models.PositiveIntegerField()
    mark = models.CharField(max_length=6)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PUN_REZIM)
    needs = models.CharField(max_length=20, default='', blank=True)
    civil_works_need = models.BooleanField(default=False)
    cables_cut = models.BooleanField(default=False)
    add_info = models.TextField(max_length=110, default='', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    name_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='Junction'

    def __str__(self):
        return '{} - {}'.format(self.corr, self.mark)

    # def get_absolute_url(self):
    #     return reverse("junc:detail", kwargs={"pk": self.pk})
    
