from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def create_superuser(self, username, first_name, last_name, cpf, password, **other_fields):

        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, first_name, last_name, cpf, password, **other_fields)

    def create_user(username, first_name, last_name, cpf, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        user = self.model(username=username, first_name=first_name,
                          last_name=last_name, cpf=cpf, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf']

    objects = UserManager()

    def __str__(self):
        return self.username
