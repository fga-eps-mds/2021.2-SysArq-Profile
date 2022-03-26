from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, username, user_type, first_name, last_name,
                         cpf, password, **other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('user_type', User.User_Type.AD)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, user_type, first_name, last_name,
                                cpf, password, **other_fields)

    def create_user(self, username, user_type, first_name, last_name, cpf, password, **other_fields):

        user = self.model(username=username, user_type=user_type, first_name=first_name,
                          last_name=last_name, cpf=cpf, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    class User_Type(models.TextChoices):
        AD = "AD", "Administrador"
        AL = "AL", "Alimentador"
        VI = "VI", "Visualizador"
    

    username = models.CharField(max_length=150, unique=True)
    user_type = models.CharField(
        max_length=2,
        choices=User_Type.choices, 
        default=User_Type.VI, 
        )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    cpf = models.CharField(max_length=15, blank=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['cpf']

    objects = UserManager()
