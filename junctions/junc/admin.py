from django.contrib import admin
from .models import Junction
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Status)

@admin.register(Junction)

class JuncData(ImportExportModelAdmin):
    pass


