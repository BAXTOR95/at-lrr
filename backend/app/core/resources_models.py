import datetime

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Resources

# Manual

class CorporativoNoDirigida(models.Model):
    """CorporativoNoDirigida resource model"""
    Branch = models.CharField(max_length=10)
    LV = models.CharField(max_length=10)
    NombreVehiculo = models.CharField(max_length=50)
    Cuenta = models.CharField(max_length=20)
    DescripcionCuenta = models.CharField(max_length=20)
    Grupo = models.IntegerField()
    Pal = models.IntegerField()
    Pal_cat_descr = models.CharField(max_length=50)
    Prod = models.CharField(max_length=50)
    Prod_cat_descr = models.CharField(max_length=50)
    Referencia = models.CharField(max_length=20, primary_key=True)
    Descripcion = models.CharField(max_length=50)
    ClasificacionRiesgo = models.CharField(max_length=2)
    Provision = models.DecimalField(max_digits=3, decimal_places=2)
    A = models.CharField(max_length=10)
    FechaInicio = models.DateField(default=datetime.datetime(1900, 1, 1))
    FechaFinal = models.DateField(default=datetime.datetime(1900, 1, 1))
    B = models.IntegerField()
    C = models.IntegerField()
    BCV = models.CharField(max_length=10)
    Tasa = models.DecimalField(max_digits=18, decimal_places=2)
    Debito = models.DecimalField(max_digits=18, decimal_places=2)
    Credito = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo = models.DecimalField(max_digits=18, decimal_places=2)
    Type = models.CharField(max_length=10)
    Type3dig = models.CharField(max_length=10)
    CuentaSIF = models.CharField(max_length=10)
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
        default=datetime.datetime(1900, 1, 1))
    FechaRegistroVencidaLitigioCastigada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaExigibilidadPagoUltimaCuotaPagada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CuentaContableProvisionEspecifica = models.CharField(max_length=10)
    CuentaContableProvisionRendimiento = models.CharField(max_length=10)
    CuentaContableInteresCuentaOrden = models.CharField(max_length=10)
    MontoInteresCuentaOrden = models.DecimalField(
        max_digits=18, decimal_places=2)
    TipoIndustria = models.IntegerField()
    TipoBeneficiarioSectorManufacturero = models.IntegerField()
    TipoBeneficiarioSectorTurismo = models.IntegerField()
    BeneficiarioEspecial = models.IntegerField()
    FechaEmisionCertificacionBeneficiarioEspecial = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TipoVivienda = models.IntegerField()
    FechaFinPeriodoGraciaPagoInteres = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CapitalTransferido = models.DecimalField(max_digits=18, decimal_places=2)
    FechaCambioEstatusCapitalTransferido = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    SaldoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    ActividadCliente = models.CharField(max_length=10)
    RifLetra = models.CharField(max_length=2)
    RifNumerico = models.CharField(max_length=10)
    GrupoEconomico = models.CharField(max_length=100)
    TipoGarantiaPrincipal = models.CharField(max_length=10)
    IsOverdraft = models.BooleanField()
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='corporativo_no_dirigida_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='corporativo_no_dirigida_checker_user_set'
    )

    def __str__(self):
        return self.Referencia


class SobregirosConsumer(models.Model):
    """CorporativoNoDirigida resource model"""
    BranchId = models.IntegerField()
    BranchDescription = models.CharField(max_length=20)
    CId = models.CharField(max_length=20)
    TipoPersona = models.CharField(max_length=20)
    Acct = models.CharField(max_length=20, primary_key=True)
    OpenDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    Rate = models.DecimalField(max_digits=18, decimal_places=2)
    MinBalance = models.DecimalField(max_digits=18, decimal_places=2)
    Producto = models.CharField(max_length=20)
    Remunerada = models.CharField(max_length=20)
    TermDays = models.IntegerField()
    StatusId = models.IntegerField()
    StatusDescription = models.CharField(max_length=20)
    Balance = models.DecimalField(max_digits=18, decimal_places=2)
    Overdraft = models.DecimalField(max_digits=18, decimal_places=2)
    Nombre = models.CharField(max_length=20)
    MaturityDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    TypeId = models.IntegerField()
    DescriptionType = models.CharField(max_length=20)
    Opened = models.IntegerField()
    RecordDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    NA2 = models.CharField(max_length=20)
    NA1 = models.CharField(max_length=20)
    NTID = models.CharField(max_length=20)
    SEX = models.CharField(max_length=2)
    BDTE = models.DateField(default=datetime.datetime(1900, 1, 1))
    CRCD = models.IntegerField()
    CPREF = models.IntegerField()
    OPDT = models.CharField(max_length=20)
    ACTI = models.IntegerField()
    OCCP = models.IntegerField()
    Fecha_Cambio_Estatus_Credito = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Fecha_Registro_Vencida_Litigio_Castigada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Fecha_Exigibilidad_Pago_ultima_cuota_pagada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Capital_Transferido = models.DecimalField(max_digits=18, decimal_places=2)
    Fecha_Cambio_Capital_Transferido = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Riesgo = models.CharField(max_length=20)
    Provision = models.DecimalField(max_digits=3, decimal_places=2)
    SaldoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sobregiros_consumer_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='sobregiros_consumer_checker_user_set'
    )

    def __str__(self):
        return self.Acct


class RendimientosCorporativos(models.Model):
    """RendimientosCorporativos resource model"""
    Branch = models.IntegerField()
    LV = models.IntegerField()
    NombreVehiculo = models.CharField(max_length=20)
    Cuenta = models.CharField(max_length=20)
    DescripcionDeLaCuenta = models.CharField(max_length=20)
    Grupo = models.IntegerField()
    Pal = models.IntegerField()
    pal_cat_descr = models.CharField(max_length=20)
    Prod = models.CharField(max_length=20)
    prod_cat_descr = models.CharField(max_length=20)
    Referencia = models.CharField(max_length=20, primary_key=True)
    Descripcion = models.CharField(max_length=20)
    A = models.IntegerField()
    FechaInicio = models.DateField(default=datetime.datetime(1900, 1, 1))
    FechaFinal = models.DateField(default=datetime.datetime(1900, 1, 1))
    B = models.IntegerField()
    C = models.IntegerField()
    BCV = models.CharField(max_length=20)
    Tasa = models.DecimalField(max_digits=18, decimal_places=2)
    Debito = models.DecimalField(max_digits=18, decimal_places=2)
    Credito = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo = models.DecimalField(max_digits=18, decimal_places=2)
    Type = models.IntegerField()
    Type3dig = models.IntegerField()
    CuentaSIF = models.CharField(max_length=20)
    PorcentajeProvision = models.DecimalField(max_digits=3, decimal_places=2)
    MontoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rendimientos_icg_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='rendimientos_icg_checker_user_set'
    )

    def __str__(self):
        return self.Referencia


class MigrateMorgage(models.Model):
    """MigrateMorgage resource model"""
    NewAcct = models.CharField(max_length=20, primary_key=True)
    OldAcct = models.CharField(max_length=20, unique=True)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='migrate_morgage_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='migrate_morgage_checker_user_set'
    )

    def __str__(self):
        return self.NewAcct


class GavetasCorporativas(models.Model):
    """GavetasCorporativas resource model"""
    RIF = models.CharField(max_length=20)
    NombreRazonSocial = models.CharField(max_length=20)
    NumeroCredito = models.CharField(max_length=20, primary_key=True)
    InteresesEfectivamenteCobrados = models.DecimalField(
        max_digits=18, decimal_places=2)
    PorcentajeComisionFLAT = models.DecimalField(
        max_digits=3, decimal_places=2)
    MontoComisionFLAT = models.DecimalField(max_digits=18, decimal_places=2)
    PeriodicidadPagoEspecialCapital = models.DecimalField(
        max_digits=18, decimal_places=2)
    FechaExigibilidadPagolaultimaCuotaPagada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaRegistroVencidaLitigioCastigada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TipoIndustria = models.IntegerField()
    TipoBeneficiarioSectorManufacturero = models.IntegerField()
    TipoBeneficiarioSectorTurismo = models.IntegerField()
    BeneficiarioEspecial = models.IntegerField()
    FechaEmisionCertificacionBeneficiarioEspecial = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TipoVivienda = models.IntegerField()
    FechaFinPeriodoGraciaPagoInteres = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CapitalTransferido = models.DecimalField(max_digits=18, decimal_places=2)
    FechaCambioEstatusCapitalTransferido = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaCambioEstatusCredito = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='gavetas_icg_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='gavetas_icg_checker_user_set'
    )

    def __str__(self):
        return self.NumeroCredito


class ModalidadHipotecaria(models.Model):
    """Modalidad Hipotecaria resource model"""
    Numerocredito = models.CharField(max_length=20, primary_key=True)
    IngresoFamiliar = models.DecimalField(max_digits=18, decimal_places=2)
    ModalidadHipotecaria = models.CharField(max_length=20)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='modalidad_hipotecaria_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='modalidad_hipotecaria_checker_user_set'
    )

    def __str__(self):
        return self.Numerocredito


class MISProvisiones(models.Model):
    """MIS Provisiones resource model"""
    Cid = models.CharField(max_length=20)
    Account = models.CharField(max_length=20, primary_key=True)
    AccountNew = models.CharField(max_length=20)
    ProdType = models.IntegerField()
    Provision = models.DecimalField(max_digits=18, decimal_places=2)
    SumSaldo = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo_Provision = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendXcobrar = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendXcobrarVenc = models.DecimalField(max_digits=18, decimal_places=2)
    ProvisionREND = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo_Provision_REND = models.DecimalField(max_digits=18, decimal_places=2)
    Overdraft = models.DecimalField(max_digits=18, decimal_places=2)
    MaxOfCantCuotasVencidas = models.IntegerField()
    CtaLocal = models.CharField(max_length=20)
    CtaProvCap = models.CharField(max_length=20)
    CtaProvRend = models.CharField(max_length=20)
    Riesgo = models.CharField(max_length=2)
    RiskSicri = models.CharField(max_length=20)
    Producto = models.IntegerField()
    DescriptionType = models.CharField(max_length=20)
    RecordDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    HDelinquency = models.CharField(max_length=50)
    BlockCode1Date = models.DateField(default=datetime.datetime(1900, 1, 1))
    BlockCodeId1 = models.CharField(max_length=2)
    BlockReason1 = models.CharField(max_length=2)
    BlockCode2Date = models.DateField(default=datetime.datetime(1900, 1, 1))
    BlockCodeId2 = models.CharField(max_length=2)
    BlockReason2 = models.CharField(max_length=2)
    Old_Acct = models.CharField(max_length=20)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mis_provisiones_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='mis_provisiones_checker_user_set'
    )

    def __str__(self):
        return self.Account


class PrestamosPrestacionesRRHH(models.Model):
    """Prestamos sobre Prestaciones Sociales RRHH resource model"""
    GEID = models.CharField(max_length=20, primary_key=True)
    NombreCliente = models.CharField(max_length=20)
    TipoCliente = models.CharField(max_length=2)
    IdentificacionCliente = models.CharField(max_length=20)
    MontoOriginal = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoActual = models.DecimalField(max_digits=18, decimal_places=2)
    FechaOtorgamiento = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='prestamos_prestaciones_hr_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='prestamos_prestaciones_hr_checker_user_set'
    )

    def __str__(self):
        return self.GEID


# Automatic

class AT04CRE(models.Model):
    """AT04CRE resource model"""
    BRANCH = models.IntegerField()
    REFERNO = models.CharField(max_length=20, primary_key=True)
    LIQUFECHA = models.DateField(default=datetime.datetime(1900, 1, 1))
    SOLIFECHA = models.DateField(default=datetime.datetime(1900, 1, 1))
    APROFECHA = models.DateField(default=datetime.datetime(1900, 1, 1))
    VCTOFECHA = models.DateField(default=datetime.datetime(1900, 1, 1))
    VCTOULTINTER = models.CharField(max_length=20)
    VCTOULTPRINC = models.CharField(max_length=20)
    ORIGFECHA = models.DateField(default=datetime.datetime(1900, 1, 1))
    PGTOULTCAPITAL = models.CharField(max_length=20)
    PGTOULTINTERES = models.CharField(max_length=20)
    BASECLI = models.CharField(max_length=20)
    RIFCLI = models.CharField(max_length=20)
    NOMECLI = models.CharField(max_length=20)
    SICVENCLI = models.CharField(max_length=20)
    SICUSACLI = models.CharField(max_length=20)
    NACICLI = models.CharField(max_length=20)
    DOMICLI = models.CharField(max_length=20)
    FECHACLI = models.DateField(default=datetime.datetime(1900, 1, 1))
    LIABICLI = models.CharField(max_length=20)
    LIABNOMCLI = models.CharField(max_length=20)
    RIESGOCLI = models.CharField(max_length=20)
    ADDRESS1 = models.CharField(max_length=20)
    ADDRESS2 = models.CharField(max_length=20)
    ADDRESS3 = models.CharField(max_length=20)
    ADDRESS4 = models.CharField(max_length=20)
    ADDRESS5 = models.CharField(max_length=20)
    ADDRESS6 = models.CharField(max_length=20)
    ADDRESSEXTRA = models.CharField(max_length=20)
    CTRORG = models.CharField(max_length=20)
    QTDREN = models.CharField(max_length=20)
    MONEDA = models.CharField(max_length=20)
    PRODCAT = models.CharField(max_length=20)
    LV = models.CharField(max_length=20)
    STATUS = models.CharField(max_length=20)
    PLAZO = models.CharField(max_length=20)
    GENLEDGER = models.CharField(max_length=20)
    CREDITLINE = models.DecimalField(max_digits=18, decimal_places=2)
    INTORIGTASA = models.DecimalField(max_digits=18, decimal_places=2)
    CAMBIOTASA = models.DecimalField(max_digits=18, decimal_places=2)
    COMISTASA = models.DecimalField(max_digits=18, decimal_places=2)
    ORIGIMONTO = models.DecimalField(max_digits=18, decimal_places=2)
    PAGOMESMONTO = models.DecimalField(max_digits=18, decimal_places=2)
    PAGOTOTAL = models.DecimalField(max_digits=18, decimal_places=2)
    SALDOMONTO = models.DecimalField(max_digits=18, decimal_places=2)
    TOTALCUOTAS = models.DecimalField(max_digits=18, decimal_places=2)
    PAGASCUOTAS = models.DecimalField(max_digits=18, decimal_places=2)
    VENCIDACUOTAS = models.DecimalField(max_digits=18, decimal_places=2)
    N030DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N060DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N090DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N120DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N180DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N360DMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    MA1AMONTOVENCIDO = models.DecimalField(max_digits=18, decimal_places=2)
    N030DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    N060DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    N090DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    N120DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    N180DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    N360DMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    MA1AMONTOAVENCER = models.DecimalField(max_digits=18, decimal_places=2)
    FILLER = models.CharField(max_length=20)
    EsNoDirigido = models.IntegerField()
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='at04cre_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='at04cre_checker_user_set'
    )

    def __str__(self):
        return self.REFERNO


class LNP860(models.Model):
    """LNP860 resource model"""
    P8NOTE = models.CharField(max_length=20, primary_key=True)
    P8TINC = models.DecimalField(max_digits=18, decimal_places=2)
    P8FVUC = models.DateField(default=datetime.datetime(1900, 1, 1))
    P8FCCC = models.DateField(default=datetime.datetime(1900, 1, 1))
    P8FVUI = models.DateField(default=datetime.datetime(1900, 1, 1))
    P8FCCI = models.DateField(default=datetime.datetime(1900, 1, 1))
    P8NRCV = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV30 = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV60 = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV90 = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV12 = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV18 = models.DecimalField(max_digits=18, decimal_places=2)
    P8MV1A = models.DecimalField(max_digits=18, decimal_places=2)
    P8MVM1 = models.DecimalField(max_digits=18, decimal_places=2)
    P8RPCV = models.DecimalField(max_digits=18, decimal_places=2)
    P8LINT = models.DecimalField(max_digits=18, decimal_places=2)
    P8FCTC = models.DateField(default=datetime.datetime(1900, 1, 1))
    P8MOCA = models.DecimalField(max_digits=18, decimal_places=2)
    P8MOIN = models.DecimalField(max_digits=18, decimal_places=2)
    P8TRXN = models.IntegerField()
    P8PRAN = models.IntegerField()
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lnp860_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='lnp860_checker_user_set'
    )

    def __str__(self):
        return self.P8NOTE


class VNP003T(models.Model):
    """VNP003T resource model"""
    DBKA = models.CharField(max_length=13)
    DAPPNA = models.CharField(max_length=12)
    DACCTA = models.CharField(max_length=22, primary_key=True)
    DSTATA = models.CharField(max_length=11)
    DTYPEA = models.CharField(max_length=13)
    DBRCHA = models.CharField(max_length=13)
    DOPDTA = models.CharField(max_length=17)
    DOFFA = models.CharField(max_length=13)
    DCBALA = models.DecimalField(max_digits=18, decimal_places=2)
    DAVBLA = models.DecimalField(max_digits=18, decimal_places=2)
    DRATEA = models.CharField(max_length=18)
    DCPRTA = models.CharField(max_length=17)
    LNBILA = models.CharField(max_length=11)
    LNACAA = models.DecimalField(max_digits=18, decimal_places=2)
    LNFACA = models.DecimalField(max_digits=18, decimal_places=2)
    LNDLRA = models.CharField(max_length=13)
    LNPDLA = models.CharField(max_length=13)
    LNMTDA = models.CharField(max_length=16)
    LNIDUA = models.DecimalField(max_digits=18, decimal_places=2)
    LNPDTA = models.CharField(max_length=12)
    TMNXMA = models.CharField(max_length=16)
    TMTDYA = models.CharField(max_length=15)
    LND30A = models.CharField(max_length=13)
    LND60A = models.CharField(max_length=13)
    LND90A = models.CharField(max_length=13)
    LNACTA = models.DecimalField(max_digits=18, decimal_places=2)
    LNPMPA = models.DecimalField(max_digits=18, decimal_places=2)
    LNF11A = models.DecimalField(max_digits=18, decimal_places=2)
    LNTRMA = models.CharField(max_length=13)
    LNFRTA = models.CharField(max_length=17)
    LNEONA = models.CharField(max_length=12)
    LNPAMA = models.DecimalField(max_digits=18, decimal_places=2)
    DOY2AA = models.DateField(default=datetime.datetime(1900, 1, 1))
    LNY2AA = models.CharField(max_length=18)
    TMY2AA = models.CharField(max_length=18)
    DMMBLA = models.CharField(max_length=22)
    DMMACA = models.DecimalField(max_digits=18, decimal_places=2)
    DMSCOA = models.CharField(max_length=13)
    LNINBA = models.CharField(max_length=12)
    LNIVAA = models.CharField(max_length=18)
    LNLFDA = models.DecimalField(max_digits=18, decimal_places=2)
    LY2ABA = models.CharField(max_length=18)
    LY2ACA = models.CharField(max_length=18)
    LXBI1A = models.DecimalField(max_digits=18, decimal_places=2)
    LXBI2A = models.DecimalField(max_digits=18, decimal_places=2)
    LXBP1A = models.DecimalField(max_digits=18, decimal_places=2)
    LXBP2A = models.DecimalField(max_digits=18, decimal_places=2)
    LNB12A = models.CharField(max_length=11)
    LY2ASA = models.CharField(max_length=18)
    LNASTA = models.CharField(max_length=13)
    LNTERF = models.CharField(max_length=13)
    LNCONF = models.CharField(max_length=41)
    LXCDTA = models.CharField(max_length=18)
    LXCPBL = models.DecimalField(max_digits=18, decimal_places=2)
    LXCCPR = models.DecimalField(max_digits=18, decimal_places=2)
    LXTREC = models.DecimalField(max_digits=18, decimal_places=2)
    LXBLPR = models.DecimalField(max_digits=18, decimal_places=2)
    LXBLIN = models.DecimalField(max_digits=18, decimal_places=2)
    LXY2AJ = models.CharField(max_length=18)
    DXMTDA = models.DecimalField(max_digits=18, decimal_places=2)
    LXY2AO = models.CharField(max_length=18)
    LNBLTY = models.CharField(max_length=11)
    DXDDRP = models.DecimalField(max_digits=18, decimal_places=2)
    DXDDRA = models.DecimalField(max_digits=18, decimal_places=2)
    DXSCDT = models.CharField(max_length=18)
    LXRENA = models.DecimalField(max_digits=18, decimal_places=2)
    LXREFA = models.DecimalField(max_digits=18, decimal_places=2)
    LXREBA = models.DecimalField(max_digits=18, decimal_places=2)
    LXREPA = models.DecimalField(max_digits=18, decimal_places=2)
    LXREOA = models.CharField(max_length=13)
    LXREIA = models.CharField(max_length=13)
    LXRIBA = models.CharField(max_length=13)
    VNDUEA = models.DecimalField(max_digits=18, decimal_places=2)
    DEMPA = models.CharField(max_length=11)
    TNBFEE = models.CharField(max_length=25)
    TNCFEE = models.DecimalField(max_digits=18, decimal_places=2)
    LXFLDO = models.CharField(max_length=11)
    LXINGF = models.DecimalField(max_digits=18, decimal_places=2)
    LXFECC = models.CharField(max_length=18)
    LXUSRC = models.CharField(max_length=20)
    LXINGU = models.DecimalField(max_digits=18, decimal_places=2)
    LXFECU = models.CharField(max_length=18)
    LXUSRU = models.CharField(max_length=20)
    LXAPRA = models.DecimalField(max_digits=18, decimal_places=2)
    LXSALD = models.DecimalField(max_digits=18, decimal_places=2)
    LXVAIN = models.DecimalField(max_digits=18, decimal_places=2)
    LXADTE = models.CharField(max_length=18)
    LXAUSR = models.CharField(max_length=20)
    LXAPRU = models.DecimalField(max_digits=18, decimal_places=2)
    LXSALU = models.DecimalField(max_digits=18, decimal_places=2)
    LXVAIU = models.DecimalField(max_digits=18, decimal_places=2)
    LXADTU = models.CharField(max_length=18)
    LXAUSU = models.CharField(max_length=20)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vnp003t_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='vnp003t_checker_user_set'
    )

    def __str__(self):
        return self.DACCTA


class AccountHistory(models.Model):
    """AccountHistory resource model"""
    BankId = models.IntegerField()
    AppId = models.IntegerField()
    Acct = models.CharField(max_length=20, primary_key=True)
    RecordDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    TypeId = models.IntegerField()
    TotalBalance = models.DecimalField(max_digits=18, decimal_places=2)
    PrincipalBalance = models.DecimalField(max_digits=18, decimal_places=2)
    InterestBalance = models.DecimalField(max_digits=18, decimal_places=2)
    AverageBalance = models.DecimalField(max_digits=18, decimal_places=2)
    Rate = models.IntegerField()
    DaysPastDue = models.IntegerField()
    InterestMTD = models.DecimalField(max_digits=18, decimal_places=2)
    NumPmtsPastDue = models.DecimalField(max_digits=18, decimal_places=2)
    Num30DPD = models.IntegerField()
    Amt30DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num60DPD = models.IntegerField()
    Amt60DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num90DPD = models.IntegerField()
    Amt90DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num120DPD = models.IntegerField()
    Amt120DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num150DPD = models.IntegerField()
    Amt150DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num180DPD = models.IntegerField()
    Amt180DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Num210DPD = models.IntegerField()
    Amt210DPD = models.DecimalField(max_digits=18, decimal_places=2)
    IntAccruedToDate = models.DecimalField(max_digits=18, decimal_places=2)
    AmountPmtPastDue = models.DecimalField(max_digits=18, decimal_places=2)
    TotalPrinPastDue = models.DecimalField(max_digits=18, decimal_places=2)
    MinBalance = models.DecimalField(max_digits=18, decimal_places=2)
    IntAccruedMTD = models.DecimalField(max_digits=18, decimal_places=2)
    NumDaysOverdrawn = models.IntegerField()
    PrimeRateNum = models.IntegerField()
    LateFees = models.DecimalField(max_digits=18, decimal_places=2)
    PastDueDate1 = models.DateField(default=datetime.datetime(1900, 1, 1))
    PastDueDate2 = models.DateField(default=datetime.datetime(1900, 1, 1))
    PastDueInt1 = models.DecimalField(max_digits=18, decimal_places=2)
    PastDueInt2 = models.DecimalField(max_digits=18, decimal_places=2)
    PastDuePrin1 = models.DecimalField(max_digits=18, decimal_places=2)
    PastDuePrin2 = models.DecimalField(max_digits=18, decimal_places=2)
    LastRcvdPmtDate = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    BlockCode1Date = models.DateField(default=datetime.datetime(1900, 1, 1))
    BlockCodeId1 = models.CharField(max_length=50)
    BlockReason1 = models.CharField(max_length=50)
    BlockCode2Date = models.DateField(default=datetime.datetime(1900, 1, 1))
    BlockCodeId2 = models.CharField(max_length=50)
    BlockReason2 = models.CharField(max_length=50)
    StatusId = models.IntegerField()
    CreditLimit = models.DecimalField(max_digits=18, decimal_places=2)
    CashBalance = models.DecimalField(max_digits=18, decimal_places=2)
    HDelinquency = models.CharField(max_length=50)
    CurrentAmtDue = models.DecimalField(max_digits=18, decimal_places=2)
    ChargeOffStatusId = models.CharField(max_length=50)
    CurrencyId = models.IntegerField()
    LastPmtAmount = models.DecimalField(max_digits=18, decimal_places=2)
    BucketReal = models.IntegerField()
    Gold = models.IntegerField()
    Opened = models.IntegerField()
    ActiveInvoluntary = models.IntegerField()
    Transactor = models.IntegerField()
    OpenedThisMonth = models.IntegerField()
    UpgradedThisMonth = models.IntegerField()
    NRFF = models.DecimalField(max_digits=18, decimal_places=2)
    PFTR = models.DecimalField(max_digits=18, decimal_places=2)
    Profitability = models.DecimalField(max_digits=18, decimal_places=2)
    BehaviorScore = models.IntegerField()
    MOB = models.IntegerField()
    NRFF2 = models.DecimalField(max_digits=18, decimal_places=2)
    LoanStatus = models.CharField(max_length=50)
    LoanTermStatus = models.CharField(max_length=50)
    LoanCondition = models.CharField(max_length=50)
    PCTID = models.CharField(max_length=50)
    BranchId = models.IntegerField()
    OfficerId = models.CharField(max_length=50)
    MaturityDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    TermDays = models.IntegerField()
    ExpirationDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    OpenDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    CancelDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    CapitalCastigado = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoCastigado = models.DecimalField(max_digits=18, decimal_places=2)
    MontoRecuperado = models.DecimalField(max_digits=18, decimal_places=2)
    CurrBillPrin = models.DecimalField(max_digits=18, decimal_places=2)
    CurrBillInt = models.DecimalField(max_digits=18, decimal_places=2)
    CurrBillDueDate = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    MtdAvgBal = models.DecimalField(max_digits=18, decimal_places=2)
    ChargeOffDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    CurrPmtType = models.CharField(max_length=50)
    PrinTranAddr = models.DecimalField(max_digits=18, decimal_places=2)
    AmtTranDDR = models.DecimalField(max_digits=18, decimal_places=2)
    NextSchedBill = models.DateField(default=datetime.datetime(1900, 1, 1))
    ANR = models.DecimalField(max_digits=18, decimal_places=2)
    RISK = models.IntegerField()
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='ah_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='ah_checker_user_set'
    )

    def __str__(self):
        return self.Acct


class CarteraDirigida(models.Model):
    """Cartera Dirigida resource model"""

    class TypeCD(models.IntegerChoices):
        HLP = 6, _('Hipotecario Largo Plazo')
        HCP = 7, _('Hipotecario Corto Plazo')
        TURISMO = 8, _('Turismo')
        MICROFINANCIERO = 9, _('Microfinanciero')
        MANUFACTURA = 10, _('Manufactura')
        AGRICOLA_ICG = 11, _('Agricola ICG')
        AGRICOLA_OTHER_ICG = 12, _('Agricola Other ICG')

    COD_OFICINA = models.CharField(max_length=4)
    COD_CONTABLE = models.CharField(max_length=10)
    NUM_CREDITO = models.CharField(max_length=30, primary_key=True)
    NUM_CREDITO_PRIMER_DESEMBOLSO = models.CharField(max_length=30)
    NUM_DESEMBOLSO = models.CharField(max_length=2)
    NATURALEZA_CLIENTE = models.IntegerField()
    TIPO_CLIENTE = models.IntegerField()
    NUM_CLIENTE = models.CharField(max_length=19)
    NOMBRE_CLIENTE = models.CharField(max_length=250)
    GENERO = models.IntegerField()
    COOPERATIVA = models.IntegerField()
    CLIENTE_NUEVO = models.IntegerField()
    COD_PARROQUIA = models.IntegerField()
    FECHA_SOLICITUD = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_APROBACION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_LIQUIDACION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TIPO_CREDITO = models.IntegerField()
    PLAZO_CREDITO = models.IntegerField()
    CLASE_RIESGO = models.IntegerField()
    ESTADO_CREDITO = models.IntegerField()
    SITUACION_CREDITO = models.IntegerField()
    PERIODO_PAGO_CAPITAL = models.IntegerField()
    PERIODO_PAGO_INTERES = models.IntegerField()
    PERIODO_GRACIA_CAPITAL = models.IntegerField()
    FECHA_VENC_ORIGINAL = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_VENC_ACTUAL = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_REESTRUCTURACION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CANT_PRORROGAS = models.IntegerField()
    FECHA_PRORROGA = models.DateField(default=datetime.datetime(1900, 1, 1))
    CANT_RENOVACIONES = models.IntegerField()
    FECHA_ULTIMA_RENOVACION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_CANCEL = models.DateField(default=datetime.datetime(1900, 1, 1))
    FECHA_VENC_ULTIMA_CUOTA_CAPITAL = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    ULTIMA_FECHA_CANCEL_CUOTA_CAPITAL = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_VENC_ULTIMA_CUOTA_INTERES = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    ULTIMA_FECHA_CANCEL_CUOTA_INTERES = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    MONTO_ORIGINAL = models.DecimalField(max_digits=18, decimal_places=2)
    MONTO_INICIAL = models.DecimalField(max_digits=18, decimal_places=2)
    MONTO_LIQUIDADO_MES = models.DecimalField(max_digits=18, decimal_places=2)
    SALDO = models.DecimalField(max_digits=18, decimal_places=2)
    RENDIMIENTOS_X_COBRAR = models.DecimalField(
        max_digits=18, decimal_places=2)
    RENDIMIENTOS_X_COBRAR_VENCIDOS = models.DecimalField(
        max_digits=18, decimal_places=2)
    PROVISION_ESPECIFICA = models.DecimalField(max_digits=18, decimal_places=2)
    PORCENTAJE_PROVISION_ESPECIFICA = models.DecimalField(
        max_digits=18, decimal_places=2)
    PROVISION_RENDIMIENTO_X_COBRAR = models.DecimalField(
        max_digits=18, decimal_places=2)
    TASA_INTERES_COBRADA = models.DecimalField(max_digits=18, decimal_places=2)
    TASA_INTERES_ACTUAL = models.DecimalField(max_digits=18, decimal_places=2)
    TASA_COMISION = models.DecimalField(max_digits=18, decimal_places=2)
    EROGACIONES_RECUPERABLES = models.DecimalField(
        max_digits=18, decimal_places=2)
    TIPO_GARANTIA_PRINCIPAL = models.IntegerField()
    NUM_CUOTAS = models.IntegerField()
    NUM_CUOTAS_VENCIDAS = models.IntegerField()
    MONTO_VENCIDO_30_DIAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTO_VENCIDO_60_DIAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTO_VENCIDO_90_DIAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTO_VENCIDO_120_DIAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTO_VENCIDO_180_DIAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTO_VENCIDO_ANUAL = models.DecimalField(max_digits=18, decimal_places=2)
    MONTO_VENCIDO_MAYOR_ANUAL = models.DecimalField(
        max_digits=18, decimal_places=2)
    BANCA_SOCIAL = models.IntegerField()
    PRODUCCION_SOCIAL = models.IntegerField()
    MODALIDAD_MICROCREDITO = models.IntegerField()
    USO_FINANCIERO = models.IntegerField()
    DESTINO_RECURSOS_MICROFINANCIEROS = models.IntegerField()
    CANT_TRABAJADORES = models.IntegerField()
    VENTAS_ANUALES = models.DecimalField(max_digits=18, decimal_places=2)
    FECHA_ESTADO_FINANCIERO = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    NUM_RTN = models.CharField(max_length=15)
    LICENCIA_TURISTICA_NACIONAL = models.CharField(max_length=15)
    FECHA_EMISION_FACTIBILIDAD_TECNICA = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    NUM_EXPEDIENTE_FACTIBILIDAD_SOCIOTECNICA = models.CharField(max_length=15)
    NUM_EXPEDIENTE_CONFORMIDAD_TURISTICA = models.CharField(max_length=15)
    NOMBRE_PROYECTO = models.CharField(max_length=200)
    COD_TIPO_PROYECTO = models.IntegerField()
    COD_TIPO_OPERACIONES_FINANCIAMIENTO = models.IntegerField()
    COD_SEGMENTO = models.IntegerField()
    TIPO_ZONA = models.IntegerField()
    FECHA_AUTENTICACION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FECHA_ULTIMA_INSPECCION = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    PORCENTAJE_EJECUCION_PROYECTO = models.DecimalField(
        max_digits=18, decimal_places=2)
    PAGOS_EFECTUADOS_MENSUALES = models.DecimalField(
        max_digits=18, decimal_places=2)
    MONTOS_LIQUIDADOS_CIERRE = models.DecimalField(
        max_digits=18, decimal_places=2)
    AMORTIZACIONES_CAPITAL_ACUMULADAS = models.DecimalField(
        max_digits=18, decimal_places=2)
    TASA_INCENTIVO = models.DecimalField(max_digits=18, decimal_places=2)
    NUMERO_OFICIO_INCENTIVO = models.CharField(max_length=15)
    NUM_REGISTRO = models.CharField(max_length=20)
    TIPO_REGISTRO = models.CharField(max_length=50)
    FECHA_VENC_REGISTRO = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TIPO_SUBSECTOR = models.CharField(max_length=1)
    RUBRO = models.CharField(max_length=8)
    COD_USO = models.CharField(max_length=12)
    CANT = models.CharField(max_length=16)
    COD_UNIDAD_MEDIDA = models.CharField(max_length=2)
    SECTOR_PRODUCCION = models.CharField(max_length=1)
    CANT_HECTAREAS = models.CharField(max_length=11)
    SUPERFICIE_TOTAL = models.CharField(max_length=11)
    NUM_BENEFICIARIOS = models.CharField(max_length=4)
    PRIORITARIO = models.CharField(max_length=1)
    DESTINO_MANUFACTURERO = models.CharField(max_length=5)
    DESTINO_ECONOMICO = models.CharField(max_length=1)
    TIPO_BENEFICIARIO = models.CharField(max_length=1)
    MODALIDAD_HIPOTECARIA = models.CharField(max_length=1)
    INGRESO_FAMILIAR = models.CharField(max_length=1)
    MONTO_LIQUIDADO_ANUAL = models.DecimalField(
        max_digits=18, decimal_places=2)
    SALDO_CREDITO_31_12 = models.DecimalField(max_digits=18, decimal_places=2)
    CANT_VIVIENDAS = models.CharField(max_length=5)
    TYPE_CD = models.IntegerField(choices=TypeCD.choices)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cd_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='cd_checker_user_set'
    )

    def __str__(self):
        return self.NUM_CREDITO


class RendimientosCobrarConsumer(models.Model):
    """Rendimientos por Cobrar Consumer resource model"""
    Acct = models.CharField(max_length=20, primary_key=True)
    SaldoRendXcobrar = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendXcobrarVenc = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendCuentaOrden = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendXMora = models.DecimalField(max_digits=18, decimal_places=2)
    ProvisionREND = models.DecimalField(max_digits=3, decimal_places=2)
    Saldo_Provision_REND = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rend_other_icg_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='rend_other_icg_checker_user_set'
    )

    def __str__(self):
        return self.Acct


class SIIF(models.Model):
    """SIIF resource model"""
    BranchId = models.IntegerField()
    Acct = models.CharField(max_length=20, primary_key=True)
    OpenDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    DaysPastDue = models.IntegerField()
    RecordDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    MaturityDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    CreditLimit = models.DecimalField(max_digits=18, decimal_places=2)
    Rate = models.DecimalField(max_digits=18, decimal_places=7)
    NumPmtsPastDue = models.IntegerField()
    AmtPmtPastDue = models.DecimalField(max_digits=18, decimal_places=2)
    Amt30DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt60DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt90DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt120DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt150DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt180DPD = models.DecimalField(max_digits=18, decimal_places=2)
    Amt210DPD = models.DecimalField(max_digits=18, decimal_places=2)
    LoanStatus = models.CharField(max_length=50)
    SaldoCastigado = models.DecimalField(max_digits=18, decimal_places=2)
    CloseDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    BlockCodeId1 = models.CharField(max_length=2)
    BlockReason1 = models.CharField(max_length=2)
    BlockCode1Date = models.DateField(default=datetime.datetime(1900, 1, 1))
    PrincipalBalance = models.DecimalField(max_digits=18, decimal_places=2)
    TypeId = models.IntegerField()
    Gender = models.CharField(max_length=50)
    FullName = models.CharField(max_length=50)
    ActivityId = models.IntegerField()
    OccupationId = models.IntegerField()
    ProfessionId = models.IntegerField()
    RelId = models.IntegerField()
    DivisionTypeId = models.CharField(max_length=2)
    Agro = models.IntegerField()
    Micro = models.IntegerField()
    FondoEstadal = models.IntegerField()
    Rewrite = models.IntegerField()
    CtaLocal = models.CharField(max_length=20)
    Cid = models.CharField(max_length=50)
    Situacion_Credito = models.IntegerField()
    SaldoCapital = models.DecimalField(max_digits=18, decimal_places=2)
    SaldoRendimientos = models.DecimalField(max_digits=18, decimal_places=2)
    Mora = models.DecimalField(max_digits=18, decimal_places=2)
    ClaseRiesgo = models.CharField(max_length=2)
    CuotasVencidas = models.IntegerField()
    EstadoCredito = models.IntegerField()
    OldAcct = models.CharField(max_length=20)
    OrigOpenDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    OrigCreditLimit = models.DecimalField(max_digits=18, decimal_places=2)
    OrigTypeId = models.IntegerField()
    Staff = models.IntegerField()
    Purchases = models.CharField(max_length=50)
    FeePaid = models.CharField(max_length=50)
    DireccionH = models.CharField(max_length=50)
    DireccionO = models.CharField(max_length=50)
    DireccionB = models.CharField(max_length=50)
    Int_Efectivamente_Cobrado = models.DecimalField(
        max_digits=18, decimal_places=2)
    Porcentaje_Comsion_Flat = models.DecimalField(
        max_digits=3, decimal_places=2)
    Monto_Comision_Flat = models.DecimalField(max_digits=18, decimal_places=2)
    Periodicidad_Pago_Especial_Capital = models.IntegerField()
    Fecha_Cambio_Status = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Fecha_Reg_Venc_Lit_cast = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Fecha_Exigibilidad_pago_ult_cuota = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Fecha_Fin_Periodo_gracia_Pago_interes = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Capital_Trasferido = models.DecimalField(max_digits=18, decimal_places=2)
    Fecha_cambio_Capital_Transferido = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Tipo_Vivienda = models.IntegerField()
    Provision = models.DecimalField(max_digits=3, decimal_places=2)
    SaldoProvision = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='siif_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='siif_checker_user_set'
    )

    def __str__(self):
        return self.Acct


class FDN(models.Model):
    """Fecha de Nacimiento resource model"""
    TipoCliente = models.CharField(max_length=2)
    IdCliente = models.CharField(max_length=20)
    FechaNacimiento = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FullName = models.CharField(max_length=50)
    RecordDate = models.DateField(default=datetime.datetime(1900, 1, 1))
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='fdn_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='fdn_checker_user_set'
    )

    class Meta:
        unique_together = (('TipoCliente', 'IdCliente'),)


    def __str__(self):
        return self.TipoCliente & self.IdCliente


class VZDWAMBS(models.Model):
    """VZDWAMBS resource model"""
    ORG = models.CharField(max_length=3)
    ACCT = models.CharField(max_length=19, primary_key=True)
    CUSTORG = models.CharField(max_length=3)
    CUSTNBR = models.CharField(max_length=19)
    RELORG = models.CharField(max_length=3)
    RELNBR = models.CharField(max_length=19)
    PRICARD = models.CharField(max_length=19)
    LOGO = models.IntegerField()
    SOURCECODE = models.CharField(max_length=15)
    DATEXFREFF = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATEBLOCK1 = models.DateField(default=datetime.datetime(1900, 1, 1))
    BLOCKCODE1 = models.CharField(max_length=1)
    BLOCKREASON1 = models.CharField(max_length=2)
    BLOCKCODE2 = models.CharField(max_length=1)
    BLOCKREASON2 = models.CharField(max_length=2)
    DATEBLOCK2 = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATECLOSE = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATELASTMAINT = models.DateField(default=datetime.datetime(1900, 1, 1))
    STATEOFISSUE = models.CharField(max_length=3)
    INTSTATUS = models.CharField(max_length=2)
    DATELASTSTATEX = models.DateField(default=datetime.datetime(1900, 1, 1))
    XFRORG = models.CharField(max_length=3)
    XFRLOGO = models.IntegerField()
    XFRACCT = models.CharField(max_length=19)
    DATECARDEXP = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATEOPENED = models.DateField(default=datetime.datetime(1900, 1, 1))
    BILLINGCYCLE = models.IntegerField()
    DATELASTSTM = models.DateField(default=datetime.datetime(1900, 1, 1))
    CURRBAL = models.DecimalField(max_digits=18, decimal_places=2)
    HIBAL = models.DecimalField(max_digits=18, decimal_places=2)
    DATEHIBAL = models.DateField(default=datetime.datetime(1900, 1, 1))
    CRLIM = models.DecimalField(max_digits=18, decimal_places=2)
    CASHBAL = models.DecimalField(max_digits=18, decimal_places=2)
    DATECRBAL = models.DateField(default=datetime.datetime(1900, 1, 1))
    LASTCRLIM = models.DecimalField(max_digits=18, decimal_places=2)
    DATELINEDEC = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATELINEINC = models.DateField(default=datetime.datetime(1900, 1, 1))
    HISTORY = models.CharField(max_length=48)
    FILLER = models.CharField(max_length=4)
    PMTCURRDUE = models.DecimalField(max_digits=18, decimal_places=2)
    PMTPASTCTR = models.IntegerField()
    PMTPASTDUE = models.DecimalField(max_digits=18, decimal_places=2)
    PMT30CTR = models.IntegerField()
    PMT30 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT60CTR = models.IntegerField()
    PMT60 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT90CTR = models.IntegerField()
    PMT90 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT120CTR = models.IntegerField()
    PMT120 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT150CTR = models.IntegerField()
    PMT150 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT180CTR = models.IntegerField()
    PMT180 = models.DecimalField(max_digits=18, decimal_places=2)
    PMT210CTR = models.IntegerField()
    PMT210 = models.DecimalField(max_digits=18, decimal_places=2)
    CHGOFFSTATUS = models.CharField(max_length=1)
    DATECGOFF = models.DateField(default=datetime.datetime(1900, 1, 1))
    AMTCGOFF = models.DecimalField(max_digits=18, decimal_places=2)
    CHGOFFRSN1 = models.CharField(max_length=1)
    CHGOFFRSN2 = models.CharField(max_length=1)
    RISKLEVEL = models.CharField(max_length=1)
    NBRUNBLKCARD = models.CharField(max_length=6)
    NBRNSF = models.CharField(max_length=4)
    LASTYTDINT = models.CharField(max_length=13)
    LASTYTDINTPAID = models.CharField(max_length=13)
    CURRYTDINDPAID = models.CharField(max_length=13)
    DATELASTPURCH = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATELASTRETURN = models.CharField(max_length=8)
    DATELASTACT = models.CharField(max_length=8)
    CARDUSAGE = models.CharField(max_length=1)
    FITESTDIGITS = models.CharField(max_length=2)
    FIAMTATRISKFACTOR = models.CharField(max_length=7)
    FIAMTATRISK = models.CharField(max_length=10)
    FISPID = models.CharField(max_length=2)
    FIREPRSCENID = models.CharField(max_length=4)
    FIREPRSTRAGID = models.CharField(max_length=4)
    FICOMMSCENID = models.CharField(max_length=4)
    FICOMMSTRAGID = models.CharField(max_length=4)
    FIDELQSCENID = models.CharField(max_length=4)
    FIDELQSTRAGID = models.CharField(max_length=4)
    FIAUTHSCENID = models.CharField(max_length=4)
    FIAUTHSTRAGID = models.CharField(max_length=4)
    FICRLIMSCENID = models.CharField(max_length=4)
    FICRLIMSTRAGID = models.CharField(max_length=4)
    FIOVLMSCENID = models.CharField(max_length=4)
    FIOVLMSTRAGID = models.CharField(max_length=4)
    FICURRBEHAVIORSCORE = models.IntegerField()
    FICRLIMITCTRLIND = models.CharField(max_length=1)
    OVERLIMNBROFCYCLES = models.CharField(max_length=3)
    TYPEOFACCT = models.CharField(max_length=1)
    DATECARDFEE = models.CharField(max_length=8)
    WAIVFEE = models.CharField(max_length=1)
    DDAACCTNBR = models.CharField(max_length=19)
    EMPLOYEECODE = models.CharField(max_length=2)
    CYCANRBAL = models.CharField(max_length=19)
    CYCANRDAYS = models.CharField(max_length=3)
    MTHANRBAL = models.DecimalField(max_digits=18, decimal_places=2)
    MTHANRDAYS = models.IntegerField()
    DATEPMTDUE = models.DateField(default=datetime.datetime(1900, 1, 1))
    DATELASTPMT = models.DateField(default=datetime.datetime(1900, 1, 1))
    PMTLASTAMT = models.DecimalField(max_digits=18, decimal_places=2)
    FILLER2 = models.CharField(max_length=62)
    CHANNELID = models.CharField(max_length=1)
    SOURCEID = models.IntegerField()
    CAMPAIGNID = models.IntegerField()
    TESTID = models.IntegerField()
    SEGMENTID = models.IntegerField()
    DAYSPASTDUE = models.IntegerField()
    NUMPMTSPASTDUE = models.IntegerField()
    BUCKETREAL = models.IntegerField()
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vzdwambs_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='vzdwambs_checker_user_set'
    )

    def __str__(self):
        return self.ACCT
