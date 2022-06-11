from django.contrib import admin
from .models import Employee, EmployeeManager
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {
            "fields": (
                'email', 'user_name', 'first_name',
            ),
        }),
        ('Permissions', {'fields': (
                'is_staff', 'is_active')}),
         ('Personal', {'fields': (
                'about',)}),
    )
    
    formfield_overrides = {
        Employee.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(Employee, UserAdminConfig)





