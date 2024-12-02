from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin

from django.db import models


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, phone, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, phone, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True, null=True, blank=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email