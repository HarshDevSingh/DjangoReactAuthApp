from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class Gender(models.Model):
    gender = models.CharField(max_length=100, blank=False, null=False, default='other')

    def __str__(self):
        return self.gender


class CustomUser(AbstractUser):
    username = None
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    def user_avatar(self, instance):
        return '/'.join(['users', str(instance)])
    user = models.OneToOneField(CustomUser, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar,default='default/default.png',blank=True,null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE,null=True,blank=True)
    dob = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.email}-{self.first_name}'
