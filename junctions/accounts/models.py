from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.



class EmployeeManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_("You have to provide an email address"))
          
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()     
        return user


    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get("is_staff") is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True'))
        if other_fields.get("is_superuser") is not True:
            raise ValueError(_('Superuser must be assigned to is_superuser=True'))
        return self.create_user(email, user_name, first_name, password, **other_fields)



class Employee(AbstractBaseUser, PermissionsMixin):
    SUPADMIN = 1
    TECH = 2
    GUEST =3
      
    ROLE_CHOICES = [
          (SUPADMIN, 'Supadmin'),
          (TECH, 'Tech'),
          (GUEST, 'Guest'),
      ]

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=20, default='', blank=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=GUEST)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    object = EmployeeManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']


    def __str__(self):
        return self.user_name

    