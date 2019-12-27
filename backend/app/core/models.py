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

EXPIRE_HOURS = getattr(settings, 'REST_FRAMEWORK_TOKEN_EXPIRE_HOURS', 24)


def resource_file_path(instance, filename):
    """Generate file path for new resource file"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

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
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

# Resources


class CorporativoNoDirigida(models.Model):
    """CorporativoNoDirigida resource model"""
    Branch = models.CharField(max_lenght=10)
    LV = models.CharField(max_lenght=10)
    NombreVehiculo = models.CharField(max_lenght=50)
    Cuenta = models.CharField(max_lenght=20)
    DescripcionCuenta = models.CharField(max_lenght=20)
    Grupo = models.IntegerField()
    Pal = models.IntegerField()
    Pal_cat_descr = models.CharField(max_lenght=50)
    Prod = models.CharField(max_lenght=50)
    Prod_cat_descr = models.CharField(max_lenght=50)
    Referencia = models.CharField(max_lenght=20, primary_key=True)
    Descripcion = models.CharField(max_lenght=50)
    ClasificacionRiesgo = models.CharField(max_lenght=2)
    Provision = models.DecimalField(max_digits=3, decimal_places=2)
    A = models.CharField(max_lenght=10)
    FechaInicio = models.DateField(default=date.fromisoformat('1900-01-01'))
    FechaFinal = models.DateField(default=date.fromisoformat('1900-01-01'))
    B = models.IntegerField()
    C = models.IntegerField()
    BCV = models.CharField(max_lenght=10)
    Tasa = models.DecimalField(max_digits=18, decimal_places=2)
    Debito = models.DecimalField(max_digits=18, decimal_places=2)
    Credito = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo = models.DecimalField(max_digits=18, decimal_places=2)
    Type = models.CharField(max_lenght=10)
    Type3dig = models.CharField(max_lenght=10)
    CuentaSIF = models.CharField(max_lenght=10)
    RendimientosCobrarReestructurados = models.DecimalField(
        max_digits=18, decimal_places=2)
    RendimientosCobrarEfectosReporto = models.DecimalField(
        max_digits=18, decimal_places=2)
    RendimientosCobrarLitigio = models.DecimalField(
        max_digits=18, decimal_places=2)
    InteresesEfectivamenteCobrados = models.DecimalField(
        max_digits=18, decimal_places=2)
    PorcentajeComisionFLAT = models.DecimalField(
        max_digits=18, decimal_places=2)
    MontoComisionFLAT = models.DecimalField(max_digits=18, decimal_places=2)
    PeriodicidadPagoEspecialCapital = models.IntegerField()
    FechaCambioEstatusCredito = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    FechaRegistroVencidaLitigioCastigada = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    FechaExigibilidadPagoUltimaCuotaPagada = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    CuentaContableProvisionEspecifica = models.CharField(max_lenght=10)
    CuentaContableProvisionRendimiento = models.CharField(max_lenght=10)
    CuentaContableInteresCuentaOrden = models.CharField(max_lenght=10)
    MontoInteresCuentaOrden = models.DecimalField(
        max_digits=18, decimal_places=2)
    TipoIndustria = models.IntegerField()
    TipoBeneficiarioSectorManufacturero = models.IntegerField()
    TipoBeneficiarioSectorTurismo = models.IntegerField()
    BeneficiarioEspecial = models.IntegerField()
    FechaEmisionCertificacionBeneficiarioEspecial = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    TipoVivienda = models.IntegerField()
    FechaFinPeriodoGraciaPagoInteres = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    CapitalTransferido = models.DecimalField(max_digits=18, decimal_places=2)
    FechaCambioEstatusCapitalTransferido = models.DateField(
        default=date.fromisoformat('1900-01-01'))
    SaldoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    ActividadCliente = models.CharField(max_lenght=10)
    RifLetra = models.CharField(max_lenght=2)
    RifNumerico = models.CharField(max_lenght=10)
    GrupoEconomico = models.CharField(max_length=100)
    TipoGarantiaPrincipal = models.CharField(max_lenght=10)
    IsOverdraft = models.BooleanField()
    MakerDate = models.DateField(default=date.now))
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CheckerDate = models.DateField(default=date.now))
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return self.Referencia

class SobregirosConsumer(models.Model):
    """CorporativoNoDirigida resource model"""
    BranchId = models.IntegerField()
    BranchDescription = models.CharField(max_lenght=20)
    CId = models.CharField(max_lenght=20)
    TipoPersona = models.CharField(max_lenght=20)
    Acct = models.CharField(max_lenght=20, primary_key=True)
    OpenDate = models.DateField(default=date.fromisoformat('1900-01-01'))
    Rate = models.DecimalField(max_digits=18, decimal_places=2)
    MinBalance = models.DecimalField(max_digits=18, decimal_places=2)
    Producto = models.CharField(max_lenght=20)
    Remunerada = models.CharField(max_lenght=20)
    TermDays = models.IntegerField()
    StatusId = models.IntegerField()
    StatusDescription = models.CharField(max_lenght=20)
    Balance = models.DecimalField(max_digits=18, decimal_places=2)
    Overdraft = models.DecimalField(max_digits=18, decimal_places=2)
    Nombre = models.CharField(max_lenght=20)
    MaturityDate = models.DateField(default=date.fromisoformat('1900-01-01'))
    TypeId = models.IntegerField()
    DescriptionType = models.CharField(max_lenght=20)
    Opened = models.IntegerField()
    RecordDate = models.DateField(default=date.fromisoformat('1900-01-01'))
    NA2 = models.CharField(max_lenght=20)
    NA1 = models.CharField(max_lenght=20)
    NTID = models.CharField(max_lenght=20)
    SEX = models.CharField(max_lenght=2)
    BDTE = models.DateField(default=date.fromisoformat('1900-01-01'))
    CRCD = models.IntegerField()
    CPREF = models.IntegerField()
    OPDT = models.CharField(max_lenght=20)
    ACTI = models.IntegerField()
    OCCP = models.IntegerField()
    Fecha_Cambio_Estatus_Crédito = models.DateField(default=date.fromisoformat('1900-01-01'))
    Fecha_Registro_Vencida_Litigio_Castigada = models.DateField(default=date.fromisoformat('1900-01-01'))
    Fecha_Exigibilidad_Pago_última_cuota_pagada = models.DateField(default=date.fromisoformat('1900-01-01'))
    Capital_Transferido = models.DecimalField(max_digits=18, decimal_places=2)
    Fecha_Cambio_Capital_Transferido = models.DateField(default=date.fromisoformat('1900-01-01'))
    Riesgo = models.CharField(max_lenght=20)
    Provision = models.DecimalField(max_digits=3, decimal_places=2)
    SaldoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=date.now))
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CheckerDate = models.DateField(default=date.now))
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return self.Acct


class RendimientosCorporativos(models.Model):
    """RendimientosCorporativos resource model"""
    Branch = models.IntegerField()
    LV = models.IntegerField()
    NombreVehiculo = models.CharField(max_lenght=20)
    Cuenta = models.CharField(max_lenght=20)
    DescripcionDeLaCuenta = models.CharField(max_lenght=20)
    Grupo = models.IntegerField()
    Pal = models.IntegerField()
    pal_cat_descr = models.CharField(max_lenght=20)
    Prod = models.CharField(max_lenght=20)
    prod_cat_descr = models.CharField(max_lenght=20)
    Referencia = models.CharField(max_lenght=20, primary_key=True)
    Descripcion = models.CharField(max_lenght=20)
    A = models.IntegerField()
    FechaInicio = models.DateField(default=date.fromisoformat('1900-01-01'))
    FechaFinal = models.DateField(default=date.fromisoformat('1900-01-01'))
    B = models.IntegerField()
    C = models.IntegerField()
    BCV = models.CharField(max_lenght=20)
    Tasa = models.DecimalField(max_digits=18, decimal_places=2)
    Debito = models.DecimalField(max_digits=18, decimal_places=2)
    Credito = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo = models.DecimalField(max_digits=18, decimal_places=2)
    Type = models.IntegerField()
    Type3dig = models.IntegerField()
    CuentaSIF = models.CharField(max_lenght=20)
    PorcentajeProvision = models.DecimalField(max_digits=3, decimal_places=2)
    MontoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=date.now))
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CheckerDate = models.DateField(default=date.now))
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return self.Referencia

class MigrateMorgage(models.Model):
    """MigrateMorgage resource model"""
    NewAcct = models.CharField(max_lenght=20, primary_key=True)
    OldAcct = models.CharField(max_lenght=20, unique=True)
    MakerDate = models.DateField(default=date.now))
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CheckerDate = models.DateField(default=date.now))
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    def __str__(self):
        return self.NewAcct

class GavetasCorporativas(models.Model):
    """GavetasCorporativas"""
    RIF = models.CharField(max_lenght=20)
    NombreRazonSocial = models.CharField(max_lenght=20)
    NumeroCredito = models.CharField(max_lenght=20)
    InteresesEfectivamenteCobrados = models.DecimalField(max_digits=18, decimal_places=2)
    PorcentajeComisiónFLAT = models.DecimalField(max_digits=3, decimal_places=2)
    MontoComisiónFLAT = models.DecimalField(max_digits=18, decimal_places=2)
    PeriodicidadPagoEspecialCapital = models.DecimalField(max_digits=18, decimal_places=2)
    FechaExigibilidadPagolaúltimaCuotaPagada = models.DateField(default=date.fromisoformat('1900-01-01'))
    FechaRegistroVencidaLitigioCastigada = models.DateField(default=date.fromisoformat('1900-01-01'))
    TipoIndustria = models.IntegerField()
    TipoBeneficiarioSectorManufacturero = models.IntegerField()
    TipoBeneficiarioSectorTurismo = models.IntegerField()
    BeneficiarioEspecial = models.IntegerField()
    FechaEmisiónCertificaciónBeneficiarioEspecial = models.DateField(default=date.fromisoformat('1900-01-01'))
    TipoVivienda = models.IntegerField()
    FechaFinPeriodoGraciaPagoInterés = models.DateField(default=date.fromisoformat('1900-01-01'))
    CapitalTransferido = models.DecimalField(max_digits=18, decimal_places=2)
    FechaCambioEstatusCapitalTransferido = models.DateField(default=date.fromisoformat('1900-01-01'))
    FechaCambioEstatusCrédito = models.DateField(default=date.fromisoformat('1900-01-01'))

    def __str__(self):
        return self.NumeroCredito


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
