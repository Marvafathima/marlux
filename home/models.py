
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# import uuid
# from django.utils import timezone 


# class User(models.Model):
#     email = models.EmailField(max_length=254, unique=True)
#     user_name = models.CharField(max_length=254, null=True, blank=True)
#     phone_number=models.CharField(max_length=15)
#     password=models.CharField(max_length=15)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)


# class Profile(models.Model):
#     user=models.OneToOneField(User,   on_delete=models.CASCADE,related_name="profile")
#     phone_number=models.CharField(max_length=15)
#     otp=models.CharField(max_length=100,null=True,blank=True)
#     uid=models.CharField(default=f'{uuid.uuid4}',max_length=200)