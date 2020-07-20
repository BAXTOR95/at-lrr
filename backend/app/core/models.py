import datetime
from datetime import date

import uuid

import unidecode

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
    """Creates a proper file name with the given file name

    Arguments:
        instance {[object]} -- the instance
        filename {[str]} -- the file name

    Returns:
        [str] -- the final file name
    """
    mod_filename = unidecode.unidecode(filename)
    ext = mod_filename.split('.')[-1]
    f_name = mod_filename.split('.')[0]
    user_id = instance.user.id
    resource_name = instance.resource_name
    final_filename = f'{user_id}_{resource_name}_{f_name}_{uuid.uuid4()}.{ext}'
    # path = os.path.join(settings.MEDIA_ROOT, filename)
    return final_filename


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

    def create_user(self, soeid, email=None, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not soeid:
            raise ValueError(_('Users must have a SOEID'))
        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        soeid = str(soeid).upper()
        user = self.model(
            soeid=soeid,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, soeid, email=None, password=None, **extra_fields):
        """Creates and saves a new super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(soeid, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    soeid = models.CharField(max_length=7, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    expiresIn = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # token = models.ForeignKey('Token',
    #                           related_name='token',
    #                           on_delete=models.CASCADE,
    #                           default=None)

    USERNAME_FIELD = 'soeid'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.soeid


class Workflow(models.Model):
    """Custom workflow model that supports starting the construction of a report"""

    class Reports(models.TextChoices):
        AT01 = 'AT01', _('AT01 - Accionistas del Ente Supervisado')
        AT02 = 'AT02', _('AT02 - Bienes Recibidos en Pago')
        AT03 = 'AT03', _('AT03 - Contable')
        AT04 = 'AT04', _('AT04 - Cartera de Creditos')
        AT05 = 'AT05', _('AT05 - Captaciones')
        AT06 = 'AT06', _('AT06 - Transacciones Financieras')
        AT07 = 'AT07', _('AT07 - Garantias Recibidas')
        AT08 = 'AT08', _('AT08 - Agencias y Oficinas')
        AT09 = 'AT09', _(
            'AT09 - Compra y Venta de Inversiones en Titulos Valores')
        AT10 = 'AT10', _('AT10 - Inversiones')
        AT11 = 'AT11', _(
            'AT11 - Conformacion de las Disponibilidades, Inversiones y Custodios a Terceros')
        AT12 = 'AT12', _('AT12 - Consumos de Tarjetas')
        AT13 = 'AT13', _('AT13 - Reclamos')
        AT14 = 'AT14', _('AT14 - Instrumentos')
        AT15 = 'AT15', _('AT15 - Notificacion de Transpaso de Acciones')
        AT16 = 'AT16', _('AT16 - Empresas Accionistas del Ente Supervisado')
        AT17 = 'AT17', _('AT17 - Agricola Semanal')
        AT18 = 'AT18', _('AT18 - Variaciones de las tasas de Credito')
        AT19 = 'AT19', _('AT19 - Transacciones de Pago')
        AT20 = 'AT20', _('AT20 - Notas al Pie del Balance')
        AT21 = 'AT21', _('AT21 - Garantes')
        AT23 = 'AT23', _('AT23 - Personal')
        AT24 = 'AT24', _('AT24 - Balance General de Publicacion')
        AT25 = 'AT25', _('AT25 - Estado de Resultados')
        AT26 = 'AT26', _('AT26 - Fraude Bancario')
        AT27 = 'AT27', _(
            'AT27 - Composicion Activa-Pasiva de Organismos Oficiales, P. Juridicas y Naturales')
        AT29 = 'AT29', _('AT29 - Gravamen')
        AT30 = 'AT30', _(
            'AT30 - Adquisicion y Venta de Bienes Recibidos en Pago')
        AT31 = 'AT31', _(
            'AT31 - Movimientos de credito y debito de las operaciones Activas y Pasivas')
        AT32 = 'AT32', _(
            'AT32 - Fondo de Ahorro Obligatorio para la Viviendaa (FAOV)')
        AT33 = 'AT33', _('AT33 - Convenio Cambiario')
        AT34 = 'AT34', _('AT34 - Grupo Junta Directiva del Ente')
        AT35 = 'AT35', _(
            'AT35 - 100 Mayores Depositantes de personas Naturales y Juridicas')
        AT36 = 'AT36', _('AT36 - Lineas de Credito de Utilizacion Automatica')
        AT37 = 'AT37', _('AT37 - Transferencias Electronicas')
        AT38 = 'AT38', _(
            'AT38 - Impuesto a las Grandes Transacciones Financieras')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None
    )
    report_name = models.CharField(
        max_length=50, choices=Reports.choices, default='')
    book_data = models.DateField(default=date.today)


class File(models.Model):
    """Custom file model that supports uploading a file"""

    class TypeCD(models.TextChoices):
        AH = 'AH', _('Account History')
        AT04 = 'AT04', _('AT04 Transmitido Pasado')
        AT04CRE = 'AT04CRE', _('AT04 CRE')
        AT07 = 'AT07', _('AT07 Actual')
        BBAT = 'BBAT', _('Bal By Acct Transformada')
        CND = 'CND', _('Cartera No Dirigida')
        CC = 'CC', _('Clientes Consumer')
        CD = 'CD', _('Cartera Dirigida')
        CFGESIIFCITI = 'CFGESIIFCITI', _(
            'Tabla CFGESIIFCITI (Equivalencias Actividad Cliente)')
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
    report_name = models.CharField(
        max_length=50, choices=Workflow.Reports.choices, default='')
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
