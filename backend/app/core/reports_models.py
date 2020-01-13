import datetime

from django.db import models
from django.conf import settings


# Reports

# AT04

class AT04(models.Model):
    """AT04 report model"""
    NumeroCredito = models.CharField(max_length=20, primary_key=True)
    FechaLiquidacion = models.DateField(default=datetime.datetime(1900, 1, 1))
    FechaSolicitud = models.DateField(default=datetime.datetime(1900, 1, 1))
    FechaAprobacion = models.DateField(default=datetime.datetime(1900, 1, 1))
    Oficina = models.IntegerField()  # TODO: Add SBUR46 Relation
    CodigoContable = models.CharField(
        max_length=20)  # TODO: Add SBUR02 Relation
    NumeroCreditoPrimerDesembolso = models.CharField(max_length=20)
    NumeroDesembolso = models.IntegerField()
    CodigoLineaCredito = models.ManyToManyField(
        'core.SB31', related_name='clc_at04_set')
    MontoLineaCredito = models.DecimalField(max_digits=18, decimal_places=2)
    EstadoCredito = models.ManyToManyField('core.SB34')
    TipoCredito = models.ManyToManyField('core.SB09')
    SituacionCredito = models.ManyToManyField('core.SB35')
    PlazoCredito = models.ManyToManyField('core.SB68')
    ClasificacionRiesgo = models.ManyToManyField('core.SB19')
    DestinoCredito = models.ManyToManyField(
        'core.SB10', related_name='dc_at04_set')
    NaturalezaCliente = models.ManyToManyField('core.SB76')
    TipoCliente = models.ManyToManyField(
        'core.SB16', related_name='tc_at04_set')
    IdentificacionCliente = models.CharField(max_length=20)
    Nombre_RazonSocial = models.CharField(max_length=200)
    Genero = models.ManyToManyField('core.SB59')
    TipoClienteRIF = models.ManyToManyField(
        'core.SB16', related_name='tcr_at04_set')
    IdentificacionTipoClienteRIF = models.CharField(max_length=20)
    ActividadCliente = models.ManyToManyField(
        'core.SB10', related_name='ac_at04_set')
    PaisNacionalidad = models.ManyToManyField('core.SB03')
    DomicilioFiscal = models.CharField(max_length=200)
    ClienteNuevo = models.ManyToManyField(
        'core.SB31', related_name='cn_at04_set')
    Cooperativa = models.ManyToManyField(
        'core.SB31', related_name='coop_at04_set')
    Sindicado = models.DecimalField(max_digits=18, decimal_places=4)
    BancoLiderSindicato = models.IntegerField()  # TODO: Add SBUR01 Relation
    RelacionCrediticia = models.ManyToManyField(
        'core.SB31', related_name='rc_at04_set')
    GrupoEconomicoFinanciero = models.ManyToManyField(
        'core.SB31', related_name='gef_at04_set')
    NombreGrupoEconomicoFinanciero = models.CharField(max_length=100)
    CodigoParroquia = models.CharField(
        max_length=20)  # TODO: Add SBUR04 Relation
    PeriodoGraciaCapital = models.IntegerField()
    PeriodicidadPagoCapital = models.ManyToManyField(
        'core.SB30', related_name='ppc_at04_set')
    PeriodicidadPagoInteresCredito = models.ManyToManyField(
        'core.SB30', related_name='ppi_at04_set')
    FechaVencimientoOriginal = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaVencimientoActual = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaReestructuracion = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CantidadProrroga = models.IntegerField()
    FechaProrroga = models.DateField(default=datetime.datetime(1900, 1, 1))
    CantidadRenovaciones = models.IntegerField()
    FechaUltimaRenovacion = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaCancelacionTotal = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaVencimientoUltimaCoutaCapital = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    UltimaFechaCancelacionCuotaCapital = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaVencimientoUltimaCuotaInteres = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    UltimaFechaCancelacionCuotaIntereses = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    Moneda = models.ManyToManyField('core.SB15')
    TipoCambioOriginal = models.DecimalField(max_digits=18, decimal_places=4)
    TipoCambioCierreMes = models.DecimalField(max_digits=18, decimal_places=4)
    MontoOriginal = models.DecimalField(max_digits=18, decimal_places=2)
    MontoInicial = models.DecimalField(max_digits=18, decimal_places=2)
    MontoLiquidadoMes = models.DecimalField(max_digits=18, decimal_places=2)
    EntePublico = models.IntegerField()  # TODO: Add SBUR28 Relation
    MontoInicialTerceros = models.DecimalField(max_digits=18, decimal_places=2)
    Saldo = models.DecimalField(max_digits=18, decimal_places=2)
    RendimientosCobrar = models.DecimalField(max_digits=18, decimal_places=2)
    RendimientosCobrarVencidos = models.DecimalField(
        max_digits=18, decimal_places=2)
    RendimientosCobrarMora = models.DecimalField(
        max_digits=18, decimal_places=2)
    ProvisionEspecifica = models.DecimalField(max_digits=18, decimal_places=2)
    PocentajeProvisionEspecifica = models.DecimalField(
        max_digits=18, decimal_places=4)
    ProvisionRendimientoCobrar = models.DecimalField(
        max_digits=18, decimal_places=2)
    TasasInteresCobrada = models.DecimalField(max_digits=18, decimal_places=4)
    TasasInteresActual = models.DecimalField(max_digits=18, decimal_places=4)
    IndicadorTasaPreferencial = models.ManyToManyField(
        'core.SB31', related_name='itp_at04_set')
    TasaComision = models.DecimalField(max_digits=18, decimal_places=4)
    ComisionesCobrar = models.DecimalField(max_digits=18, decimal_places=2)
    ComisionesCobradas = models.DecimalField(max_digits=18, decimal_places=2)
    ErogacionesRecuperables = models.DecimalField(
        max_digits=18, decimal_places=2)
    TipoGarantiaPrincipal = models.ManyToManyField('core.SB11')
    NumeroCuotas = models.IntegerField()
    NumeroCuotasVencidas = models.IntegerField()
    MontoVencido30dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencido60dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencido90dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencido120dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencido180dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencidoUnAno = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencidoMasUnAno = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencer30dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencer60dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencer90dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencer120dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencer180dias = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencerUnAno = models.DecimalField(max_digits=18, decimal_places=2)
    MontoVencerMasUnAno = models.DecimalField(max_digits=18, decimal_places=2)
    BancaSocial = models.ManyToManyField(
        'core.SB31', related_name='bs_at04_set')
    UnidadProduccionSocial = models.ManyToManyField(
        'core.SB31', related_name='ups_at04_set')
    ModalidadMicrocredito = models.ManyToManyField('core.SB81')
    UsoFinanciero = models.ManyToManyField('core.SB82')
    DestinoRecursosMicrofinancieros = models.ManyToManyField('core.SB83')
    CantidadTrabajadores = models.IntegerField()
    VentaAnuales = models.DecimalField(max_digits=18, decimal_places=2)
    FechaEstadoFinanciero = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    NumeroRTN = models.CharField(max_length=50)
    LicenciaTuristicaNacional = models.CharField(max_length=50)
    FechaEmisionFactibilidadSociotecnica_ConformidadTuristica = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    # TODO: Add SBUR84 Relation
    NumeroExpedienteFactibilidadSociotecnica = models.IntegerField()
    # TODO: Add SBUR84 Relation
    NumeroExpedienteConformidadTuristica = models.IntegerField()
    NombreProyectoUnidadProduccion = models.CharField(max_length=200)
    DireccionProyectoUnidadProduccion = models.CharField(max_length=250)
    CodigoTipoProyecto = models.ManyToManyField('core.SB85')
    CodigoTipoOperacionesFinanciamiento = models.ManyToManyField('core.SB100')
    CodigoSegmento = models.ManyToManyField('core.SB101')
    TipoZona = models.ManyToManyField('core.SB102')
    FechaAutenticacionProtocolizacion = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaUltimaInspeccion = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    PorcentajeEjecucionProyecto = models.DecimalField(
        max_digits=18, decimal_places=4)
    PagosEfectuadosDuranteMes = models.DecimalField(
        max_digits=18, decimal_places=2)
    MontosLiquidadosFechaCierre = models.DecimalField(
        max_digits=18, decimal_places=2)
    AmortizacionesCapitalAcumuladasFecha = models.DecimalField(
        max_digits=18, decimal_places=2)
    TasaIncentivo = models.ManyToManyField(
        'core.SB31', related_name='ti_at04_set')
    NumeroOficioIncentivo = models.CharField(max_length=50)
    NumeroRegistro_ConstanciaMPPAT = models.IntegerField()
    TipoRegistro_ConstanciaMPPAT = models.CharField(max_length=50)
    FechaVencimientoRegistro_ConstanciaMPPAT = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TipoSubsector = models.ManyToManyField('core.SB103')
    Rubro = models.ManyToManyField('core.SB88')
    CodigoUso = models.ManyToManyField('core.SB66')
    CantidadUnidades = models.DecimalField(max_digits=18, decimal_places=2)
    CodigoUnidadMedida = models.ManyToManyField('core.SB67')
    SectorProduccion = models.ManyToManyField('core.SB87')
    CantidadHectareas = models.DecimalField(max_digits=18, decimal_places=4)
    SuperficieTotalPropiedad = models.DecimalField(
        max_digits=18, decimal_places=4)
    NumeroProductoresBeneficiarios = models.IntegerField()
    Prioritario = models.ManyToManyField(
        'core.SB31', related_name='priori_at04_set')
    DestinoManufacturero = models.ManyToManyField(
        'core.SB92', related_name='dm_at04_set')
    DestinoEconomico = models.ManyToManyField(
        'core.SB105', related_name='de_at04_set')
    TipoBeneficiario = models.ManyToManyField(
        'core.SB31', related_name='tb_at04_set')
    ModalidadHipoteca = models.ManyToManyField('core.SB90')
    IngresoFamiliar = models.DecimalField(max_digits=18, decimal_places=2)
    MontoLiquidadoDuranteAnoCurso = models.DecimalField(
        max_digits=18, decimal_places=2)
    SaldoCredito31_12 = models.DecimalField(max_digits=18, decimal_places=2)
    CantidadViviendasConstruir = models.IntegerField()
    RendimientosCobrarReestructurados = models.DecimalField(
        max_digits=18, decimal_places=2)
    RendimientosCobrarAfectosReporto = models.DecimalField(
        max_digits=18, decimal_places=2)
    RendimientosCobrarLitigio = models.DecimalField(
        max_digits=18, decimal_places=2)
    InteresEfectivamenteCobrado = models.DecimalField(
        max_digits=18, decimal_places=2)
    PorcentajeComisionFlat = models.DecimalField(
        max_digits=18, decimal_places=4)
    MontoComisionFlat = models.DecimalField(max_digits=18, decimal_places=2)
    PeriocidadPagoEspecialCapital = models.ManyToManyField('core.SB30')
    FechaCambioEstatusCredito = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaRegistroVencidaLitigiooCastigada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaExigibilidadPagoUltimaCuotaPagada = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CuentaContableProvisionEspecifica = models.CharField(
        max_length=20)  # TODO: Add SBUR02 Relation
    CuentaContableProvisionRendimiento = models.CharField(
        max_length=20)  # TODO: Add SBUR02 Relation
    CuentaContableInteresCuentaOrden = models.CharField(
        max_length=20)  # TODO: Add SBUR02 Relation
    MontoInteresCuentaOrden = models.DecimalField(
        max_digits=18, decimal_places=2)
    TipoIndustria = models.ManyToManyField('core.SB136')
    TipoBeneficiarioSectorManufacturero = models.ManyToManyField('core.SB137')
    TipoBeneficiarioSectorTurismo = models.ManyToManyField('core.SB140')
    BeneficiarioEspecial = models.IntegerField()
    FechaEmisionCertificacionBeneficiarioEspecial = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    TipoVivienda = models.ManyToManyField('core.SB138')
    FechaFinPeriodoGraciaPagoInteres = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    CapitalTransferido = models.DecimalField(max_digits=18, decimal_places=2)
    FechaCambioEstatusCapitalTransferido = models.DateField(
        default=datetime.datetime(1900, 1, 1))
    FechaNacimiento = models.DateField(default=datetime.datetime(1900, 1, 1))
    UnidadValoracionAT04 = models.DecimalField(max_digits=18, decimal_places=2)
    MakerDate = models.DateField(default=datetime.date.today)
    MakerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='at04_maker_user_set'
    )
    CheckerDate = models.DateField(default=datetime.date.today)
    CheckerUser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='at04_checker_user_set'
    )

    def __str__(self):
        return self.NumeroCredito
