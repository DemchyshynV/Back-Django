from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=13,
                             unique=True,
                             validators=[RegexValidator(r'^([+])(\d{1,13})$', 'invalid phone number')])
