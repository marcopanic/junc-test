from django.contrib import admin
from stomps.models import Pedal
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Pedal)

class PedalData(ImportExportModelAdmin):
    pass