"""AT04 Report Creation Module"""
import pandas as pd
import numpy as np
import os
import sys
import string
import ntpath
import datetime

from pathlib import Path

from django.conf import settings

pd.set_option('display.precision', 4)
pd.options.display.float_format = '{:.2f}'.format

#  RESOURCE PATH

RESOURCES_PATH = os.path.join(settings.MEDIA_ROOT, 'resources')
AH_PATH = os.path.join(RESOURCES_PATH, 'AH.txt')
AT04_PAST_PATH = os.path.join(RESOURCES_PATH, 'AT04.txt')
AT04CRE_PATH = os.path.join(RESOURCES_PATH, 'AT04CRE.txt')
AT07_PATH = os.path.join(RESOURCES_PATH, 'AT07.txt')
BBAT_PATH = os.path.join(RESOURCES_PATH, 'BBAT.txt')
CD_PATH = os.path.join(RESOURCES_PATH, 'CD.txt')
CND_PATH = os.path.join(RESOURCES_PATH, 'CND.txt')
FDN_PATH = os.path.join(RESOURCES_PATH, 'FDN.txt')
GICG_PATH = os.path.join(RESOURCES_PATH, 'GICG.txt')
LNP860_PATH = os.path.join(RESOURCES_PATH, 'LNP860.txt')
MISP_PATH = os.path.join(RESOURCES_PATH, 'MISP.txt')
MM_PATH = os.path.join(RESOURCES_PATH, 'MM.txt')
PPRRHH_PATH = os.path.join(RESOURCES_PATH, 'PPRRHH.txt')
RICG_PATH = os.path.join(RESOURCES_PATH, 'RICG.txt')
SC_PATH = os.path.join(RESOURCES_PATH, 'SC.txt')
SIIF_PATH = os.path.join(RESOURCES_PATH, 'SIIF.txt')
VNP003T_PATH = os.path.join(RESOURCES_PATH, 'VNP003T.txt')
CFGESIIFCITI_PATH = os.path.join(RESOURCES_PATH, 'CFGESIIFCITI.txt')  # Tabla equivalencias Actividad Cliente
CC_PATH = os.path.join(RESOURCES_PATH, 'CC.txt')  # Clientes Consumo

CD_CHOICES = {
    'CCA_CONSUMO': 1,  # Cartera de Creditos al Consumo
    'CCH': 2,  # Credicheque
    'PIL': 3,  # Pils
    'REWRITES': 4,  # Rewrites
    'TDC': 5,  # Tarjetas de Credito
    'HLP': 6,  # Hipotecario Largo Plazo
    'HCP': 7,  # Hipotecario Corto Plazo
    'TURISMO': 8,  # Turismo
    'MICROFINANCIERO': 9,  # Microfinanciero
    'MANUFACTURA': 10,  # Manufactura
    'AGRICOLA_ICG': 11,  # Agricola ICG
    'AGRICOLA_OTHER_ICG': 12,  # Agricola Other ICG
    'ICG_NO_DIRIGIDA': 13,  # Corporativa No Dirigida
    'CARROS': 14,  # Carros
    'SEGUROS': 15,  # PIL Seguros
    'SOBREGIROS': 16,  # Sobregiros
    'RRHH': 17,  # Prestaciones Recursos Humanos
}

DEFAULT_DATE = pd.to_datetime('1900-01-01')


class ReportCreation():
    """Data Preparation Class for every resource file"""
    _out_folder = 'reports'
    _out_path = os.path.join(settings.MEDIA_ROOT, _out_folder)

    _fecha_reportar = DEFAULT_DATE

    _labels = [
        'NumeroCredito',
        'FechaLiquidacion',
        'FechaSolicitud',
        'FechaAprobacion',
        'Oficina',
        'CodigoContable',
        'NumeroCreditoPrimerDesembolso',
        'NumeroDesembolso',
        'CodigoLineaCredito',
        'MontoLineaCredito',
        'EstadoCredito',
        'TipoCredito',
        'SituacionCredito',
        'PlazoCredito',
        'ClasificacionRiesgo',
        'DestinoCredito',
        'NaturalezaCliente',
        'TipoCliente',
        'IdentificacionCliente',
        'Nombre_RazonSocial',
        'Genero',
        'TipoClienteRIF',
        'IdentificacionTipoClienteRIF',
        'ActividadCliente',
        'PaisNacionalidad',
        'DomicilioFiscal',
        'ClienteNuevo',
        'Cooperativa',
        'Sindicado',
        'BancoLiderSindicato',
        'RelacionCrediticia',
        'GrupoEconomicoFinanciero',
        'NombreGrupoEconomicoFinanciero',
        'CodigoParroquia',
        'PeriodoGraciaCapital',
        'PeriodicidadPagoCapital',
        'PeriodicidadPagoInteresCredito',
        'FechaVencimientoOriginal',
        'FechaVencimientoActual',
        'FechaReestructuracion',
        'CantidadProrroga',
        'FechaProrroga',
        'CantidadRenovaciones',
        'FechaUltimaRenovacion',
        'FechaCancelacionTotal',
        'FechaVencimientoUltimaCoutaCapital',
        'UltimaFechaCancelacionCuotaCapital',
        'FechaVencimientoUltimaCuotaInteres',
        'UltimaFechaCancelacionCuotaIntereses',
        'Moneda',
        'TipoCambioOriginal',
        'TipoCambioCierreMes',
        'MontoOriginal',
        'MontoInicial',
        'MontoLiquidadoMes',
        'EntePublico',
        'MontoInicialTerceros',
        'Saldo',
        'RendimientosCobrar',
        'RendimientosCobrarVencidos',
        'RendimientosCobrarMora',
        'ProvisionEspecifica',
        'PorcentajeProvisionEspecifica',
        'ProvisionRendimientoCobrar',
        'TasasInteresCobrada',
        'TasasInteresActual',
        'IndicadorTasaPreferencial',
        'TasaComision',
        'ComisionesCobrar',
        'ComisionesCobradas',
        'ErogacionesRecuperables',
        'TipoGarantiaPrincipal',
        'NumeroCuotas',
        'NumeroCuotasVencidas',
        'MontoVencido30dias',
        'MontoVencido60dias',
        'MontoVencido90dias',
        'MontoVencido120dias',
        'MontoVencido180dias',
        'MontoVencidoUnAno',
        'MontoVencidoMasUnAno',
        'MontoVencer30dias',
        'MontoVencer60dias',
        'MontoVencer90dias',
        'MontoVencer120dias',
        'MontoVencer180dias',
        'MontoVencerUnAno',
        'MontoVencerMasUnAno',
        'BancaSocial',
        'UnidadProduccionSocial',
        'ModalidadMicrocredito',
        'UsoFinanciero',
        'DestinoRecursosMicrofinancieros',
        'CantidadTrabajadores',
        'VentaAnuales',
        'FechaEstadoFinanciero',
        'NumeroRTN',
        'LicenciaTuristicaNacional',
        'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica',
        'NumeroExpedienteFactibilidadSociotecnica',
        'NumeroExpedienteConformidadTuristica',
        'NombreProyectoUnidadProduccion',
        'DireccionProyectoUnidadProduccion',
        'CodigoTipoProyecto',
        'CodigoTipoOperacionesFinanciamiento',
        'CodigoSegmento',
        'TipoZona',
        'FechaAutenticacionProtocolizacion',
        'FechaUltimaInspeccion',
        'PorcentajeEjecucionProyecto',
        'PagosEfectuadosDuranteMes',
        'MontosLiquidadosFechaCierre',
        'AmortizacionesCapitalAcumuladasFecha',
        'TasaIncentivo',
        'NumeroOficioIncentivo',
        'NumeroRegistro_ConstanciaMPPAT',
        'TipoRegistro_ConstanciaMPPAT',
        'FechaVencimientoRegistro_ConstanciaMPPAT',
        'TipoSubsector',
        'Rubro',
        'CodigoUso',
        'CantidadUnidades',
        'CodigoUnidadMedida',
        'SectorProduccion',
        'CantidadHectareas',
        'SuperficieTotalPropiedad',
        'NumeroProductoresBeneficiarios',
        'Prioritario',
        'DestinoManufacturero',
        'DestinoEconomico',
        'TipoBeneficiario',
        'ModalidadHipoteca',
        'IngresoFamiliar',
        'MontoLiquidadoDuranteAnoCurso',
        'SaldoCredito31_12',
        'CantidadViviendasConstruir',
        'RendimientosCobrarReestructurados',
        'RendimientosCobrarAfectosReporto',
        'RendimientosCobrarLitigio',
        'InteresEfectivamenteCobrado',
        'PorcentajeComisionFlat',
        'MontoComisionFlat',
        'PeriocidadPagoEspecialCapital',
        'FechaCambioEstatusCredito',
        'FechaRegistroVencidaLitigiooCastigada',
        'FechaExigibilidadPagoUltimaCuotaPagada',
        'CuentaContableProvisionEspecifica',
        'CuentaContableProvisionRendimiento',
        'CuentaContableInteresCuentaOrden',
        'MontoInteresCuentaOrden',
        'TipoIndustria',
        'TipoBeneficiarioSectorManufacturero',
        'TipoBeneficiarioSectorTurismo',
        'BeneficiarioEspecial',
        'FechaEmisionCertificacionBeneficiarioEspecial',
        'TipoVivienda',
        'FechaFinPeriodoGraciaPagoInteres',
        'CapitalTransferido',
        'FechaCambioEstatusCapitalTransferido',
        'FechaNacimiento',
        'UnidadValoracionAT04',
    ]

    # %%
    #  DEFINING RESOURCES
    ah_df = pd.DataFrame()
    at04_past_df = pd.DataFrame()
    at04cre_df = pd.DataFrame()
    at07_df = pd.DataFrame()
    bbat_df = pd.DataFrame()
    cd_df = pd.DataFrame()
    cnd_df = pd.DataFrame()
    fdn_df = pd.DataFrame()
    gicg_df = pd.DataFrame()
    lnp860_df = pd.DataFrame()
    misp_df = pd.DataFrame()
    mm_df = pd.DataFrame()
    pprrhh_df = pd.DataFrame()
    ricg_df = pd.DataFrame()
    sc_df = pd.DataFrame()
    vnp003t_df = pd.DataFrame()
    siif_df = pd.DataFrame()
    cc_df = pd.DataFrame()
    cfgesiifciti_df = pd.DataFrame()
    at04cre_mod_df = pd.DataFrame()
    at04cre_cfgesc_df = pd.DataFrame()
    siif_cfgesc_df = pd.DataFrame()
    gicg_mod_df = pd.DataFrame()
    cnd_mod_df = pd.DataFrame()
    bbat_mod_df = pd.DataFrame()
    siif_mod_df = pd.DataFrame()
    lnp860_mod_df = pd.DataFrame()
    misp_mod_df = pd.DataFrame()
    vnp003t_mod_df = pd.DataFrame()
    cc_mod_df = pd.DataFrame()
    ah_mod_df = pd.DataFrame()
    at04cre_cnd_df = pd.DataFrame()
    ricg_mod_df = pd.DataFrame()

    at04_df = pd.DataFrame()

    # %%
    def set_dataframes(self):
        """Creates and Sets the Dataframes to be used"""
        #  IMPORTING RESOURCES
        self.ah_df = pd.read_csv(
            AH_PATH, sep='~', low_memory=False, encoding='latin')
        self.at04_past_df = pd.read_csv(AT04_PAST_PATH, sep='~',
                                        low_memory=False, encoding='latin')
        self.at04cre_df = pd.read_csv(AT04CRE_PATH, sep='~',
                                      low_memory=False, encoding='latin')
        self.at07_df = pd.read_csv(AT07_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.bbat_df = pd.read_csv(BBAT_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.cd_df = pd.read_csv(
            CD_PATH, sep='~', low_memory=False, encoding='latin')
        self.cnd_df = pd.read_csv(
            CND_PATH, sep='~', low_memory=False, encoding='latin')
        self.fdn_df = pd.read_csv(
            FDN_PATH, sep='~', low_memory=False, encoding='latin')
        self.gicg_df = pd.read_csv(GICG_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.lnp860_df = pd.read_csv(LNP860_PATH, sep='~',
                                     low_memory=False, encoding='latin')
        self.misp_df = pd.read_csv(MISP_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.mm_df = pd.read_csv(
            MM_PATH, sep='~', low_memory=False, encoding='latin')
        self.pprrhh_df = pd.read_csv(PPRRHH_PATH, sep='~',
                                     low_memory=False, encoding='latin')
        self.ricg_df = pd.read_csv(RICG_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.sc_df = pd.read_csv(
            SC_PATH, sep='~', low_memory=False, encoding='latin')
        self.vnp003t_df = pd.read_csv(VNP003T_PATH, sep='~',
                                      low_memory=False, encoding='latin')
        self.siif_df = pd.read_csv(SIIF_PATH, sep='~',
                                   low_memory=False, encoding='latin')
        self.cc_df = pd.read_csv(
            CC_PATH, sep='~', low_memory=False, encoding='latin')
        self.cfgesiifciti_df = pd.read_csv(
            CFGESIIFCITI_PATH, sep='~', low_memory=False, encoding='latin')

        # %%
        # MODIFING ORIGINAL DF

        # CONVERTING CFGE CodigoCiti TO NUMERIC
        self.cfgesiifciti_df['CodigoCiti'] = pd.to_numeric(
            self.cfgesiifciti_df['CodigoCiti'], errors='coerce')

        # RENAMING SIIF COLUMN
        self.siif_df.rename(
            columns={'%Comsion_Flat': 'Porc_Comision_Flat'}, inplace=True)

        # Adding NO_DIRIGIDO to AT04CRE Dataframe

        self.at04cre_df['NO_DIRIGIDO'] = self.at04cre_df.REFERNO.isin(
            self.cnd_df.Referencia).astype(int)

        # Adding type_cd to SIIF DataFrame
        self.siif_df['TypeCD'] = 0

        # CARTERA CREDITOS AL CONSUMO
        filter_df = self.siif_df['TypeId'].isin([593, 594, 190, 196, 610, 611])
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('CCA_CONSUMO')

        # PIL
        filter_df = self.siif_df['TypeId'].isin(
            [10, 11, 12, 13, 14, 15, 18, 35, 36, 224, 640])
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('PIL')

        # CREDICHEQUE
        filter_df = self.siif_df['TypeId'].isin([590, 591, 592, 596, 603, 605])
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('CCH')

        # REWRITES
        filter_df = self.siif_df['TypeId'].isin([70, 90, 91, 92, 93])
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('REWRITES')

        # TDC
        filter_df = ((self.siif_df.TypeId == 999) & (self.siif_df.Micro == 0))
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('TDC')

        # CARROS
        filter_df = ((self.siif_df['TypeId'].isin([25, 27, 52, 56, 57, 597, 20, 21, 22, 23,
                                                   24, 26, 28, 29, 30, 31, 34, 40, 41])) &
                     (self.siif_df['CtaLocal'] == 8190310200) &
                     (self.siif_df['EstadoCredito'] == 3))
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('CARROS')

        # PIL SEGUROS
        filter_df = ((self.siif_df['TypeId'].isin([25, 27, 52, 56, 57, 597, 20, 21, 22, 23,
                                                   24, 26, 28, 29, 30, 31, 34, 40, 41])) &
                     (self.siif_df['CtaLocal'] == 8190310400) &
                     (self.siif_df['EstadoCredito'] == 3))
        self.siif_df.loc[filter_df, 'TypeCD'] = CD_CHOICES.get('SEGUROS')

        # %%
        # MODIFING SOME DATAFRAMES

        # ADDING ADDRESS FIELD TO AT04CRE AND SETTING NEW INDEX
        sep = ' '
        self.at04cre_mod_df = self.at04cre_df.copy()
        self.at04cre_mod_df['ADDRESS'] = self.at04cre_mod_df['ADDRESS3'] + sep + self.at04cre_mod_df['ADDRESS4'] + \
            sep + \
            self.at04cre_mod_df['ADDRESS5'].astype(
                str) + sep + self.at04cre_mod_df['ADDRESS6']
        self.at04cre_mod_df['ADDRESS'] = self.at04cre_mod_df['ADDRESS'].apply(
            lambda x: x.upper().strip())
        self.at04cre_mod_df = self.at04cre_mod_df.set_index('REFERNO')

        # CREATING UNION BETWEEN AT04CRE & CFGE
        self.at04cre_cfgesc_df = self.at04cre_df.set_index('SICVENCLI').join(
            self.cfgesiifciti_df.set_index('CodigoCiti')).set_index('REFERNO')

        # CREATING UNION BETWEEN SIIF & CFGE
        self.cfgesiifciti_filter = (self.cfgesiifciti_df['AtomoSIF'] == 'CTE') & (
            self.cfgesiifciti_df['TablaSIF'] == 'SB10') & (self.cfgesiifciti_df['Insumo'] == 'CORE')
        self.siif_cfgesc_df = self.siif_df.set_index('ActivityId').join(
            self.cfgesiifciti_df[self.cfgesiifciti_filter].set_index('CodigoCiti')).set_index('Acct')

        # CREATING GICG WITH NEW INDEX
        self.gicg_mod_df = self.gicg_df.set_index('NumeroCredito')

        # CREATING CND WITH NEW INDEX
        self.cnd_mod_df = self.cnd_df.set_index('Referencia')

        # CREATING BBAT WITH NEW INDEX
        self.bbat_mod_df = self.bbat_df.set_index('Acct')

        # CREATING SIIF WITH NEW INDEX AND CLEAN ADDRESS FIELD
        self.siif_mod_df = self.siif_df.set_index('Acct')
        self.siif_mod_df['Address'] = self.siif_mod_df['Address'].apply(
            lambda x: str(x).upper().strip())

        # CREATING LNP860 WITH NEW INDEX
        self.lnp860_mod_df = self.lnp860_df.set_index('P8NOTE')

        # CREATING MISP WITH NEW INDEX
        self.misp_mod_df = self.misp_df.set_index('Account')

        # CREATING VNP003T FILTERED WITH NEW INDEX
        self.vnp003t_mod_df = self.vnp003t_df[(self.vnp003t_df['DBKA'] == 51) & (
            self.vnp003t_df['DAPPNA'] == 50)].set_index('DACCTA')

        # CREATING CC WITH NEW INDEX
        self.cc_mod_df = self.cc_df.set_index('IdentificadorCliente')

        # CREATING AH WITH NEW INDEX
        self.ah_mod_df = self.ah_df.loc[(
            self.ah_df['AppId'] == 50)].set_index('Acct')

        # CREATING UNION BETWEEN AT04CRE & CND
        self.at04cre_cnd_df = self.at04cre_df.set_index('REFERNO').join(self.cnd_df.set_index(
            'Referencia'), lsuffix='_at04cre', rsuffix='_cnd').reset_index()

        # CREATING NEW RENDIMIENTOS CORPORATIVOS
        self.ricg_mod_df = self.ricg_df.copy()
        self.ricg_mod_df['Status'] = self.ricg_mod_df['DescripcionDeLaCuenta'].apply(
            lambda x: str(x).upper().strip().split()[-1])
        self.ricg_mod_df = self.ricg_mod_df.set_index('Referencia')

        return True

    # %%
    # HELPFUL METHODS

    def is_nan(self, value, value_if_nan):
        """Checks whether a value is nan and returns the exception if True or the original value if False"""
        return value_if_nan if pd.isnull(value) else value

    def get_plazo_credito(self, plazo_credito):
        """Gets the Plazo Credito Value Cartera Dirigidas ICG"""
        if plazo_credito == 1:
            return 'C'
        elif plazo_credito == 2:
            return 'M'
        elif plazo_credito == 3:
            return 'L'
        else:
            return plazo_credito

    def get_actividad_cliente(self, num_credito, banca, value_if_null, type_dc):
        """Gets the Actividad Cliente value"""
        if banca == 'ICG':
            if type_dc == CD_CHOICES.get('TURISMO'):
                return 'N77'
            elif type_dc == CD_CHOICES.get('HCP'):
                return 'F41'
            else:
                act_cliente = self.at04cre_cfgesc_df.at[int(num_credito), 'CodigoSIF'] if int(
                    num_credito) in self.at04cre_cfgesc_df.index else np.NaN
                return self.is_nan(act_cliente, value_if_null)
        else:
            if type_dc == CD_CHOICES.get('AGRICOLA_OTHER_ICG'):
                return 'A01'
            if type_dc == CD_CHOICES.get('HLP'):
                return 'LG8'
            else:
                act_cliente = self.siif_cfgesc_df.at[
                    num_credito,
                    'CodigoSIF'
                ] if num_credito in self.siif_cfgesc_df.index else np.NaN
                if type_dc == CD_CHOICES.get('MICROFINANCIERO'):
                    value_if_null = 'G45'

                return self.is_nan(act_cliente, value_if_null)
            pass

    def get_domicilio_fiscal(self, num_credito, type_dc, is_in_dom_fis_field):
        """Gets the Domicilio Fiscal Value"""
        if type_dc in [
            CD_CHOICES.get('TURISMO'), CD_CHOICES.get('AGRICOLA_ICG')
        ] or is_in_dom_fis_field:
            return self.at04cre_mod_df.at[
                int(num_credito),
                'ADDRESS'
            ] if int(num_credito) in self.at04cre_mod_df.index else ''
        elif type_dc in [CD_CHOICES.get('MANUFACTURA'), CD_CHOICES.get('HCP')]:
            return ''
        elif type_dc in [
            CD_CHOICES.get('AGRICOLA_OTHER_ICG'),
            CD_CHOICES.get('HLP'),
            CD_CHOICES.get('MICROFINANCIERO')
        ]:
            return self.get_siif_values(num_credito, 'Address')
        else:
            pass

    def get_monto_vencer(self, num_credito, banca, dias):
        """Gets the Monto Vencer value"""
        possible_days = [30, 60, 90, 120, 180, 360, '+360']

        if banca == 'ICG':
            if dias == 30:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N030DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == 60:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N060DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == 90:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N090DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == 120:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N120DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == 180:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N180DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == 360:
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'N360DMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            elif dias == '+360':
                return self.at04cre_mod_df.at[
                    int(num_credito),
                    'MA1AMONTOAVENCER'
                ] if int(num_credito) in self.at04cre_mod_df.index else 0
            else:
                sys.exit(f'The days given ({dias}) are out of bound!')
        else:
            pass

    def get_gicg_cnd_values(self, num_credito, campo):
        """Gets the Gavetas ICG or Carteras No Dirigidas Values"""
        if campo in [
            'InteresesEfectivamenteCobrados',
            'MontoComisionFLAT',
            'PeriodicidadPagoEspecialCapital',
            'CapitalTransferido'
        ]:
            gicg_value = self.gicg_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.gicg_mod_df.index else False
            cnd_value = self.cnd_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.cnd_mod_df.index else False
            return gicg_value or cnd_value or 0.00
        elif campo in [
            'FechaCambioEstatusCredito',
            'FechaRegistroVencidaLitigioCastigada',
            'FechaExigibilidadPagoUltimaCuotaPagada',
            'FechaCambioEstatusCapitalTransferido'
        ]:
            gicg_value = self.gicg_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.gicg_mod_df.index else False
            cnd_value = self.cnd_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.cnd_mod_df.index else False
            return gicg_value or cnd_value or pd.to_datetime('01/01/1900')
        elif campo in [
            'TipoIndustria',
            'TipoBeneficiarioSectorManufacturero',
            'TipoBeneficiarioSectorTurismo',
            'BeneficiarioEspecial',
            'TipoVivienda'
        ]:
            gicg_value = int(self.gicg_mod_df.at[int(num_credito), campo]) if int(
                num_credito) in self.gicg_mod_df.index else False
            return gicg_value or 0
        elif campo in [
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'FechaFinPeriodoGraciaPagoInteres'
        ]:
            gicg_value = self.gicg_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.gicg_mod_df.index else False
            return gicg_value or pd.to_datetime('01/01/1900')
        else:
            sys.exit(f'The field ({campo}) is invalid or not supported!')

    def get_porcentaje_comision_flat(self, num_credito, banca):
        """Gets Porcentaje Comision Flat Value"""
        if banca == 'ICG':
            return self.gicg_mod_df.at[
                int(num_credito),
                'PorcentajeComisionFLAT'
            ] if int(num_credito) in self.gicg_mod_df.index else 0.00
        else:
            pass

    def get_bbat_amounts(self, num_credito, status):
        """Gets BalByAcct Transformada Values"""
        choices = ['vigente', 'vencido', 'mora', 'orden']

        if status == 'vigente':
            self.bbat_mod_df.at[int(num_credito), 'SaldoRendXcobrar'] if int(
                num_credito) in self.bbat_mod_df.index else np.nan
        elif status == 'vencido':
            self.bbat_mod_df.at[int(num_credito), 'SaldoRendXcobrarVenc'] if int(
                num_credito) in self.bbat_mod_df.index else np.nan
        elif status == 'mora':
            self.bbat_mod_df.at[int(num_credito), 'SaldoRendXMora'] if int(
                num_credito) in self.bbat_mod_df.index else np.nan
        elif status == 'orden':
            self.bbat_mod_df.at[int(num_credito), 'SaldoRendCuentaOrden'] if int(
                num_credito) in self.bbat_mod_df.index else np.nan
        else:
            sys.exit(
                f'The status ({status}) is invalid or not supported! Supported values are [{choices}]')

    def get_siif_values(self, num_credito, campo):
        """Gets SIIF Values"""
        if campo == 'Address':
            return self.siif_mod_df.at[
                int(num_credito),
                'Address'
            ] if int(num_credito) in self.siif_mod_df.index else ''
        elif campo in [
            'Int_Efectivamente_Cobrado',
            'Porc_Comision_Flat',
            'Monto_Comision_Flat',
            'Capital_Trasferido',
            'CreditLimit',
            'FeePaid'
        ]:
            siif_value = self.siif_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.siif_mod_df.index else False
            return self.is_nan(siif_value, 0.00) or 0.00
        elif campo in [
            'Periodicidad_Pago_Especial_Capital',
            'Tipo_Vivienda',
            'Staff',
            'TypeId'
        ]:
            siif_value = int(self.siif_mod_df.at[int(num_credito), campo]) if int(
                num_credito) in self.siif_mod_df.index else False
            return self.is_nan(siif_value, 0) or 0.
        elif campo in [
            'Fecha_Cambio_Status',
            'Fecha_Reg_Venc_Lit_cast',
            'Fecha_Exigibilidad_pago_ult_cuota',
            'Fecha_Fin_Periodo_gracia_Pago_interes',
            'Fecha_cambio_Capital_Transferido',
            'OpenDate'
        ]:
            siif_value = self.siif_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.siif_mod_df.index else False
            return self.is_nan(siif_value, pd.to_datetime('01/01/1900')) or pd.to_datetime('01/01/1900')
        else:
            sys.exit(f'The field ({campo}) is invalid or not supported!')

    def get_cod_linea_credito(self, num_credito, estado_credito, type_dc):
        """Gets Codigo Linea Credito Value"""
        if type_dc == CD_CHOICES.get('MICROFINANCIERO'):
            type_id = self.get_siif_values(num_credito, 'TypeId')

            if type_id == 5:
                return 2
            elif (type_id in (16, 17, 999)) or int(estado_credito) == 3:
                return 1
            else:
                return -1
        elif type_dc in [
            CD_CHOICES.get('REWRITES'),
            CD_CHOICES.get('PIL'),
            CD_CHOICES.get('TDC'),
        ]:
            if type_dc in [
                CD_CHOICES.get('REWRITES'),
                CD_CHOICES.get('PIL'),
            ] or int(estado_credito) == 3:
                return 1
            else:
                return 2
        else:
            return 1

    def get_monto_linea_credito(self, num_credito, estado_credito, type_dc, monto_inicial):
        """Gets Monto Linea Credito Value"""
        cod_linea_credito = self.get_cod_linea_credito(
            num_credito, estado_credito, type_dc)

        if cod_linea_credito == 2:
            return self.is_nan(monto_inicial, 0.00)
        elif cod_linea_credito == 1:
            return 0.00
        else:
            return np.NaN

    def get_comisiones_cobrar(self, num_credito, type_dc):
        """Gets Comisiones por Cobrar Value"""
        if type_dc in [CD_CHOICES.get('MICROFINANCIERO'), CD_CHOICES.get('CCH')]:
            type_id = self.get_siif_values(num_credito, 'TypeId')

            if type_id in (16, 17, 610, 611, 999):
                return 0.00
            elif type_id in (190, 196) or type_dc == CD_CHOICES.get('CCH'):
                vnp003t_value = self.vnp003t_mod_df.at[int(num_credito), 'TNBFEE'] if int(
                    num_credito) in self.vnp003t_mod_df.index else False
                return vnp003t_value or 0.00
            else:
                return np.NaN
        else:
            return 0.00

    def get_comisiones_cobradas(
        self,
        num_credito,
        type_dc,
        fecha_liquidacion=DEFAULT_DATE
    ):
        """Gets Comisiones Cobradas Value"""
        if type_dc == CD_CHOICES.get('MICROFINANCIERO'):
            type_id = self.get_siif_values(num_credito, 'TypeId')
            credit_limit = self.get_siif_values(num_credito, 'CreditLimit')
            fee_paid = self.get_siif_values(num_credito, 'FeePaid')

            if type_id in (190, 196, 610, 611):
                return 0.00
            elif type_id in (16, 17):
                return 0.00 if pd.to_datetime(
                    fecha_liquidacion
                ) < self._fecha_reportar else credit_limit * 0.02
            elif type_id == 999:
                return fee_paid
            else:
                return np.NaN
        elif type_dc == CD_CHOICES.get('PIL'):
            type_id = self.get_siif_values(num_credito, 'TypeId')
            open_date = self.get_siif_values(num_credito, 'OpenDate')
            credit_limit = self.get_siif_values(num_credito, 'CreditLimit')

            if pd.to_datetime(open_date) < self._fecha_reportar:
                return 0.00
            elif type_id == 18:
                return credit_limit * 0.02
            else:
                return credit_limit * 0.03
        else:
            return 0.00

    def get_fecha_venc_original(self, division_type, maturity_date, open_date, record_date):
        """Gets Fecha Vencimiento Original Value"""
        if str(division_type).upper() not in ['R', 'E', 'V', 'C']:
            return pd.to_datetime(maturity_date)
        elif str(division_type).upper() == 'E':
            return pd.to_datetime(open_date) + pd.DateOffset(months=36)
        else:
            return pd.to_datetime(record_date) + pd.DateOffset(months=36)

    def get_fecha_venc_actual(
        self,
        fecha_venc_original,
        cant_renovaciones,
        fecha_ult_renovacion,
        type_cd
    ):
        """Gets Fecha Vencimiento Actual Value"""
        if type_cd == CD_CHOICES.get('CCA_CONSUMO'):
            if self.is_nan(cant_renovaciones, 0) == 0:
                return pd.to_datetime(fecha_venc_original)
            else:
                return pd.to_datetime(fecha_ult_renovacion) + pd.DateOffset(months=36)
        else:
            return fecha_venc_original

    def get_cant_renovaciones(self, division_type, open_date, record_date):
        """Gets Cantidad Renovaciones Value"""
        date_diff = np.round(
            np.abs((pd.to_datetime(open_date) - pd.to_datetime(record_date)).days)/30, 0)
        return (date_diff / 36) if str(division_type).upper() == 'E' else 0

    def get_fecha_ult_renovacion(self, division_type, open_date, record_date):
        """Gets Fecha Ultima Renovacion Value"""
        date_diff = np.round(
            np.abs((pd.to_datetime(open_date) - pd.to_datetime(record_date)).days)/30, 0)
        if str(division_type).upper() == 'E' and (date_diff/36) > 0:
            return pd.to_datetime(open_date) + pd.DateOffset(months=(date_diff/36)*36)
        else:
            return DEFAULT_DATE

    def get_lnp860_values(self, num_credito, campo):
        """Gets LNP860 Values"""
        if campo in ['P8FCTC', 'P8FVUC', 'P8FCCC', 'P8FVUI', 'P8FCCI']:
            lnp860_value = self.lnp860_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.lnp860_mod_df.index else False
            return lnp860_value or pd.to_datetime('01/01/1900')
        elif campo in [
            'P8RPCV',
            'P8TINC',
            'P8NRCV',
            'P8MV30',
            'P8MV60',
            'P8MV90',
            'P8MV12',
            'P8MV18',
            'P8MV1A',
            'P8MVM1',
        ]:
            lnp860_value = self.lnp860_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.lnp860_mod_df.index else False
            return self.is_nan(lnp860_value, 0.00) or 0.00
        else:
            sys.exit(f'The field ({campo}) is invalid or not supported!')

    def get_misp_values(self, num_credito, campo):
        """Gets MIS Provisiones Values"""
        if campo in ['Provision', 'Saldo_Provision', 'ProvisionREND', 'Saldo_Provision_REND']:
            misp_value = self.misp_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.misp_mod_df.index else False
            return self.is_nan(misp_value, 0.00) or 0.00
        else:
            sys.exit(f'The field ({campo}) is invalid or not supported!')

    def get_num_cuotas(self, division_type, agro, open_date, maturity_date):
        """Gets Numero Cuotas Value"""
        date_diff = np.round(
            np.abs((pd.to_datetime(open_date) - pd.to_datetime(maturity_date)).days)/30, 0)
        if str(division_type).upper() in ('R', 'E', 'V'):
            return 0
        elif agro == 0:
            return date_diff
        else:
            return np.round(date_diff/6, 0)

    def get_nacionalidad(self, id_cliente):
        """Gets Nacionalidad Value"""
        nationality = self.cc_mod_df.at[id_cliente,
                                        'Nacionalidad'] if id_cliente in self.cc_mod_df.index else False
        return nationality or 'XX'

    def get_ah_values(self, num_credito, campo, type_cd):
        """Gets Account History Values"""
        if type_cd in [CD_CHOICES.get('CARROS'), CD_CHOICES.get('SEGUROS')]:
            if campo in ['CapitalCastigado', ]:
                ah_value = self.ah_mod_df.at[int(num_credito), campo] if int(
                    num_credito) in self.ah_mod_df.index else False
                return self.is_nan(ah_value, 0.00) or 0.00
            else:
                sys.exit(f'The field ({campo}) is invalid or not supported!')

    def get_periosidad_pago(self, estado_credito, type_cd, is_capital):
        """Gets Periosidad Pago Value"""
        if estado_credito in (2, 3):
            return 0
        elif estado_credito == 1:
            return 512 if is_capital and type_cd == CD_CHOICES.get('CCA_CONSUMO') else 8
        else:
            return -1

    def get_monto_liquidado_mes(self, purchases, credit_limit, open_date, type_cd):
        """Gets Monto Liquidado al cierre del Mes Value"""
        if type_cd == CD_CHOICES.get('PIL'):
            return 0.00 if pd.to_datetime(
                open_date
            ) < self._fecha_reportar else self.is_nan(credit_limit, 0.00)
        elif type_cd in [
            CD_CHOICES.get('CCH'),
            CD_CHOICES.get('CCA_CONSUMO'),
            CD_CHOICES.get('TDC'),
        ]:
            return self.is_nan(purchases, 0.00)
        else:
            return 0.00

    def get_num_reg_const_mppat(self, type_cd):
        """Gets Numero Registro Constancia MPPAT Value"""
        if type_cd in [
            CD_CHOICES.get('PIL'),
            CD_CHOICES.get('REWRITES'),
        ]:
            return 2
        elif type_cd in [CD_CHOICES.get('CCH'), ]:
            return 1
        else:
            return 0

    def get_fecha_cancelacion_total(self, num_credito, block_code_date, block_code_id, type_cd):
        """Gets Fecha Cancelacion Total Value"""
        if type_cd in [CD_CHOICES.get('CARROS'), CD_CHOICES.get('SEGUROS'), ]:
            return DEFAULT_DATE
        elif type_cd in [CD_CHOICES.get('TDC'), ]:
            return block_code_date if str(block_code_id) == 'A' else DEFAULT_DATE
        else:
            return self.get_lnp860_values(num_credito, 'P8FCTC')

    def get_fecha_venc_ult_cuota(self, num_credito, orig_open_date, open_date, type_cd, is_capital):
        """Gets Fecha Venc Ultima Cuota Value"""
        if type_cd in [CD_CHOICES.get('CARROS'), CD_CHOICES.get('SEGUROS'), ]:
            return self.is_nan(orig_open_date, open_date)
        elif type_cd in [CD_CHOICES.get('TDC'), ]:
            return DEFAULT_DATE
        else:
            return self.get_lnp860_values(num_credito, 'P8FVUC' if is_capital else 'P8FVUI')

    def get_tipo_credito(self, prod_category):
        """Gets Tipo Credito Value"""
        if prod_category in ['14046', '14060']:  # Agricola
            return 4
        elif prod_category == '14040':  # Comercial
            return 2
        elif prod_category == '14061':  # Construccion
            return 3
        elif prod_category == '14240':  # Manufactura
            return 8
        elif prod_category == '14057':  # Turismo
            return 6
        else:
            return 2

    def get_situacion_credito(self, cta_contable):
        """Gets Situacion Credito Value"""
        if str(cta_contable).startswith('131'):
            return 1
        elif str(cta_contable).startswith('132'):
            return 2
        elif str(cta_contable).startswith('133'):
            return 3
        elif str(cta_contable).startswith('134'):
            return 4
        else:
            return ''

    def get_plazo_credito_cnd(self, plazo_days):
        """Gets Plazo Credito Value for Cartera No Dirigida ICG"""
        if float(plazo)/365 <= 3:
            return 'C'
        elif float(plazo)/365 > 3 and float(plazo)/365 <= 5:
            return 'M'
        elif float(plazo)/365 > 5:
            return 'L'
        else:
            return ''

    def get_periocidad_pago_icg(self, plazo_days, total_cuotas):
        """Gets Periocidad Pago ICG"""
        calc = float(plazo_days)/float(total_cuotas)

        if float(total_cuotas) == 1:
            return 512
        elif 1 < calc < 7:
            return 1
        elif 7 <= calc < 15:
            return 2
        elif 15 <= calc < 30:
            return 4
        elif 30 <= calc < 60:
            return 8
        elif 60 <= calc < 90:
            return 16
        elif 90 <= calc < 120:
            return 32
        elif 120 <= calc < 180:
            return 64
        elif 180 <= calc < 365:
            return 128
        elif calc >= 365:
            return 256
        else:
            return ''

    def get_fecha_canc_cuota_cap(
        self,
        vcto_fecha,
        vcto_ult_princ,
        ctrorg,
        liq_fecha,
        orig_fecha,
        saldo_monto,
        orig_monto
    ):
        """Gets Fecha Cancelacion Cuota Capital Value for Carteras No Dirigidas ICG"""
        if vcto_fecha == 0:
            return vcto_ult_princ
        elif pd.isnull(vcto_fecha):
            return liq_fecha if ctrorg == 0 else orig_fecha
        elif saldo_monto == orig_monto:
            return DEFAULT_DATE
        else:
            return vcto_fecha

    def get_fecha_canc_cuota_int(
        self,
        vcto_fecha,
        vcto_ult_princ,
        ctrorg,
        liq_fecha,
        orig_fecha,
        saldo_monto,
        orig_monto,
        plazo_days,
        total_cuotas
    ):
        """Gets Fecha Cancelacion Cuota Intereses Value for Carteras No Dirigidas ICG"""
        if vcto_fecha == 0:
            return vcto_ult_princ
        elif pd.isnull(vcto_fecha):
            return liq_fecha if ctrorg == 0 else orig_fecha
        elif saldo_monto == orig_monto and not pd.isnull(float(plazo_days)/float(total_cuotas)):
            return DEFAULT_DATE
        else:
            return vcto_fecha

    def get_ricg_values(self, num_credito, campo):
        """Gets Rendimientos Corportavios Values"""
        if campo in ['Saldo', ]:
            ricg_value = self.ricg_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.ricg_mod_df.index else False
            return is_nan(ricg_value, 0.00) or 0.00
        elif campo in ['Status', ]:
            ricg_value = self.ricg_mod_df.at[int(num_credito), campo] if int(
                num_credito) in self.ricg_mod_df.index else False
            return is_nan(ricg_value, '') or ''
        else:
            sys.exit(f'The field ({campo}) is invalid or not supported!')

    # %%
    def create_report(self, user, book_date):
        """Creates the AT04 Report"""

        print(datetime.date.today(), ': Setting Dataframes...')

        data_frames_set = self.set_dataframes()

        if not data_frames_set:
            return {
                'report_path': '',
                'description': 'Cartera de Creditos',
                'last_proocessing_date': None,
                'data': {}
            }

        self._fecha_reportar = pd.to_datetime(book_date)

        # INITIALIZING AT04 DATAFRAME
        self.at04_df = pd.DataFrame(columns=self._labels)

        # %%
        # Filling the base DataFrame with the necessary registries
        # ALL OF CD ICG

        print(datetime.date.today(), ': Adding CD ICG...')

        filter_df = self.cd_df.TYPE_CD.isin([
            CD_CHOICES.get('TURISMO'),
            CD_CHOICES.get('AGRICOLA_ICG'),
            CD_CHOICES.get('MANUFACTURA'),
            CD_CHOICES.get('HCP'),
        ])

        self.at04_df = self.at04_df.append([pd.DataFrame({
            'NumeroCredito': row.NUM_CREDITO,
            'FechaLiquidacion': row.FECHA_LIQUIDACION,
            'FechaSolicitud': row.FECHA_SOLICITUD,
            'FechaAprobacion': row.FECHA_APROBACION,
            'Oficina': 2 if row.COD_OFICINA == 1 else row.COD_OFICINA,
            'CodigoContable': row.COD_CONTABLE,
            'NumeroCreditoPrimerDesembolso': row.NUM_CREDITO_PRIMER_DESEMBOLSO,
            'NumeroDesembolso': row.NUM_DESEMBOLSO,
            'CodigoLineaCredito': 1,
            'MontoLineaCredito': row.MONTO_INICIAL if row.TYPE_CD == CD_CHOICES.get(
                'TURISMO'
            ) else 0.00,
            'EstadoCredito': row.ESTADO_CREDITO,
            'TipoCredito': 0 if row.ESTADO_CREDITO == 3 else row.TIPO_CREDITO,
            'SituacionCredito': row.SITUACION_CREDITO,
            'PlazoCredito': self.get_plazo_credito(row.PLAZO_CREDITO),
            'ClasificacionRiesgo': row.CLASE_RIESGO,
            'DestinoCredito': self.get_actividad_cliente(row.NUM_CREDITO, 'ICG', '', row.TYPE_CD),
            'NaturalezaCliente': row.NATURALEZA_CLIENTE,
            'TipoCliente': row.TIPO_CLIENTE,
            'IdentificacionCliente': str(row.NUM_CLIENTE)[-9:],
            'Nombre_RazonSocial': str(row.NOMBRE_CLIENTE).strip().title().replace('\'\'', '´'),
            'Genero': 3 if row.GENERO not in [0, 1, 2] else row.GENERO,
            'TipoClienteRIF': row.TIPO_CLIENTE,
            'IdentificacionTipoClienteRIF': str(row.NUM_CLIENTE)[-9:],
            'ActividadCliente': self.get_actividad_cliente(row.NUM_CREDITO, 'ICG', 'XXX', row.TYPE_CD),
            'PaisNacionalidad': 'VE' if str(row.TIPO_CLIENTE).upper() in ['V', 'J', 'G'] else 'XX',
            'DomicilioFiscal': self.get_domicilio_fiscal(row.NUM_CREDITO, row.TYPE_CD, True),
            'ClienteNuevo': row.CLIENTE_NUEVO,
            'Cooperativa': row.COOPERATIVA,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': 1,
            'GrupoEconomicoFinanciero': 1,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': self.is_nan(row.COD_PARROQUIA, '010109'),
            'PeriodoGraciaCapital': row.PERIODO_GRACIA_CAPITAL,
            'PeriodicidadPagoCapital': row.PERIODO_PAGO_CAPITAL,
            'PeriodicidadPagoInteresCredito': row.PERIODO_PAGO_INTERES,
            'FechaVencimientoOriginal': row.FECHA_VENC_ORIGINAL,
            'FechaVencimientoActual': row.FECHA_VENC_ACTUAL,
            'FechaReestructuracion': row.FECHA_REESTRUCTURACION,
            'CantidadProrroga': row.CANT_PRORROGAS,
            'FechaProrroga': row.FECHA_PRORROGA,
            'CantidadRenovaciones': row.CANT_RENOVACIONES,
            'FechaUltimaRenovacion': row.FECHA_ULTIMA_RENOVACION,
            'FechaCancelacionTotal': row.FECHA_CANCEL,
            'FechaVencimientoUltimaCoutaCapital': row.FECHA_VENC_ULTIMA_CUOTA_CAPITAL,
            'UltimaFechaCancelacionCuotaCapital': row.ULTIMA_FECHA_CANCEL_CUOTA_CAPITAL,
            'FechaVencimientoUltimaCuotaInteres': row.FECHA_VENC_ULTIMA_CUOTA_INTERES,
            'UltimaFechaCancelacionCuotaIntereses': row.ULTIMA_FECHA_CANCEL_CUOTA_INTERES,
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': row.MONTO_ORIGINAL,
            'MontoInicial': row.MONTO_INICIAL,
            'MontoLiquidadoMes': row.MONTO_LIQUIDADO_MES,
            'EntePublico': 0,
            'MontoInicialTerceros': 0,
            'Saldo': row.SALDO,
            'RendimientosCobrar': row.RENDIMIENTOS_X_COBRAR,
            'RendimientosCobrarVencidos': row.RENDIMIENTOS_X_COBRAR_VENCIDOS,
            'RendimientosCobrarMora': self.get_ricg_values(row.NUM_CREDITO, 'Saldo')
            if self.get_ricg_values(row.NUM_CREDITO, 'Status') == 'MORA' else 0.00,
            'ProvisionEspecifica': row.PROVISION_ESPECIFICA,
            'PorcentajeProvisionEspecifica': row.PORCENTAJE_PROVISION_ESPECIFICA,
            'ProvisionRendimientoCobrar': row.PROVISION_RENDIMIENTO_X_COBRAR,
            'TasasInteresCobrada': row.TASA_INTERES_COBRADA,
            'TasasInteresActual': row.TASA_INTERES_ACTUAL,
            'IndicadorTasaPreferencial': 1,
            'TasaComision': row.TASA_COMISION,
            'ComisionesCobrar': 0.00,
            'ComisionesCobradas': 0,
            'ErogacionesRecuperables': row.EROGACIONES_RECUPERABLES,
            'TipoGarantiaPrincipal': row.TIPO_GARANTIA_PRINCIPAL,
            'NumeroCuotas': row.NUM_CUOTAS,
            'NumeroCuotasVencidas': row.NUM_CUOTAS_VENCIDAS,
            'MontoVencido30dias': self.is_nan(row.MONTO_VENCIDO_30_DIAS, 0.00),
            'MontoVencido60dias': self.is_nan(row.MONTO_VENCIDO_60_DIAS, 0.00),
            'MontoVencido90dias': self.is_nan(row.MONTO_VENCIDO_90_DIAS, 0.00),
            'MontoVencido120dias': self.is_nan(row.MONTO_VENCIDO_120_DIAS, 0.00),
            'MontoVencido180dias': self.is_nan(row.MONTO_VENCIDO_180_DIAS, 0.00),
            'MontoVencidoUnAno': self.is_nan(row.MONTO_VENCIDO_ANUAL, 0.00),
            'MontoVencidoMasUnAno': self.is_nan(row.MONTO_VENCIDO_MAYOR_ANUAL, 0.00),
            'MontoVencer30dias': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 30),
            'MontoVencer60dias': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 60),
            'MontoVencer90dias': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 90),
            'MontoVencer120dias': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 120),
            'MontoVencer180dias': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 180),
            'MontoVencerUnAno': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', 360),
            'MontoVencerMasUnAno': self.get_monto_vencer(row.NUM_CREDITO, 'ICG', '+360'),
            'BancaSocial': row.BANCA_SOCIAL,
            'UnidadProduccionSocial': row.PRODUCCION_SOCIAL,
            'ModalidadMicrocredito': 0,
            'UsoFinanciero': row.USO_FINANCIERO
            if row.TYPE_CD == CD_CHOICES.get('MANUFACTURA') else 0,
            'DestinoRecursosMicrofinancieros': 0,
            'CantidadTrabajadores': row.CANT_TRABAJADORES if row.TYPE_CD == CD_CHOICES.get(
                'MANUFACTURA'
            ) else 0,
            'VentaAnuales': row.VENTAS_ANUALES if row.TYPE_CD == CD_CHOICES.get(
                'MANUFACTURA'
            ) else 0,
            'FechaEstadoFinanciero': row.FECHA_ESTADO_FINANCIERO if row.TYPE_CD == CD_CHOICES.get(
                'MANUFACTURA'
            ) else pd.to_datetime('01/01/1900'),
            'NumeroRTN': row.NUM_RTN if row.TYPE_CD == CD_CHOICES.get('TURISMO') else '',
            'LicenciaTuristicaNacional':
            row.LICENCIA_TURISTICA_NACIONAL if row.TYPE_CD == CD_CHOICES.get(
                'TURISMO') else '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica':
            row.FECHA_EMISION_FACTIBILIDAD_TECNICA if row.TYPE_CD == CD_CHOICES.get(
                'TURISMO'
            ) else pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': str(self.is_nan(
                row.NUM_EXPEDIENTE_FACTIBILIDAD_SOCIOTECNICA, 0
            )).strip() if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'NumeroExpedienteConformidadTuristica': str(self.is_nan(
                row.NUM_EXPEDIENTE_CONFORMIDAD_TURISTICA, 0
            )).strip() if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'NombreProyectoUnidadProduccion': str(
                row.NOMBRE_PROYECTO
            ).strip().upper().replace('\'\'', '´')
            if row.TYPE_CD in [
                CD_CHOICES.get('TURISMO'),
                CD_CHOICES.get('AGRICOLA_ICG')
            ] else '',
            'DireccionProyectoUnidadProduccion': self.get_domicilio_fiscal(
                row.NUM_CREDITO,
                row.TYPE_CD,
                False
            ),
            'CodigoTipoProyecto': row.COD_TIPO_PROYECTO
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'CodigoTipoOperacionesFinanciamiento': row.COD_TIPO_OPERACIONES_FINANCIAMIENTO
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'CodigoSegmento': row.COD_SEGMENTO
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'TipoZona': row.TIPO_ZONA if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'FechaAutenticacionProtocolizacion': row.FECHA_AUTENTICACION
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': row.FECHA_ULTIMA_INSPECCION
            if row.TYPE_CD in [
                CD_CHOICES.get('TURISMO'),
                CD_CHOICES.get('AGRICOLA_ICG')
            ] else pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': row.PORCENTAJE_EJECUCION_PROYECTO
            if row.TYPE_CD in [
                CD_CHOICES.get('TURISMO'),
                CD_CHOICES.get('AGRICOLA_ICG')
            ] else 0,
            'PagosEfectuadosDuranteMes': row.PAGOS_EFECTUADOS_MENSUALES
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'MontosLiquidadosFechaCierre': row.MONTOS_LIQUIDADOS_CIERRE
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0.00,
            'AmortizacionesCapitalAcumuladasFecha': row.AMORTIZACIONES_CAPITAL_ACUMULADAS
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0.00,
            'TasaIncentivo': row.TASA_INCENTIVO
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else 0,
            'NumeroOficioIncentivo': row.NUMERO_OFICIO_INCENTIVO
            if row.TYPE_CD == CD_CHOICES.get('TURISMO') else '',
            'NumeroRegistro_ConstanciaMPPAT': row.NUM_REGISTRO
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'TipoRegistro_ConstanciaMPPAT': row.TIPO_REGISTRO
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': row.FECHA_VENC_REGISTRO
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else pd.to_datetime('01/01/1900'),
            'TipoSubsector': row.TIPO_SUBSECTOR
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'Rubro': row.RUBRO if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'CodigoUso': row.COD_USO if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'CantidadUnidades': row.CANT if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'CodigoUnidadMedida': row.COD_UNIDAD_MEDIDA
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'SectorProduccion': row.SECTOR_PRODUCCION
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'CantidadHectareas': row.CANT_HECTAREAS
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'SuperficieTotalPropiedad': row.SUPERFICIE_TOTAL
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'NumeroProductoresBeneficiarios': row.NUM_BENEFICIARIOS
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'Prioritario': row.PRIORITARIO
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_ICG') else 0,
            'DestinoManufacturero': row.DESTINO_MANUFACTURERO
            if row.TYPE_CD == CD_CHOICES.get('MANUFACTURA') else 0,
            'DestinoEconomico': row.DESTINO_ECONOMICO
            if row.TYPE_CD == CD_CHOICES.get('MANUFACTURA') else 0,
            'TipoBeneficiario': row.TIPO_BENEFICIARIO
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0,
            'ModalidadHipoteca': row.MODALIDAD_HIPOTECARIA
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0,
            'IngresoFamiliar': row.INGRESO_FAMILIAR
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0.00,
            'MontoLiquidadoDuranteAnoCurso': row.MONTO_LIQUIDADO_ANUAL
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0.00,
            'SaldoCredito31_12': row.SALDO_CREDITO_31_12
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0.00,
            'CantidadViviendasConstruir': row.CANT_VIVIENDAS
            if row.TYPE_CD == CD_CHOICES.get('HCP') else 0,
            'RendimientosCobrarReestructurados': self.get_ricg_values(row.NUM_CREDITO, 'Saldo')
            if self.get_ricg_values(row.NUM_CREDITO, 'Status') == 'RESTRUCTURADOS' else 0.00,
            'RendimientosCobrarAfectosReporto': self.get_ricg_values(row.NUM_CREDITO, 'Saldo')
            if self.get_ricg_values(row.NUM_CREDITO, 'Status') == 'EFECTOS' else 0.00,
            'RendimientosCobrarLitigio': self.get_ricg_values(row.NUM_CREDITO, 'Saldo')
            if self.get_ricg_values(row.NUM_CREDITO, 'Status') == 'LITIGIO' else 0.00,
            'InteresEfectivamenteCobrado': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'InteresesEfectivamenteCobrados'
            ),
            'PorcentajeComisionFlat': self.get_porcentaje_comision_flat(
                row.NUM_CREDITO,
                'ICG'
            ),
            'MontoComisionFlat': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'MontoComisionFLAT'
            ),
            'PeriocidadPagoEspecialCapital': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'PeriodicidadPagoEspecialCapital'
            ),
            'FechaCambioEstatusCredito': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaCambioEstatusCredito'
            ),
            'FechaRegistroVencidaLitigiooCastigada': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaRegistroVencidaLitigioCastigada'
            ),
            'FechaExigibilidadPagoUltimaCuotaPagada': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaExigibilidadPagoUltimaCuotaPagada'
            ),
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': 0.00,
            'TipoIndustria': self.get_gicg_cnd_values(row.NUM_CREDITO, 'TipoIndustria'),
            'TipoBeneficiarioSectorManufacturero': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'TipoBeneficiarioSectorManufacturero'
            ),
            'TipoBeneficiarioSectorTurismo': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'TipoBeneficiarioSectorTurismo'
            ),
            'BeneficiarioEspecial': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'BeneficiarioEspecial'
            ),
            'FechaEmisionCertificacionBeneficiarioEspecial': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaEmisionCertificacionBeneficiarioEspecial'
            ),
            'TipoVivienda': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'TipoVivienda'
            ),
            'FechaFinPeriodoGraciaPagoInteres': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaFinPeriodoGraciaPagoInteres'
            ),
            'CapitalTransferido': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'CapitalTransferido'
            ),
            'FechaCambioEstatusCapitalTransferido': self.get_gicg_cnd_values(
                row.NUM_CREDITO,
                'FechaCambioEstatusCapitalTransferido'
            ),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': row.TYPE_CD,
        } for row in self.cd_df.loc[filter_df].itertuples())],
            ignore_index=True,
            sort=True)

        #  ALL OF CD OTHER ICG

        print(datetime.date.today(), ': Adding CD OTHER ICG...')

        filter_df = self.cd_df.TYPE_CD.isin([
            CD_CHOICES.get('AGRICOLA_OTHER_ICG'),
            CD_CHOICES.get('HLP'),
            CD_CHOICES.get('MICROFINANCIERO')
        ])

        self.at04_df = self.at04_df.append([pd.DataFrame({
            'NumeroCredito': row.NUM_CREDITO,
            'FechaLiquidacion': row.FECHA_LIQUIDACION,
            'FechaSolicitud': row.FECHA_SOLICITUD,
            'FechaAprobacion': row.FECHA_APROBACION,
            'Oficina': 2 if row.COD_OFICINA == 1 else row.COD_OFICINA,
            'CodigoContable': row.COD_CONTABLE,
            'NumeroCreditoPrimerDesembolso': row.NUM_CREDITO_PRIMER_DESEMBOLSO,
            'NumeroDesembolso': row.NUM_DESEMBOLSO,
            'CodigoLineaCredito': self.get_cod_linea_credito(
                row.NUM_CREDITO,
                row.ESTADO_CREDITO,
                row.TYPE_CD
            ),
            'MontoLineaCredito': self.get_monto_linea_credito(
                row.NUM_CREDITO,
                row.ESTADO_CREDITO,
                row.TYPE_CD,
                row.MONTO_INICIAL
            ),
            'EstadoCredito': row.ESTADO_CREDITO,
            'TipoCredito': 0 if row.ESTADO_CREDITO == 3 else row.TIPO_CREDITO,
            'SituacionCredito': row.SITUACION_CREDITO,
            'PlazoCredito': self.get_plazo_credito(row.PLAZO_CREDITO),
            'ClasificacionRiesgo': row.CLASE_RIESGO,
            'DestinoCredito': self.get_actividad_cliente(row.NUM_CREDITO, 'GCG', '', row.TYPE_CD),
            'NaturalezaCliente': row.NATURALEZA_CLIENTE,
            'TipoCliente': row.TIPO_CLIENTE,
            'IdentificacionCliente': str(row.NUM_CLIENTE)[-9:],
            'Nombre_RazonSocial': str(row.NOMBRE_CLIENTE).strip().title().replace('\'\'', '´'),
            'Genero': 3 if row.GENERO not in [0, 1, 2] else row.GENERO,
            'TipoClienteRIF': row.TIPO_CLIENTE,
            'IdentificacionTipoClienteRIF': str(row.NUM_CLIENTE)[-9:],
            'ActividadCliente': self.get_actividad_cliente(row.NUM_CREDITO, 'GCG', 'XXX', row.TYPE_CD),
            'PaisNacionalidad': 'VE' if str(row.TIPO_CLIENTE).upper() in ['V', 'J', 'G'] else 'XX',
            'DomicilioFiscal': self.get_domicilio_fiscal(row.NUM_CREDITO, row.TYPE_CD, False),
            'ClienteNuevo': row.CLIENTE_NUEVO,
            'Cooperativa': row.COOPERATIVA,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': self.get_siif_values(
                row.NUM_CREDITO, 'Staff'
            ) if row.TYPE_CD in [CD_CHOICES.get('HLP'), CD_CHOICES.get('MICROFINANCIERO')] else 1,
            'GrupoEconomicoFinanciero': 1,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': self.is_nan(row.COD_PARROQUIA, '010109'),
            'PeriodoGraciaCapital': row.PERIODO_GRACIA_CAPITAL,
            'PeriodicidadPagoCapital': row.PERIODO_PAGO_CAPITAL,
            # TODO: Revisar por que se deja pago capital
            'PeriodicidadPagoInteresCredito': row.PERIODO_PAGO_INTERES,
            'FechaVencimientoOriginal': row.FECHA_VENC_ORIGINAL,
            'FechaVencimientoActual': row.FECHA_VENC_ACTUAL,
            'FechaReestructuracion': row.FECHA_REESTRUCTURACION,
            'CantidadProrroga': row.CANT_PRORROGAS,
            'FechaProrroga': row.FECHA_PRORROGA,
            'CantidadRenovaciones': row.CANT_RENOVACIONES,
            'FechaUltimaRenovacion': row.FECHA_ULTIMA_RENOVACION,
            'FechaCancelacionTotal': row.FECHA_CANCEL,
            'FechaVencimientoUltimaCoutaCapital': row.FECHA_VENC_ULTIMA_CUOTA_CAPITAL,
            'UltimaFechaCancelacionCuotaCapital': row.ULTIMA_FECHA_CANCEL_CUOTA_CAPITAL,
            'FechaVencimientoUltimaCuotaInteres': row.FECHA_VENC_ULTIMA_CUOTA_INTERES,
            'UltimaFechaCancelacionCuotaIntereses': row.ULTIMA_FECHA_CANCEL_CUOTA_INTERES,
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': row.MONTO_ORIGINAL,
            'MontoInicial': row.MONTO_INICIAL,
            'MontoLiquidadoMes': row.MONTO_LIQUIDADO_MES,
            'EntePublico': 0,
            'MontoInicialTerceros': 0,
            'Saldo': row.SALDO,
            'RendimientosCobrar': self.is_nan(self.get_bbat_amounts(
                row.NUM_CREDITO, 'vigente'
            ), row.RENDIMIENTOS_X_COBRAR),
            'RendimientosCobrarVencidos': self.is_nan(self.get_bbat_amounts(
                row.NUM_CREDITO, 'vencido'
            ), row.RENDIMIENTOS_X_COBRAR_VENCIDOS),
            'RendimientosCobrarMora': self.is_nan(self.get_bbat_amounts(
                row.NUM_CREDITO, 'mora'
            ), 0.00),
            'ProvisionEspecifica': row.PROVISION_ESPECIFICA,
            'PorcentajeProvisionEspecifica': row.PORCENTAJE_PROVISION_ESPECIFICA,
            'ProvisionRendimientoCobrar': row.PROVISION_RENDIMIENTO_X_COBRAR,
            'TasasInteresCobrada': row.TASA_INTERES_COBRADA,
            'TasasInteresActual': row.TASA_INTERES_ACTUAL,
            'IndicadorTasaPreferencial': self.get_siif_values(
                row.NUM_CREDITO, 'Staff'
            ) if row.TYPE_CD == CD_CHOICES.get('HLP') else 1,
            'TasaComision': row.TASA_COMISION,
            'ComisionesCobrar': self.get_comisiones_cobrar(row.NUM_CREDITO, row.TYPE_CD),
            'ComisionesCobradas': self.get_comisiones_cobradas(
                row.NUM_CREDITO,
                row.TYPE_CD,
                row.FECHA_LIQUIDACION
            ),
            'ErogacionesRecuperables': row.EROGACIONES_RECUPERABLES,
            'TipoGarantiaPrincipal': row.TIPO_GARANTIA_PRINCIPAL,
            'NumeroCuotas': row.NUM_CUOTAS,
            'NumeroCuotasVencidas': row.NUM_CUOTAS_VENCIDAS,
            'MontoVencido30dias': self.is_nan(row.MONTO_VENCIDO_30_DIAS, 0.00),
            'MontoVencido60dias': self.is_nan(row.MONTO_VENCIDO_60_DIAS, 0.00),
            'MontoVencido90dias': self.is_nan(row.MONTO_VENCIDO_90_DIAS, 0.00),
            'MontoVencido120dias': self.is_nan(row.MONTO_VENCIDO_120_DIAS, 0.00),
            'MontoVencido180dias': self.is_nan(row.MONTO_VENCIDO_180_DIAS, 0.00),
            'MontoVencidoUnAno': self.is_nan(row.MONTO_VENCIDO_ANUAL, 0.00),
            'MontoVencidoMasUnAno': self.is_nan(row.MONTO_VENCIDO_MAYOR_ANUAL, 0.00),
            'MontoVencer30dias': 0,
            'MontoVencer60dias': 0,
            'MontoVencer90dias': 0,
            'MontoVencer120dias': 0,
            'MontoVencer180dias': 0,
            'MontoVencerUnAno': 0,
            'MontoVencerMasUnAno': 0,
            'BancaSocial': row.BANCA_SOCIAL,
            'UnidadProduccionSocial': row.PRODUCCION_SOCIAL,
            'ModalidadMicrocredito': row.MODALIDAD_MICROCREDITO \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else 0,
            'UsoFinanciero': row.USO_FINANCIERO \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else 0,
            'DestinoRecursosMicrofinancieros': row.DESTINO_RECURSOS_MICROFINANCIEROS \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else 0,
            'CantidadTrabajadores': row.CANT_TRABAJADORES \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else 0,
            'VentaAnuales': row.VENTAS_ANUALES \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else 0,
            'FechaEstadoFinanciero': row.FECHA_ESTADO_FINANCIERO \
            if row.TYPE_CD == CD_CHOICES.get('MICROCREDITO') else pd.to_datetime('01/01/1900'),
            'NumeroRTN': '',
            'LicenciaTuristicaNacional': '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica': pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': 0,
            'NumeroExpedienteConformidadTuristica': 0,
            'NombreProyectoUnidadProduccion': str(
                row.NOMBRE_PROYECTO
            ).strip().upper().replace('\'\'', '´') \
            if (row.ESTADO_CREDITO == 1 and row.TYPE_CD == CD_CHOICES.get(
                'AGRICOLA_OTHER_ICG'
            )) else '',
            'DireccionProyectoUnidadProduccion': self.get_domicilio_fiscal(
                row.NUM_CREDITO,
                row.TYPE_CD,
                False
            ) if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else '',
            'CodigoTipoProyecto': 0,
            'CodigoTipoOperacionesFinanciamiento': 0,
            'CodigoSegmento': 0,
            'TipoZona': 0,
            'FechaAutenticacionProtocolizacion': pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': row.FECHA_ULTIMA_INSPECCION \
            if row.TYPE_CD in [
                CD_CHOICES.get('AGRICOLA_OTHER_ICG'),
            ] else pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': 0,
            'PagosEfectuadosDuranteMes': 0,
            'MontosLiquidadosFechaCierre': 0.00,
            'AmortizacionesCapitalAcumuladasFecha': 0.00,
            'TasaIncentivo': 0,
            'NumeroOficioIncentivo': '',
            'NumeroRegistro_ConstanciaMPPAT': row.NUM_REGISTRO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'TipoRegistro_ConstanciaMPPAT': row.TIPO_REGISTRO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': row.FECHA_VENC_REGISTRO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else pd.to_datetime('01/01/1900'),
            'TipoSubsector': row.TIPO_SUBSECTOR \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'Rubro': row.RUBRO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'CodigoUso': row.COD_USO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'CantidadUnidades': row.CANT \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'CodigoUnidadMedida': row.COD_UNIDAD_MEDIDA \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'SectorProduccion': row.SECTOR_PRODUCCION \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'CantidadHectareas': row.CANT_HECTAREAS \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'SuperficieTotalPropiedad': row.SUPERFICIE_TOTAL \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'NumeroProductoresBeneficiarios': row.NUM_BENEFICIARIOS \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'Prioritario': row.PRIORITARIO \
            if row.TYPE_CD == CD_CHOICES.get('AGRICOLA_OTHER_ICG') else 0,
            'DestinoManufacturero': 0,
            'DestinoEconomico': 4 \
            if (row.ESTADO_CREDITO == 1 and row.TYPE_CD == CD_CHOICES.get('MICROFINANCIERO')) else 0,
            'TipoBeneficiario': row.TIPO_BENEFICIARIO \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0,
            'ModalidadHipoteca': row.MODALIDAD_HIPOTECARIA \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0,
            'IngresoFamiliar': row.INGRESO_FAMILIAR \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0.00,
            'MontoLiquidadoDuranteAnoCurso': row.MONTO_LIQUIDADO_ANUAL \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0.00,
            'SaldoCredito31_12': row.SALDO_CREDITO_31_12 \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0.00,
            'CantidadViviendasConstruir': row.CANT_VIVIENDAS \
            if row.TYPE_CD == CD_CHOICES.get('HLP') else 0,
            'RendimientosCobrarReestructurados': self.get_bbat_amounts(
                row.NUM_CREDITO, 'vigente'
            ) if str(row.COD_CONTABLE).startswith('132') else 0.00,
            'RendimientosCobrarAfectosReporto': 0.00,
            'RendimientosCobrarLitigio': 0.00,
            'InteresEfectivamenteCobrado': self.get_siif_values(
                row.NUM_CREDITO,
                'Int_Efectivamente_Cobrado'
            ),
            'PorcentajeComisionFlat': self.get_siif_values(
                row.NUM_CREDITO,
                'Porc_Comision_Flat'
            ),
            'MontoComisionFlat': self.get_siif_values(
                row.NUM_CREDITO,
                'Monto_Comision_Flat'
            ),
            'PeriocidadPagoEspecialCapital': self.get_siif_values(
                row.NUM_CREDITO,
                'Periodicidad_Pago_Especial_Capital'
            ),
            'FechaCambioEstatusCredito': self.get_siif_values(row.NUM_CREDITO, 'Fecha_Cambio_Status'),
            'FechaRegistroVencidaLitigiooCastigada': self.get_siif_values(
                row.NUM_CREDITO,
                'Fecha_Reg_Venc_Lit_cast'
            ),
            'FechaExigibilidadPagoUltimaCuotaPagada': self.get_siif_values(
                row.NUM_CREDITO,
                'Fecha_Exigibilidad_pago_ult_cuota'
            ),
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': self.is_nan(self.get_bbat_amounts(row.NUM_CREDITO, 'orden'), 0.00),
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('01/01/1900'),
            'TipoVivienda': self.get_siif_values(row.NUM_CREDITO, 'Tipo_Vivienda'),
            'FechaFinPeriodoGraciaPagoInteres': self.get_siif_values(
                row.NUM_CREDITO,
                'Fecha_Fin_Periodo_gracia_Pago_interes'
            ),
            'CapitalTransferido': self.get_siif_values(row.NUM_CREDITO, 'Capital_Trasferido'),
            'FechaCambioEstatusCapitalTransferido': self.get_siif_values(
                row.NUM_CREDITO,
                'Fecha_cambio_Capital_Transferido'
            ),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': row.TYPE_CD,
        } for row in self.cd_df.loc[filter_df].itertuples())],
            ignore_index=True,
            sort=True)

        #  CARTERA NO DIRIGIDA CONSUMO (SIIF)

        print(datetime.date.today(),
              ': Adding CARTERA NO DIRIGIDA CONSUMO (SIIF)...')

        filter_df = self.siif_df.TypeCD.isin([
            CD_CHOICES.get('CCA_CONSUMO'),
            CD_CHOICES.get('PIL'),
            CD_CHOICES.get('CCH'),
            CD_CHOICES.get('REWRITES'),
            CD_CHOICES.get('TDC'),
            CD_CHOICES.get('CARROS'),
            CD_CHOICES.get('SEGUROS'),
        ])

        self.at04_df = self.at04_df.append([pd.DataFrame({
            'NumeroCredito': row.Acct,
            'FechaLiquidacion': row.OpenDate,
            'FechaSolicitud': pd.to_datetime(row.OpenDate) - pd.to_timedelta(1, unit='d')
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else row.OpenDate,
            'FechaAprobacion': row.OpenDate,
            'Oficina': 2 if int(self.is_nan(row.BranchId, 2)) == 1 else int(self.is_nan(row.BranchId, 2)),
            'CodigoContable': row.CtaLocal,
            'NumeroCreditoPrimerDesembolso': 0 if row.TypeCD in [
                CD_CHOICES.get('CCA_CONSUMO'),
                CD_CHOICES.get('CCH'),
                CD_CHOICES.get('TDC'),
            ] else row.Acct,
            'NumeroDesembolso': 0 if row.TypeCD in [
                CD_CHOICES.get('CCA_CONSUMO'),
                CD_CHOICES.get('CCH'),
                CD_CHOICES.get('TDC'),
            ] else 1,
            'CodigoLineaCredito': self.get_cod_linea_credito(row.Acct, row.EstadoCredito, row.TypeCD),
            'MontoLineaCredito': self.get_monto_linea_credito(
                row.Acct,
                row.EstadoCredito,
                row.TypeCD,
                row.CreditLimit
            ),
            'EstadoCredito': row.EstadoCredito,
            'TipoCredito': 0 if row.EstadoCredito == 3 else 1,
            'SituacionCredito': row.Situacion_Credito
            if row.EstadoCredito == 1 or row.TypeCD in [CD_CHOICES.get('TDC'), ] else 0,
            'PlazoCredito': 'C'
            if row.EstadoCredito == 1 or row.TypeCD in [CD_CHOICES.get('TDC'), ] else 0,
            'ClasificacionRiesgo': row.ClaseRiesgo if row.EstadoCredito == 1 else 0,
            'DestinoCredito': 0 if row.TypeCD in [
                CD_CHOICES.get('TDC'),
            ] else self.get_actividad_cliente(row.Acct, 'GCG', 'G45', row.TypeCD),
            'NaturalezaCliente': 1 if str(row.Cid).strip()[0].upper() in ['V', 'E', 'P'] else 2,
            'TipoCliente': str(row.Cid).strip()[0].upper(),
            'IdentificacionCliente': str(row.Cid).strip()[1:],
            'Nombre_RazonSocial': str(row.FullName).strip().title().replace('\'\'', '´'),
            'Genero': 3 if row.Gender not in [0, 1, 2] else 0
            if str(row.Cid).strip()[0].upper() not in ['V', 'E', 'P'] else row.Gender,
            'TipoClienteRIF': str(row.Cid).strip()[0],
            'IdentificacionTipoClienteRIF': str(row.Cid).strip()[1:],
            'ActividadCliente': self.get_actividad_cliente(row.Acct, 'GCG', 'G45', row.TypeCD),
            'PaisNacionalidad': 'VE' if str(row.Cid).strip()[0].upper() in [
                'V',
                'J',
                'G'
            ] else self.get_nacionalidad(str(row.Cid).strip().upper()),
            'DomicilioFiscal': str(row.Address).strip().upper().replace('  ', ''),
            'ClienteNuevo': 1
            if pd.to_datetime(row.OpenDate) < self._fecha_reportar or
            row.TypeCD in [CD_CHOICES.get('REWRITES'),
                           CD_CHOICES.get('TDC'),
                           CD_CHOICES.get('CARROS'),
                           CD_CHOICES.get('SEGUROS'), ] else 2,
            'Cooperativa': 1,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': 1 if row.TypeCD in [CD_CHOICES.get('REWRITES'), ] else row.Staff,
            'GrupoEconomicoFinanciero': 1,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': '010109',
            'PeriodoGraciaCapital': 7 if row.TypeCD in [CD_CHOICES.get('TDC'), ] else 0,
            'PeriodicidadPagoCapital': self.get_periosidad_pago(row.EstadoCredito, row.TypeCD, True),
            'PeriodicidadPagoInteresCredito': self.get_periosidad_pago(row.EstadoCredito, row.TypeCD, False),
            'FechaVencimientoOriginal': self.get_fecha_venc_original(
                row.DivisionTypeId,
                row.MaturityDate,
                row.OpenDate,
                row.RecordDate
            ),
            'FechaVencimientoActual': self.get_fecha_venc_actual(
                self.get_fecha_venc_original(
                    row.DivisionTypeId,
                    row.MaturityDate,
                    row.OpenDate,
                    row.RecordDate
                ),
                self.get_cant_renovaciones(
                    row.DivisionTypeId, row.OpenDate, row.RecordDate
                ),
                self.get_fecha_ult_renovacion(
                    row.DivisionTypeId, row.OpenDate, row.RecordDate
                ),
                row.TypeCD
            ),
            'FechaReestructuracion': DEFAULT_DATE,
            'CantidadProrroga': 0,
            'FechaProrroga': DEFAULT_DATE,
            'CantidadRenovaciones': self.get_cant_renovaciones(
                row.DivisionTypeId,
                row.OpenDate,
                row.RecordDate
            ),
            'FechaUltimaRenovacion': self.get_fecha_ult_renovacion(
                row.DivisionTypeId,
                row.OpenDate,
                row.RecordDate
            ),
            'FechaCancelacionTotal': self.get_fecha_cancelacion_total(
                row.Acct,
                row.BlockCode1Date,
                row.BlockCodeId1,
                row.TypeCD
            ),
            'FechaVencimientoUltimaCoutaCapital': self.get_fecha_venc_ult_cuota(
                row.Acct,
                row.OrigOpenDate,
                row.OpenDate,
                row.TypeCD,
                True
            ),
            'UltimaFechaCancelacionCuotaCapital': DEFAULT_DATE
            if row.TypeCD in [
                CD_CHOICES.get('TDC'),
                CD_CHOICES.get('CARROS'),
                CD_CHOICES.get('SEGUROS'),
            ] else self.get_lnp860_values(row.Acct, 'P8FCCC'),
            'FechaVencimientoUltimaCuotaInteres': self.get_fecha_venc_ult_cuota(
                row.Acct,
                row.OrigOpenDate,
                row.OpenDate,
                row.TypeCD,
                False
            ),
            'UltimaFechaCancelacionCuotaIntereses': DEFAULT_DATE
            if row.TypeCD in [
                CD_CHOICES.get('TDC'),
                CD_CHOICES.get('CARROS'),
                CD_CHOICES.get('SEGUROS'),
            ] else self.get_lnp860_values(row.Acct, 'P8FCCI'),
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': self.get_ah_values(
                row.Acct,
                'CapitalCastigado',
                row.TypeCD
            ) if row.TypeCD in [
                CD_CHOICES.get('CARROS'),
                CD_CHOICES.get('SEGUROS'),
            ] else self.is_nan(row.CreditLimit, 0.00),
            'MontoInicial': self.get_ah_values(
                row.Acct,
                'CapitalCastigado',
                row.TypeCD
            ) if row.TypeCD in [
                CD_CHOICES.get('CARROS'),
                CD_CHOICES.get('SEGUROS'),
            ] else self.is_nan(row.CreditLimit, 0.00),
            'MontoLiquidadoMes': self.get_monto_liquidado_mes(
                row.Purchases,
                row.CreditLimit,
                row.OpenDate,
                row.TypeCD
            ),
            'EntePublico': 0,
            'MontoInicialTerceros': 0,
            'Saldo': self.is_nan(row.SaldoCapital, 0.00)
            if row.EstadoCredito == 1 else self.is_nan(row.SaldoCastigado, 0.00)
            if row.EstadoCredito == 3 else 0.00,
            'RendimientosCobrar': self.is_nan(self.get_bbat_amounts(row.Acct, 'vigente'), row.SaldoRendimientos),
            'RendimientosCobrarVencidos': self.is_nan(
                self.get_bbat_amounts(row.Acct, 'vencido'),
                self.get_lnp860_values(row.Acct, 'P8RPCV')
            ),
            'RendimientosCobrarMora': self.is_nan(self.get_bbat_amounts(row.Acct, 'mora'), 0.00),
            'ProvisionEspecifica': self.is_nan(row.SaldoProvision, self.get_misp_values(row.Acct, 'Saldo_Provision')),
            'PorcentajeProvisionEspecifica': self.is_nan(row.Provision, self.get_misp_values(row.Acct, 'Provision')),
            'ProvisionRendimientoCobrar': self.get_misp_values(row.Acct, 'Saldo_Provision_REND'),
            'TasasInteresCobrada': row.Rate
            if row.TypeCD in [
                CD_CHOICES.get('TDC'),
            ] else 0 if row.TypeCD in [
                CD_CHOICES.get('CARROS'),
                CD_CHOICES.get('SEGUROS'),
            ] else self.get_lnp860_values(row.Acct, 'P8TINC'),
            'TasasInteresActual': row.Rate
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.is_nan(row.Rate, 0) * 100,
            'IndicadorTasaPreferencial': 1,
            'TasaComision': 0 if row.TypeCD not in [
                CD_CHOICES.get('PIL'),
            ] else 2 if row.TypeId == 18 else 3,
            'ComisionesCobrar': self.get_comisiones_cobrar(row.Acct, row.TypeCD)
            if row.TypeCD in [CD_CHOICES.get('CCH'), ] else 0,
            'ComisionesCobradas': self.is_nan(row.FeePaid, 0.00)
            if row.TypeCD in [CD_CHOICES.get('CCH'), CD_CHOICES.get('TDC'), ] else 0,
            'ErogacionesRecuperables': 0,
            'TipoGarantiaPrincipal': 12 if row.TypeCD in [CD_CHOICES.get('CCA_CONSUMO'), ] else 10,
            'NumeroCuotas': 36 if row.TypeCD in [
                CD_CHOICES.get('TDC'),
            ] else self.get_num_cuotas(row.DivisionTypeId, row.Agro, row.OpenDate, row.MaturityDate),
            'NumeroCuotasVencidas': row.NumPmtsPastDue
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8NRCV'),
            'MontoVencido30dias': row.Amt30DPD
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8MV30'),
            'MontoVencido60dias': row.Amt60DPD
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8MV60'),
            'MontoVencido90dias': row.Amt90DPD
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8MV90'),
            'MontoVencido120dias': row.Amt120DPD
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8MV12'),
            'MontoVencido180dias': row.Amt180DPD
            if row.TypeCD in [CD_CHOICES.get('TDC'), ] else self.get_lnp860_values(row.Acct, 'P8MV18'),
            'MontoVencidoUnAno': self.get_lnp860_values(row.Acct, 'P8MV1A'),
            'MontoVencidoMasUnAno': self.get_lnp860_values(row.Acct, 'P8MVM1'),
            'MontoVencer30dias': 0.00,
            'MontoVencer60dias': 0.00,
            'MontoVencer90dias': 0.00,
            'MontoVencer120dias': 0.00,
            'MontoVencer180dias': 0.00,
            'MontoVencerUnAno': 0.00,
            'MontoVencerMasUnAno': 0.00,
            'BancaSocial': 1,
            'UnidadProduccionSocial': 0 if row.TypeCD in [CD_CHOICES.get('CCA_CONSUMO'), ] else 1,
            'ModalidadMicrocredito': 0,
            'UsoFinanciero': 0,
            'DestinoRecursosMicrofinancieros': 0,
            'CantidadTrabajadores': 0,
            'VentaAnuales': 0,
            'FechaEstadoFinanciero': pd.to_datetime('01/01/1900'),
            'NumeroRTN': '',
            'LicenciaTuristicaNacional': '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica': pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': 0,
            'NumeroExpedienteConformidadTuristica': 0,
            'NombreProyectoUnidadProduccion': '',
            'DireccionProyectoUnidadProduccion': '',
            'CodigoTipoProyecto': 0,
            'CodigoTipoOperacionesFinanciamiento': 0,
            'CodigoSegmento': 0,
            'TipoZona': 0,
            'FechaAutenticacionProtocolizacion': pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': 0,
            'PagosEfectuadosDuranteMes': 0,
            'MontosLiquidadosFechaCierre': 0.00,
            'AmortizacionesCapitalAcumuladasFecha': 0.00,
            'TasaIncentivo': 0,
            'NumeroOficioIncentivo': '',
            'NumeroRegistro_ConstanciaMPPAT': self.get_num_reg_const_mppat(row.TypeCD),
            'TipoRegistro_ConstanciaMPPAT': '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': pd.to_datetime('01/01/1900'),
            'TipoSubsector': 0,
            'Rubro': 0,
            'CodigoUso': 0,
            'CantidadUnidades': 0,
            'CodigoUnidadMedida': 0,
            'SectorProduccion': 0,
            'CantidadHectareas': 0,
            'SuperficieTotalPropiedad': 0,
            'NumeroProductoresBeneficiarios': 0,
            'Prioritario': 0,
            'DestinoManufacturero': 0,
            'DestinoEconomico': 0,
            'TipoBeneficiario': 0,
            'ModalidadHipoteca': 0,
            'IngresoFamiliar': 0.00,
            'MontoLiquidadoDuranteAnoCurso': 0.00,
            'SaldoCredito31_12': 0.00,
            'CantidadViviendasConstruir': 0,
            'RendimientosCobrarReestructurados': self.get_bbat_amounts(row.Acct, 'vigente')
            if str(row.CtaLocal).startswith('132') else 0.00,
            'RendimientosCobrarAfectosReporto': 0.00,
            'RendimientosCobrarLitigio': 0.00,
            'InteresEfectivamenteCobrado': self.is_nan(row.Int_Efectivamente_Cobrado, 0.00),
            'PorcentajeComisionFlat': self.is_nan(row.Porc_Comision_Flat, 0.00),
            'MontoComisionFlat': self.is_nan(row.Monto_Comision_Flat, 0.00),
            'PeriocidadPagoEspecialCapital': self.is_nan(row.Periodicidad_Pago_Especial_Capital, 0),
            'FechaCambioEstatusCredito': self.is_nan(row.Fecha_Cambio_Status, pd.to_datetime('01/01/1900')),
            'FechaRegistroVencidaLitigiooCastigada': self.is_nan(
                row.Fecha_Reg_Venc_Lit_cast,
                pd.to_datetime('01/01/1900')
            ),
            'FechaExigibilidadPagoUltimaCuotaPagada': self.is_nan(
                row.Fecha_Exigibilidad_pago_ult_cuota,
                pd.to_datetime('01/01/1900')
            ),
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': self.is_nan(self.get_bbat_amounts(row.Acct, 'orden'), 0.00),
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('01/01/1900'),
            'TipoVivienda': self.is_nan(row.Tipo_Vivienda, 0),
            'FechaFinPeriodoGraciaPagoInteres': self.is_nan(
                row.Fecha_Fin_Periodo_gracia_Pago_interes,
                pd.to_datetime('01/01/1900')
            ),
            'CapitalTransferido': self.is_nan(row.Capital_Trasferido, 0.00),
            'FechaCambioEstatusCapitalTransferido': self.is_nan(
                row.Fecha_cambio_Capital_Transferido,
                pd.to_datetime('01/01/1900')
            ),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': row.TypeCD,
        } for row in self.siif_df.loc[filter_df].itertuples())], ignore_index=True, sort=True)

        #  RRHH

        print(datetime.date.today(), ': Adding RRHH...')

        self.at04_df = self.at04_df.append([pd.DataFrame({
            'NumeroCredito': row.GEID,
            'FechaLiquidacion': row.FechaOtorgamiento,
            'FechaSolicitud': row.FechaOtorgamiento,
            'FechaAprobacion': row.FechaOtorgamiento,
            'Oficina': 2,
            'CodigoContable': 1311510000,
            'NumeroCreditoPrimerDesembolso': row.GEID,
            'NumeroDesembolso': 1,
            'CodigoLineaCredito': 1,
            'MontoLineaCredito': 0.00,
            'EstadoCredito': 1,
            'TipoCredito': 2,
            'SituacionCredito': 1,
            'PlazoCredito': 'C',
            'ClasificacionRiesgo': 'A',
            'DestinoCredito': 'K64',
            'NaturalezaCliente': 1,
            'TipoCliente': row.TipoCliente,
            'IdentificacionCliente': row.IdentificacionCliente,
            'Nombre_RazonSocial': str(row.NombreCliente).strip().title(),
            'Genero': 2,
            'TipoClienteRIF': row.TipoCliente,
            'IdentificacionTipoClienteRIF': row.IdentificacionCliente,
            'ActividadCliente': 'K64',
            'PaisNacionalidad': 'VE',
            'DomicilioFiscal': 'Av. Casanova Centro Comercial el Recreo Torre Norte Citibank'.upper(),
            'ClienteNuevo': 1,
            'Cooperativa': 1,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': 2,
            'GrupoEconomicoFinanciero': 1,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': '010109',
            'PeriodoGraciaCapital': 0,
            'PeriodicidadPagoCapital': 8,
            'PeriodicidadPagoInteresCredito': 8,
            'FechaVencimientoOriginal': pd.to_datetime(row.FechaOtorgamiento) + pd.DateOffset(months=12),
            'FechaVencimientoActual': pd.to_datetime(row.FechaOtorgamiento) + pd.DateOffset(months=12),
            'FechaReestructuracion': DEFAULT_DATE,
            'CantidadProrroga': 0,
            'FechaProrroga': DEFAULT_DATE,
            'CantidadRenovaciones': 0,
            'FechaUltimaRenovacion': DEFAULT_DATE,
            'FechaCancelacionTotal': DEFAULT_DATE,
            'FechaVencimientoUltimaCoutaCapital': self._fecha_reportar,
            'UltimaFechaCancelacionCuotaCapital': self._fecha_reportar,
            'FechaVencimientoUltimaCuotaInteres': self._fecha_reportar,
            'UltimaFechaCancelacionCuotaIntereses': self._fecha_reportar,
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': row.MontoOriginal,
            'MontoInicial': row.MontoOriginal,
            'MontoLiquidadoMes': 0.00,
            'EntePublico': 0,
            'MontoInicialTerceros': 0.00,
            'Saldo': row.SaldoActual,
            'RendimientosCobrar': 0.00,
            'RendimientosCobrarVencidos': 0.00,
            'RendimientosCobrarMora': 0.00,
            'ProvisionEspecifica': 0.00,
            'PorcentajeProvisionEspecifica': 0.00,
            'ProvisionRendimientoCobrar': 0.00,
            'TasasInteresCobrada': 17,
            'TasasInteresActual': 17,
            'IndicadorTasaPreferencial': 1,
            'TasaComision': 3,
            'ComisionesCobrar': 0,
            'ComisionesCobradas': 0,
            'ErogacionesRecuperables': 0,
            'TipoGarantiaPrincipal': 10,
            'NumeroCuotas': 12,
            'NumeroCuotasVencidas': 0,
            'MontoVencido30dias': 0.00,
            'MontoVencido60dias': 0.00,
            'MontoVencido90dias': 0.00,
            'MontoVencido120dias': 0.00,
            'MontoVencido180dias': 0.00,
            'MontoVencidoUnAno': 0.00,
            'MontoVencidoMasUnAno': 0.00,
            'MontoVencer30dias': 0.00,
            'MontoVencer60dias': 0.00,
            'MontoVencer90dias': 0.00,
            'MontoVencer120dias': 0.00,
            'MontoVencer180dias': 0.00,
            'MontoVencerUnAno': 0.00,
            'MontoVencerMasUnAno': 0.00,
            'BancaSocial': 1,
            'UnidadProduccionSocial': 1,
            'ModalidadMicrocredito': 0,
            'UsoFinanciero': 0,
            'DestinoRecursosMicrofinancieros': 0,
            'CantidadTrabajadores': 0,
            'VentaAnuales': 0,
            'FechaEstadoFinanciero': pd.to_datetime('01/01/1900'),
            'NumeroRTN': '',
            'LicenciaTuristicaNacional': '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica': pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': 0,
            'NumeroExpedienteConformidadTuristica': 0,
            'NombreProyectoUnidadProduccion': '',
            'DireccionProyectoUnidadProduccion': '',
            'CodigoTipoProyecto': 0,
            'CodigoTipoOperacionesFinanciamiento': 0,
            'CodigoSegmento': 0,
            'TipoZona': 0,
            'FechaAutenticacionProtocolizacion': pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': 0,
            'PagosEfectuadosDuranteMes': 0,
            'MontosLiquidadosFechaCierre': 0.00,
            'AmortizacionesCapitalAcumuladasFecha': 0.00,
            'TasaIncentivo': 0,
            'NumeroOficioIncentivo': '',
            'NumeroRegistro_ConstanciaMPPAT': 0,
            'TipoRegistro_ConstanciaMPPAT': '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': pd.to_datetime('01/01/1900'),
            'TipoSubsector': 0,
            'Rubro': 0,
            'CodigoUso': 0,
            'CantidadUnidades': 0,
            'CodigoUnidadMedida': 0,
            'SectorProduccion': 0,
            'CantidadHectareas': 0,
            'SuperficieTotalPropiedad': 0,
            'NumeroProductoresBeneficiarios': 0,
            'Prioritario': 0,
            'DestinoManufacturero': 0,
            'DestinoEconomico': 0,
            'TipoBeneficiario': 0,
            'ModalidadHipoteca': 0,
            'IngresoFamiliar': 0.00,
            'MontoLiquidadoDuranteAnoCurso': 0.00,
            'SaldoCredito31_12': 0.00,
            'CantidadViviendasConstruir': 0,
            'RendimientosCobrarReestructurados': 0.00,
            'RendimientosCobrarAfectosReporto': 0.00,
            'RendimientosCobrarLitigio': 0.00,
            'InteresEfectivamenteCobrado': 0.00,
            'PorcentajeComisionFlat': 0.00,
            'MontoComisionFlat': 0.00,
            'PeriocidadPagoEspecialCapital': 0,
            'FechaCambioEstatusCredito': pd.to_datetime('01/01/1900'),
            'FechaRegistroVencidaLitigiooCastigada': pd.to_datetime('01/01/1900'),
            'FechaExigibilidadPagoUltimaCuotaPagada': pd.to_datetime('01/01/1900'),
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': 0.00,
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('01/01/1900'),
            'TipoVivienda': 0,
            'FechaFinPeriodoGraciaPagoInteres': pd.to_datetime('01/01/1900'),
            'CapitalTransferido': 0.00,
            'FechaCambioEstatusCapitalTransferido': pd.to_datetime('01/01/1900'),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': CD_CHOICES.get('RRHH'),
        } for row in self.pprrhh_df.itertuples())], ignore_index=True, sort=True)

        #  Corporativa No Dirigida

        print(datetime.date.today(), ': Adding Corporativa No Dirigida...')

        filter_df = self.at04cre_df.NO_DIRIGIDO == 1

        self.at04_df = self.at04_df.append(pd.DataFrame([{
            'NumeroCredito': row.REFERNO,
            'FechaLiquidacion': row.ORIGFECHA if row.CTRORG != 0 else row.LIQUFECHA,
            'FechaSolicitud': row.ORIGFECHA if row.CTRORG != 0 else row.SOLIFECHA,
            'FechaAprobacion': row.ORIGFECHA if row.CTRORG != 0 else row.LIQUFECHA,
            'Oficina': 2,
            'CodigoContable': row.GENLEDGER,
            'NumeroCreditoPrimerDesembolso': row.CTRORG if row.CTRORG != 0 else row.REFERNO,
            'NumeroDesembolso': 1,
            'CodigoLineaCredito': 1,
            'MontoLineaCredito': 0.00,
            'EstadoCredito': 1,
            'TipoCredito': self.get_tipo_credito(row.PRODCAT),
            'SituacionCredito': self.get_situacion_credito(row.GENLEDGER),
            'PlazoCredito': self.get_plazo_credito_cnd(row.PLAZO),
            'ClasificacionRiesgo': row.ClasificacionRiesgo,
            'DestinoCredito': 'XXX',
            'NaturalezaCliente': 2,
            'TipoCliente': str(row.RIFCLI).strip()[0].upper(),
            'IdentificacionCliente': str(row.RIFCLI).strip()[1:],
            'Nombre_RazonSocial': str(row.NOMECLI).strip().title().replace('\'\'', '´'),
            'Genero': 0,
            'TipoClienteRIF': str(row.RIFCLI).strip()[0],
            'IdentificacionTipoClienteRIF': str(row.RIFCLI).strip()[1:],
            'ActividadCliente': row.ActividadCliente,
            'PaisNacionalidad': 'VE',
            'DomicilioFiscal': self.get_domicilio_fiscal(
                row.REFERNO,
                CD_CHOICES.get('ICG_NO_DIRIGIDA'),
                False
            ),
            'ClienteNuevo': 1,
            'Cooperativa': 1,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': 1,
            'GrupoEconomicoFinanciero': 2,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': '010109',
            'PeriodoGraciaCapital': 0,
            'PeriodicidadPagoCapital': self.get_periocidad_pago_icg(row.PLAZO, row.TOTALCUOTAS),
            'PeriodicidadPagoInteresCredito': self.get_periocidad_pago_icg(row.PLAZO, row.TOTALCUOTAS),
            'FechaVencimientoOriginal': row.LIQUFECHA if row.QTDREN != 0 else row.VCTOFECHA,
            'FechaVencimientoActual': row.VCTOFECHA,
            'FechaReestructuracion': row.LIQUFECHA
            if str(row.GENLEDGER).startswith('132') else DEFAULT_DATE,
            'CantidadProrroga': row.QTDREN,
            'FechaProrroga': DEFAULT_DATE
            if int(row.QTDREN) == 0 else pd.to_datetime(row.LIQUFECHA) + pd.DateOffset(days=1),
            'CantidadRenovaciones': row.QTDREN,
            'FechaUltimaRenovacion': row.LIQUFECHA if row.QTDREN > 0 else row.VCTOFECHA,
            'FechaCancelacionTotal': DEFAULT_DATE,
            'FechaVencimientoUltimaCoutaCapital': row.VCTOFECHA,
            'UltimaFechaCancelacionCuotaCapital': self.get_fecha_canc_cuota_cap(
                row.VCTOFECHA,
                row.VCTOULTPRINC,
                row.CTRORG,
                row.LIQUFECHA,
                row.ORIGFECHA,
                row.SALDOMONTO,
                row.ORIGIMONTO
            ),
            'FechaVencimientoUltimaCuotaInteres': row.VCTOFECHA,
            'UltimaFechaCancelacionCuotaIntereses': self.get_fecha_canc_cuota_int(
                row.VCTOFECHA,
                row.VCTOULTPRINC,
                row.CTRORG,
                row.LIQUFECHA,
                row.ORIGFECHA,
                row.SALDOMONTO,
                row.ORIGIMONTO,
                row.PLAZO,
                row.TOTALCUOTAS
            ),
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': row.ORIGIMONTO,
            'MontoInicial': row.ORIGIMONTO,
            'MontoLiquidadoMes': row.ORIGIMONTO,
            'EntePublico': 0,
            'MontoInicialTerceros': 0,
            'Saldo': row.SALDOMONTO,
            'RendimientosCobrar': 0,
            'RendimientosCobrarVencidos': 0,
            'RendimientosCobrarMora': 0,
            'ProvisionEspecifica': row.SaldoProvision,
            'PorcentajeProvisionEspecifica': row.Provision,
            'ProvisionRendimientoCobrar': 0,
            'TasasInteresCobrada': row.INTORIGTASA,
            'TasasInteresActual': row.INTORIGTASA,
            'IndicadorTasaPreferencial': 1,
            'TasaComision': 0,
            'ComisionesCobrar': 0,
            'ComisionesCobradas': 0,
            'ErogacionesRecuperables': 0,
            'TipoGarantiaPrincipal': row.TipoGarantiaPrincipal,
            'NumeroCuotas': row.TOTALCUOTAS,
            'NumeroCuotasVencidas': row.VENCIDACUOTAS,
            'MontoVencido30dias': row.N030DMONTOVENCIDO,
            'MontoVencido60dias': row.N060DMONTOVENCIDO,
            'MontoVencido90dias': row.N090DMONTOVENCIDO,
            'MontoVencido120dias': row.N120DMONTOVENCIDO,
            'MontoVencido180dias': row.N180DMONTOVENCIDO,
            'MontoVencidoUnAno': row.N360DMONTOVENCIDO,
            'MontoVencidoMasUnAno': row.MA1AMONTOVENCIDO,
            'MontoVencer30dias': row.N030DMONTOAVENCER,
            'MontoVencer60dias': row.N060DMONTOAVENCER,
            'MontoVencer90dias': row.N090DMONTOAVENCER,
            'MontoVencer120dias': row.N120DMONTOAVENCER,
            'MontoVencer180dias': row.N180DMONTOAVENCER,
            'MontoVencerUnAno': row.N360DMONTOAVENCER,
            'MontoVencerMasUnAno': row.MA1AMONTOAVENCER,
            'BancaSocial': 1,
            'UnidadProduccionSocial': 1,
            'ModalidadMicrocredito': 0,
            'UsoFinanciero': 0,
            'DestinoRecursosMicrofinancieros': 0,
            'CantidadTrabajadores': 0,
            'VentaAnuales': 0,
            'FechaEstadoFinanciero': pd.to_datetime('01/01/1900'),
            'NumeroRTN': '',
            'LicenciaTuristicaNacional': '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica': pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': 0,
            'NumeroExpedienteConformidadTuristica': 0,
            'NombreProyectoUnidadProduccion': '',
            'DireccionProyectoUnidadProduccion': '',
            'CodigoTipoProyecto': 0,
            'CodigoTipoOperacionesFinanciamiento': 0,
            'CodigoSegmento': 0,
            'TipoZona': 0,
            'FechaAutenticacionProtocolizacion': pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': 0,
            'PagosEfectuadosDuranteMes': 0,
            'MontosLiquidadosFechaCierre': 0.00,
            'AmortizacionesCapitalAcumuladasFecha': 0.00,
            'TasaIncentivo': 0,
            'NumeroOficioIncentivo': '',
            'NumeroRegistro_ConstanciaMPPAT': 0,
            'TipoRegistro_ConstanciaMPPAT': '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': pd.to_datetime('01/01/1900'),
            'TipoSubsector': 0,
            'Rubro': 0,
            'CodigoUso': 0,
            'CantidadUnidades': 0,
            'CodigoUnidadMedida': 0,
            'SectorProduccion': 0,
            'CantidadHectareas': 0,
            'SuperficieTotalPropiedad': 0,
            'NumeroProductoresBeneficiarios': 0,
            'Prioritario': 0,
            'DestinoManufacturero': 0,
            'DestinoEconomico': 0,
            'TipoBeneficiario': 0,
            'ModalidadHipoteca': 0,
            'IngresoFamiliar': 0.00,
            'MontoLiquidadoDuranteAnoCurso': 0.00,
            'SaldoCredito31_12': 0.00,
            'CantidadViviendasConstruir': 0,
            'RendimientosCobrarReestructurados': self.get_bbat_amounts(row.Acct, 'vigente')
            if str(row.CtaLocal).startswith('132') else 0.00,
            'RendimientosCobrarAfectosReporto': 0.00,
            'RendimientosCobrarLitigio': 0.00,
            'InteresEfectivamenteCobrado': self.is_nan(row.Int_Efectivamente_Cobrado, 0.00),
            'PorcentajeComisionFlat': self.is_nan(row.Porc_Comision_Flat, 0.00),
            'MontoComisionFlat': self.is_nan(row.Monto_Comision_Flat, 0.00),
            'PeriocidadPagoEspecialCapital': self.is_nan(row.Periodicidad_Pago_Especial_Capital, 0),
            'FechaCambioEstatusCredito': self.is_nan(row.Fecha_Cambio_Status, pd.to_datetime('01/01/1900')),
            'FechaRegistroVencidaLitigiooCastigada': self.is_nan(
                row.Fecha_Reg_Venc_Lit_cast,
                pd.to_datetime('01/01/1900')
            ),
            'FechaExigibilidadPagoUltimaCuotaPagada': self.is_nan(
                row.Fecha_Exigibilidad_pago_ult_cuota,
                pd.to_datetime('01/01/1900')
            ),
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': self.is_nan(self.get_bbat_amounts(row.Acct, 'orden'), 0.00),
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('01/01/1900'),
            'TipoVivienda': self.is_nan(row.Tipo_Vivienda, 0),
            'FechaFinPeriodoGraciaPagoInteres': self.is_nan(
                row.Fecha_Fin_Periodo_gracia_Pago_interes,
                pd.to_datetime('01/01/1900')
            ),
            'CapitalTransferido': self.is_nan(row.Capital_Trasferido, 0.00),
            'FechaCambioEstatusCapitalTransferido': self.is_nan(
                row.Fecha_cambio_Capital_Transferido,
                pd.to_datetime('01/01/1900')
            ),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': CD_CHOICES.get('ICG_NO_DIRIGIDA'),
        } for row in self.at04cre_cnd_df[filter_df].itertuples()]), ignore_index=True, sort=True)

        #  Sobregiros Other ICG

        print(datetime.date.today(), ': Adding Sobregiros Other ICG...')

        self.at04_df = self.at04_df.append(pd.DataFrame([{
            'NumeroCredito': row.Acct,
            'FechaLiquidacion': row.OpenDate,
            'FechaSolicitud': pd.to_datetime(row.OpenDate) - pd.DateOffset(days=12),
            'FechaAprobacion': row.OpenDate,
            'Oficina': row.BranchId,
            'CodigoContable': '1330210000',
            'NumeroCreditoPrimerDesembolso': row.Acct,
            'NumeroDesembolso': 1,
            'CodigoLineaCredito': 1,
            'MontoLineaCredito': 0.00,
            'EstadoCredito': 1,
            'TipoCredito': 2,
            'SituacionCredito': 3,
            'PlazoCredito': 'C',
            'ClasificacionRiesgo': row.Riesgo,
            'DestinoCredito': self.get_actividad_cliente(row.Acct, 'GCG', '', CD_CHOICES.get('SOBREGIROS')),
            'NaturalezaCliente': 1,
            'TipoCliente': str(row.CId).strip()[0].upper(),
            'IdentificacionCliente': str(row.CId).strip()[1:],
            'Nombre_RazonSocial': str(row.Nombre).strip().title().replace('\'\'', '´'),
            'Genero': 2 if row.SEX == 'M' else 1 if row.SEX == 'F' else 3,
            'TipoClienteRIF': str(row.CId).strip()[0],
            'IdentificacionTipoClienteRIF': str(row.CId).strip()[1:],
            'ActividadCliente': self.get_actividad_cliente(row.Acct, 'GCG', '', CD_CHOICES.get('SOBREGIROS')),
            'PaisNacionalidad': 'VE' if str(row.CId).strip()[0].upper() == 'V' else 'XX',
            'DomicilioFiscal': row.NA2,
            'ClienteNuevo': 1,
            'Cooperativa': 1,
            'Sindicado': 0,
            'BancoLiderSindicato': 0,
            'RelacionCrediticia': 2 if row.TypeId == 22 else 1,
            'GrupoEconomicoFinanciero': 1,
            'NombreGrupoEconomicoFinanciero': '',
            'CodigoParroquia': '',
            'PeriodoGraciaCapital': 0,
            'PeriodicidadPagoCapital': 8,
            'PeriodicidadPagoInteresCredito': 8,
            'FechaVencimientoOriginal': row.RecordDate,
            'FechaVencimientoActual': row.RecordDate,
            'FechaReestructuracion': DEFAULT_DATE,
            'CantidadProrroga': 0,
            'FechaProrroga': DEFAULT_DATE,
            'CantidadRenovaciones': 0,
            'FechaUltimaRenovacion': DEFAULT_DATE,
            'FechaCancelacionTotal': DEFAULT_DATE,
            'FechaVencimientoUltimaCoutaCapital': row.RecordDate,
            'UltimaFechaCancelacionCuotaCapital': DEFAULT_DATE,
            'FechaVencimientoUltimaCuotaInteres': row.RecordDate,
            'UltimaFechaCancelacionCuotaIntereses': DEFAULT_DATE,
            'Moneda': 'VES',
            'TipoCambioOriginal': 1,
            'TipoCambioCierreMes': 1,
            'MontoOriginal': row.Overdraft,
            'MontoInicial': row.Overdraft,
            'MontoLiquidadoMes': 0,
            'EntePublico': 0,
            'MontoInicialTerceros': 0,
            'Saldo': row.Overdraft,
            'RendimientosCobrar': 0,
            'RendimientosCobrarVencidos': 0,
            'RendimientosCobrarMora': 0,
            'ProvisionEspecifica': row.SaldoProvision,
            'PorcentajeProvisionEspecifica': row.Provision,
            'ProvisionRendimientoCobrar': 0,
            'TasasInteresCobrada': 24,
            'TasasInteresActual': 24,
            'IndicadorTasaPreferencial': 1,
            'TasaComision': 22,
            'ComisionesCobrar': 0,
            'ComisionesCobradas': 0,
            'ErogacionesRecuperables': 0,
            'TipoGarantiaPrincipal': 10,
            'NumeroCuotas': 1,
            'NumeroCuotasVencidas': 1,
            'MontoVencido30dias': 0,
            'MontoVencido60dias': 0,
            'MontoVencido90dias': 0,
            'MontoVencido120dias': 0,
            'MontoVencido180dias': 0,
            'MontoVencidoUnAno': 0,
            'MontoVencidoMasUnAno': 0,
            'MontoVencer30dias': 0,
            'MontoVencer60dias': 0,
            'MontoVencer90dias': 0,
            'MontoVencer120dias': 0,
            'MontoVencer180dias': 0,
            'MontoVencerUnAno': 0,
            'MontoVencerMasUnAno': 0,
            'BancaSocial': 1,
            'UnidadProduccionSocial': 1,
            'ModalidadMicrocredito': 0,
            'UsoFinanciero': 0,
            'DestinoRecursosMicrofinancieros': 0,
            'CantidadTrabajadores': 0,
            'VentaAnuales': 0,
            'FechaEstadoFinanciero': pd.to_datetime('01/01/1900'),
            'NumeroRTN': '',
            'LicenciaTuristicaNacional': '',
            'FechaEmisionFactibilidadSociotecnica_ConformidadTuristica': pd.to_datetime('01/01/1900'),
            'NumeroExpedienteFactibilidadSociotecnica': 0,
            'NumeroExpedienteConformidadTuristica': 0,
            'NombreProyectoUnidadProduccion': '',
            'DireccionProyectoUnidadProduccion': '',
            'CodigoTipoProyecto': 0,
            'CodigoTipoOperacionesFinanciamiento': 0,
            'CodigoSegmento': 0,
            'TipoZona': 0,
            'FechaAutenticacionProtocolizacion': pd.to_datetime('01/01/1900'),
            'FechaUltimaInspeccion': pd.to_datetime('01/01/1900'),
            'PorcentajeEjecucionProyecto': 0,
            'PagosEfectuadosDuranteMes': 0,
            'MontosLiquidadosFechaCierre': 0.00,
            'AmortizacionesCapitalAcumuladasFecha': 0.00,
            'TasaIncentivo': 0,
            'NumeroOficioIncentivo': '',
            'NumeroRegistro_ConstanciaMPPAT': 0,
            'TipoRegistro_ConstanciaMPPAT': '',
            'FechaVencimientoRegistro_ConstanciaMPPAT': pd.to_datetime('01/01/1900'),
            'TipoSubsector': 0,
            'Rubro': 0,
            'CodigoUso': 0,
            'CantidadUnidades': 0,
            'CodigoUnidadMedida': 0,
            'SectorProduccion': 0,
            'CantidadHectareas': 0,
            'SuperficieTotalPropiedad': 0,
            'NumeroProductoresBeneficiarios': 0,
            'Prioritario': 0,
            'DestinoManufacturero': 0,
            'DestinoEconomico': 0,
            'TipoBeneficiario': 0,
            'ModalidadHipoteca': 0,
            'IngresoFamiliar': 0.00,
            'MontoLiquidadoDuranteAnoCurso': 0.00,
            'SaldoCredito31_12': 0.00,
            'CantidadViviendasConstruir': 0,
            'RendimientosCobrarReestructurados': 0.00,
            'RendimientosCobrarAfectosReporto': 0.00,
            'RendimientosCobrarLitigio': 0.00,
            'InteresEfectivamenteCobrado': 0.00,
            'PorcentajeComisionFlat': 0.00,
            'MontoComisionFlat': 0.00,
            'PeriocidadPagoEspecialCapital': 0,
            'FechaCambioEstatusCredito': row.Fecha_Cambio_Estatus_Credito,
            'FechaRegistroVencidaLitigiooCastigada': row.Fecha_Registro_Vencida_Litigio_Castigada,
            'FechaExigibilidadPagoUltimaCuotaPagada': row.Fecha_Exigibilidad_Pago_ultima_cuota_pagada,
            'CuentaContableProvisionEspecifica': 0,
            'CuentaContableProvisionRendimiento': 1490310000,
            'CuentaContableInteresCuentaOrden': 8190410400,
            'MontoInteresCuentaOrden': 0.00,
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('01/01/1900'),
            'TipoVivienda': 0,
            'FechaFinPeriodoGraciaPagoInteres': pd.to_datetime('01/01/1900'),
            'CapitalTransferido': 0.00,
            'FechaCambioEstatusCapitalTransferido': pd.to_datetime('01/01/1900'),
            'FechaNacimiento': pd.to_datetime('01/01/1900'),
            'UnidadValoracionAT04': 0.00,
            'TipoCD': CD_CHOICES.get('SOBREGIROS'),
        } for row in self.sc_df.itertuples()]), ignore_index=True, sort=True)

        self.at04_df['MakerDate'] = datetime.date.today()
        self.at04_df.MakerDate = pd.to_datetime(self.at04_df.MakerDate)
        self.at04_df['MakerUser'] = user

        # %%
        #  Making some adjustments to the report

        # Setting CapitalCastigado as MontoOriginal and Inicial of Canceled credits
        filter_df = (self.at04_df.EstadoCredito == 3) & \
                    (self.at04_df.MontoLineaCredito == 0.00) & \
                    (self.at04_df.TipoDC.isin([
                        CD_CHOICES.get('CCA_CONSUMO'),
                        CD_CHOICES.get('CCH'),
                        CD_CHOICES.get('PIL'),
                        CD_CHOICES.get('REWRITES'),
                        CD_CHOICES.get('MICROFINANCIERO'),
                        CD_CHOICES.get('CARROS'),
                        CD_CHOICES.get('SEGUROS')
                    ]))

        self.at04_df.loc[filter_df, ['MontoOriginal', 'MontoInicial']] = self.at04_df[filter_df].set_index('NumeroCredito').join(
            self.ah_mod_df, rsuffix='_ah')[['CapitalCastigado', 'CapitalCastigado']]

        # Setting FechaLiquidacion as FechaVencimientoUltimaCuotalCapital and Intereses of Canceled credits
        filter_canceled_df = self.at04_df.EstadoCredito == 3
        filter_active_df = self.at04_df.EstadoCredito == 1
        filter_type_df = self.at04_df.TipoDC.isin([
            CD_CHOICES.get('CCA_CONSUMO'),
            CD_CHOICES.get('CCH'),
            CD_CHOICES.get('PIL'),
            CD_CHOICES.get('REWRITES'),
            CD_CHOICES.get('TDC'),
            CD_CHOICES.get('HLP'),
            CD_CHOICES.get('MICROFINANCIERO'),
            CD_CHOICES.get('AGRICOLA_OTHER_ICG'),
            CD_CHOICES.get('CARROS'),
            CD_CHOICES.get('SEGUROS')
        ])

        self.at04_df.loc[
            filter_canceled_df & filter_type_df,
            ['FechaVencimientoUltimaCoutaCapital',
                'FechaVencimientoUltimaCuotaInteres']
        ] = self.at04_df[filter_df][['FechaLiquidacion', 'FechaLiquidacion']]

        self.at04_df.loc[
            filter_active_df & filter_type_df,
            ['FechaVencimientoUltimaCoutaCapital',
                'FechaVencimientoUltimaCuotaInteres']
        ] = [DEFAULT_DATE, DEFAULT_DATE]

        # Check that UltimaechaCancelacionCuotaIntereses is 19000101
        filter_df = (self.at04_df.MontoOriginal == self.at04_df.Saldo) & \
                    (self.at04_df.PeriodicidadPagoInteresCredito < 1024) & \
                    (self.at04_df.TipoDC.isin([
                        CD_CHOICES.get('ICG_NO_DIRIGIDA'),
                    ]))
        self.at04_df.loc[filter_df,
                         'UltimaFechaCancelacionCuotaIntereses'] = DEFAULT_DATE

        # Check that TipoCredito = 1 when TipoCD PILS and CodigoContable = 1330510102
        filter_df = (self.at04_df.CodigoContable == 1330510102) & \
                    (self.at04_df.TipoDC.isin([
                        CD_CHOICES.get('PILS'),
                    ]))
        self.at04_df.loc[filter_df, 'TipoCredito'] = 1

        # Check that EstadoCredito = 3 and SituacionCredito = 0
        # When CodigoContable = 8190310100
        self.at04_df.loc[
            self.at04_df.CodigoContable == 8190310100,
            ['EstadoCredito', 'SituacionCredito']
        ] = [3, 0]

        # Check that TipoCredito equals zero (0) for canceled credits
        filter_canceled_df = self.at04_df.EstadoCredito == 3
        self.at04_df.loc[filter_canceled_df, 'TipoCredito'] = 0

        # Check that ClasificacionRiesgo is zero (0) for EstadoCredito in 2 and 3
        filter_df = self.at04_df.EstadoCredito in (2, 3)
        self.at04_df.loc[filter_df, 'ClasificacionRiesgo'] = 0

        # TODO: Include AT04_MES_ANTERIOR TABLE

        # %%
        print('Exporting AT04 Report...')

        out_path = os.path.join(
            self._out_path, f'AT04{self._fecha_reportar.strftime("%Y%m%d")}.txt')

        Path(os.path.dirname(os.path.abspath(out_path))).mkdir(
            parents=True, exist_ok=True)

        self.at04_df[self._labels].to_csv(
            out_path,
            sep='~', date_format='%Y%m%d', index=False)

        return {
            'report_path': out_path,
            'description': 'Cartera de Creditos',
            'last_processing_date': datetime.date.today(),
            'data': self.at04_df[self._labels].head(100).to_json(
                orient='records',
                date_format='iso',
                double_precision=2
            )
        }
