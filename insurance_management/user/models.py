from django.db import models

from django.core.validators import RegexValidator
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from oauth2_provider.models import AbstractApplication, Application


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_role, password=None):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_role=user_role)
        user.set_password(password)
        user.save(using=self._db)
        application = Application.objects.create(
            user=user,
            authorization_grant_type='password',
            client_type="public",
        )
        application.save()
        return user

    def create_superuser(self, email, user_role, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email=email, password=password, user_role=user_role)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ("super_user", "super_user"),
        ("organization", "organization"),
        ("employee", "employee"),
    ]

    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    user_role = models.CharField(choices=ROLE_CHOICES, max_length=15)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_role']


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
