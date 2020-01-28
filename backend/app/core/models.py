import datetime
from datetime import date

import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from rest_framework.authtoken.models import Token

from django.utils.translation import gettext_lazy as _


EXPIRE_HOURS = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_HOURS', 24)


# def resource_file_path(instance, filename):
#     """Generate file path for new resource file"""
#     ext = filename.split('.')[-1]
#     filename = f'{uuid.uuid4()}.{ext}'

#     return os.path.join(settings.MEDIA_ROOT, filename)

def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    user_id = instance.user.id
    resource_name = instance.resource_name
    filename = f'{user_id}_{resource_name}_{uuid.uuid4()}.{ext}'
    return os.path.join(settings.MEDIA_ROOT, filename)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(
            user=instance)
        yesterday = (timezone.now() - datetime.timedelta(hours=EXPIRE_HOURS))
        instance.expiresIn = (
            instance.auth_token.created - yesterday).total_seconds()
        instance.save()


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    expiresIn = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # token = models.ForeignKey('Token',
    #                           related_name='token',
    #                           on_delete=models.CASCADE,
    #                           default=None)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class File(models.Model):
    """Custom file model that supports uploading a file"""

    class TypeCD(models.TextChoices):
        AH = 'AH', _('Account History')
        AT04CRE = 'AT04CRE', _('AT04 CRE')
        AT07 = 'AT07', _('AT07')
        BBAT = 'BBAT', _('Bal By Acct Transformada')
        CND = 'CND', _('Cartera No Dirigida')
        CD = 'CD', _('Cartera Dirigida')
        FDN = 'FDN', _('Fecha de Nacimiento')
        GICG = 'GICG', _('Gavetas ICG')
        LNP860 = 'LNP860', _('LNP860')
        MM = 'MM', _('Migrate Mortgage')
        MISP = 'MISP', _('MIS Provisiones')
        PPRRHH = 'PPRRHH', _('Prestamos sobre Prestaciones RRHH')
        RICG = 'RICG', _('Rendimientos ICG')
        SIIF = 'SIIF', _('SIIF')
        SC = 'SC', _('Sobregiros Consumer')
        VNP003T = 'VNP003T', _('VNP003T')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    resource_name = models.CharField(
        max_length=50, choices=TypeCD.choices, default='')
    file = models.FileField(upload_to=path_and_rename, blank=False, null=False)

    def __str__(self):
        return self.file.name


# class Tag(models.Model):
#     """Tag to be used for a recipe"""
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.name


# class Ingredient(models.Model):
#     """Ingredient to be used in a recipe"""
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )

#     def __str__(self):
#         return self.name


# class Recipe(models.Model):
#     """Recipe object"""
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE
#     )
#     title = models.CharField(max_length=255)
#     time_minutes = models.IntegerField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     link = models.CharField(max_length=255, blank=True)
#     ingredients = models.ManyToManyField('Ingredient')
#     tags = models.ManyToManyField('Tag')
#     image = models.ImageField(null=True, upload_to=recipe_image_file_path)

#     def __str__(self):
#         return self.title
