"""Data Preparation module"""

import datetime
import ntpath
import pandas as pd

from os.path import join, dirname, abspath
from os import remove
from django.conf import settings


HLP = 6 # Hipotecario Largo Plazo
HCP = 7 # Hipotecario Corto Plazo
TURISMO = 8 # Turismo
MICROFINANCIERO = 9 # Microfinanciero
MANUFACTURA = 10 # Manufactura
AGRICOLA_ICG = 11 # Agricola ICG
AGRICOLA_OTHER_ICG = 12 # Agricola Other ICG

RESOURCE_CHOICES = [
    'AH',
    'AT04CRE'
    'AT07'
    'BBAT',
    'CND',
    'CD',
    'FDN',
    'GICG',
    'LNP860',
    'MM',
    'MISP',
    'PPRRHH',
    'RICG',
    'SIIF',
    'SC',
    'VNP003T',
]


class DataPreparation():
    """Data Preparation Class for every resource file"""

    def path_leaf(self, path):
        """Gets the name of the file (with its extention) from a given full path"""

        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)


    def get_path_file(self, path):
        """Gets the absolute path, file name and extension of the given full path to file"""

        abs_dir = dirname(abspath(path))
        f_name, f_ext = self.path_leaf(path).split('.')

        return abs_dir, f_name, f_ext


    def account_history(self, data, user):
        """Account History resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, f_ext = self.get_path_file(path)

        a_h = pd.read_csv(path, sep='~', low_memory=False)

        a_h.RecordDate = pd.to_datetime(a_h.RecordDate)
        a_h.PastDueDate1 = pd.to_datetime(
            a_h.PastDueDate1)
        a_h.PastDueDate2 = pd.to_datetime(
            a_h.PastDueDate2)
        a_h.LastRcvdPmtDate = pd.to_datetime(
            a_h.LastRcvdPmtDate)
        a_h.BlockCode1Date = pd.to_datetime(
            a_h.BlockCode1Date)
        a_h.BlockCode2Date = pd.to_datetime(
            a_h.BlockCode2Date)
        a_h.MaturityDate = pd.to_datetime(
            a_h.MaturityDate)
        a_h.ExpirationDate = pd.to_datetime(
            a_h.ExpirationDate)
        a_h.OpenDate = pd.to_datetime(a_h.OpenDate)
        a_h.CancelDate = pd.to_datetime(a_h.CancelDate)
        a_h.ExpirationDate = pd.to_datetime(
            a_h.ExpirationDate)

        a_h.RecordDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.PastDueDate1.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.PastDueDate2.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.LastRcvdPmtDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.BlockCode1Date.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.BlockCode2Date.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.MaturityDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.ExpirationDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.OpenDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.CancelDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)
        a_h.ExpirationDate.fillna(
            pd.to_datetime('1900-01-01'), inplace=True)

        a_h['MakerDate'] = datetime.date.today
        a_h['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        a_h.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        remove(join(abs_dir, f_name, f_ext))

        return out_path  # TODO: Maybe add the relative path


    def at04_cre(self, data, user):
        """AT04CRE resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        labels = [
            'BRANCH', 'REFERNO', 'LIQUFECHA', 'SOLIFECHA', 'APROFECHA',
            'VCTOFECHA', 'VCTOULTINTER', 'VCTOULTPRINC', 'ORIGFECHA',
            'PGTOULTCAPITAL', 'PGTOULTINTERES', 'BASECLI', 'RIFCLI',
            'NOMECLI', 'SICVENCLI', 'SICUSACLI', 'NACICLI', 'DOMICLI',
            'FECHACLI', 'LIABICLI', 'LIABNOMCLI', 'RIESGOCLI', 'ADDRESS1',
            'ADDRESS2', 'ADDRESS3', 'ADDRESS4', 'ADDRESS5', 'ADDRESS6',
            'ADDRESSEXTRA', 'CTRORG', 'QTDREN', 'MONEDA', 'PRODCAT',
            'LV', 'STATUS', 'PLAZO', 'GENLEDGER', 'CREDITLINE', 'INTORIGTASA',
            'CAMBIOTASA', 'COMISTASA', 'ORIGIMONTO', 'PAGOMESMONTO',
            'PAGOTOTAL', 'SALDOMONTO', 'TOTALCUOTAS', 'PAGASCUOTAS',
            'VENCIDACUOTAS', 'N030DMONTOVENCIDO', 'N060DMONTOVENCIDO',
            'N090DMONTOVENCIDO', 'N120DMONTOVENCIDO', 'N180DMONTOVENCIDO',
            'N360DMONTOVENCIDO', 'MA1AMONTOVENCIDO', 'N030DMONTOAVENCER',
            'N060DMONTOAVENCER', 'N090DMONTOAVENCER', 'N120DMONTOAVENCER',
            'N180DMONTOAVENCER', 'N360DMONTOAVENCER', 'MA1AMONTOAVENCER',
            'FILLER',
        ]

        fwidths = [3, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 6, 12, 32, 4, 3, 3, 3, 6, 6, 32,
                   1, 18, 26, 32, 32, 32, 32, 516, 10, 4, 3, 5, 2, 3, 5, 15, 5, 9, 9,
                   9, 18, 18, 18, 18, 4, 4, 4, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,
                   18, 18, 18, 18, 4, ]

        at04cre = pd.read_fwf(path, widths=fwidths, names=labels)

        at04cre.LIQUFECHA = pd.to_datetime(at04cre.LIQUFECHA, format='%Y%m%d')
        at04cre.SOLIFECHA = pd.to_datetime(at04cre.SOLIFECHA, format='%Y%m%d')
        at04cre.APROFECHA = pd.to_datetime(at04cre.APROFECHA, format='%Y%m%d')
        at04cre.VCTOFECHA = pd.to_datetime(at04cre.VCTOFECHA, format='%Y%m%d')
        at04cre.VCTOULTINTER = pd.to_datetime(
            at04cre.VCTOULTINTER, format='%Y%m%d')
        at04cre.VCTOULTPRINC = pd.to_datetime(
            at04cre.VCTOULTPRINC, format='%Y%m%d')
        at04cre.PGTOULTCAPITAL = pd.to_datetime(
            at04cre.PGTOULTCAPITAL, format='%Y%m%d')
        at04cre.PGTOULTINTERES = pd.to_datetime(
            at04cre.PGTOULTINTERES, format='%Y%m%d')

        at04cre.CREDITLINE = at04cre.CREDITLINE.apply(lambda x: x/100)
        at04cre.INTORIGTASA = at04cre.INTORIGTASA.apply(lambda x: x/100)
        at04cre.CAMBIOTASA = at04cre.CAMBIOTASA.apply(lambda x: x/100)
        at04cre.COMISTASA = at04cre.COMISTASA.apply(lambda x: x/100)
        at04cre.ORIGIMONTO = at04cre.ORIGIMONTO.apply(lambda x: x/100)
        at04cre.PAGOMESMONTO = at04cre.PAGOMESMONTO.apply(lambda x: x/100)
        at04cre.PAGOTOTAL = at04cre.PAGOTOTAL.apply(lambda x: x/100)
        at04cre.SALDOMONTO = at04cre.SALDOMONTO.apply(lambda x: x/100)
        at04cre.PAGOTOTAL = at04cre.PAGOTOTAL.apply(lambda x: x/100)
        at04cre.N030DMONTOAVENCER = at04cre.N030DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.N060DMONTOAVENCER = at04cre.N060DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.N090DMONTOAVENCER = at04cre.N090DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.N120DMONTOAVENCER = at04cre.N120DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.N180DMONTOAVENCER = at04cre.N180DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.N360DMONTOAVENCER = at04cre.N360DMONTOAVENCER.apply(
            lambda x: x/100)
        at04cre.MA1AMONTOAVENCER = at04cre.MA1AMONTOAVENCER.apply(
            lambda x: x/100)

        at04cre['MakerDate'] = datetime.date.today
        at04cre['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        at04cre.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def at07(self, data, user):
        """AT07 resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        names = [
            'NumeroCredito', 'CodigoBien', 'FechaLiquidacion',
            'CodigoContable', 'ClaseBien', 'TipoCliente',
            'IdentificacionCliente', 'NombreRazonSocial',
            'SituacionGarante', 'MontoInicial', 'MontoActual',
            'MontoAvaluo', 'ValorMercado', 'FechaUltimoAvaluo',
            'CodigoPeritoAvaluador',
        ]

        parse_dates = [
            'FechaLiquidacion',
            'FechaUltimoAvaluo',
        ]

        at07_df = pd.read_csv(path,
                              sep='~',
                              low_memory=False,
                              encoding="latin",
                              parse_dates=parse_dates,
                              header=None,
                              names=names)

        at07_df[['MontoInicial',
                 'MontoActual',
                 'MontoAvaluo',
                 'ValorMercado']] = at07_df[['MontoInicial',
                                             'MontoActual',
                                             'MontoAvaluo',
                                             'ValorMercado']].replace(to_replace=',',
                                                                      value='.',
                                                                      regex=True)

        at07_df.MontoInicial = pd.to_numeric(
            at07_df.MontoInicial, errors='coerce', downcast='float')
        at07_df.MontoActual = pd.to_numeric(
            at07_df.MontoActual, errors='coerce', downcast='float')
        at07_df.MontoAvaluo = pd.to_numeric(
            at07_df.MontoAvaluo, errors='coerce', downcast='float')
        at07_df.ValorMercado = pd.to_numeric(
            at07_df.ValorMercado, errors='coerce', downcast='float')
        at07_df['MakerDate'] = datetime.date.today
        at07_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        at07_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def bal_by_acct_transformada(self, data, user):
        """BalByAcct Transformada resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        bbat = pd.read_csv(path, sep='	', low_memory=False)

        bbat.SaldoRendXcobrar.replace(
            to_replace='Bs.S', value='', inplace=True, regex=True)
        bbat.SaldoRendXcobrarVenc.replace(
            to_replace='Bs.S', value='', inplace=True, regex=True)
        bbat.SaldoRendCuentaOrden.replace(
            to_replace='Bs.S', value='', inplace=True, regex=True)
        bbat.SaldoRendXMora.replace(
            to_replace='Bs.S', value='', inplace=True, regex=True)

        bbat.SaldoRendXcobrar = pd.to_numeric(
            bbat.SaldoRendXcobrar, errors='coerce')
        bbat.SaldoRendXcobrarVenc = pd.to_numeric(
            bbat.SaldoRendXcobrarVenc, errors='coerce')
        bbat.SaldoRendCuentaOrden = pd.to_numeric(
            bbat.SaldoRendCuentaOrden, errors='coerce')
        bbat.SaldoRendXMora = pd.to_numeric(
            bbat.SaldoRendXMora, errors='coerce')
        bbat['MakerDate'] = datetime.date.today
        bbat['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        bbat.to_csv(
            out_path, sep='~', index=False)

        return out_path


    def cartera_no_dirigida(self, data, user):
        """Cartera No Dirigida resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        names = [
            'Branch', 'LV', 'NombreVehiculo', 'Cuenta', 'Grupo',
            'Pal', 'Pal_cat_descr', 'Prod', 'Prod_cat_descr',
            'Referencia', 'Descripcion', 'ClasificacionRiesgo',
            'Provision', 'A', 'FechaInicio', 'FechaFinal', 'B', 'C',
            'BCV', 'Tasa', 'Debito', 'Credito', 'Saldo', 'Type',
            'Type3dig', 'CuentaSIF', 'RendimientosCobrarReestructurados',
            'RendimientosCobrarEfectosReporto', 'RendimientosCobrarLitigio',
            'InteresesEfectivamenteCobrados', 'PorcentajeComisionFLAT',
            'MontoComisionFLAT', 'PeriodicidadPagoEspecialCapital',
            'FechaCambioEstatusCredito', 'FechaRegistroVencidaLitigioCastigada',
            'FechaExigibilidadPagoUltimaCuotaPagada',
            'CuentaContableProvisionEspecifica',
            'CuentaContableProvisionRendimiento',
            'CuentaContableInteresCuentaOrden',
            'MontoInteresCuentaOrden', 'TipoBeneficiarioSectorManufacturero',
            'TipoBeneficiarioSectorTurismo', 'BeneficiarioEspecial',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'TipoVivienda', 'FechaFinPeriodoGraciaPagoInteres',
            'CapitalTransferido', 'FechaCambioEstatusCapitalTransferido',
            'SaldoProvision', 'ActividadCliente', 'TipoGarantiaPrincipal',
        ]

        parse_dates = [
            'FechaCambioEstatusCredito',
            'FechaRegistroVencidaLitigioCastigada',
            'FechaExigibilidadPagoUltimaCuotaPagada',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'FechaFinPeriodoGraciaPagoInteres',
            'FechaCambioEstatusCapitalTransferido'
        ]

        na_values = {
            'ActividadCliente': '0',
            'TipoGarantiaPrincipal': '0',
        }

        cnd = pd.read_excel(path, parse_dates=parse_dates, names=names)

        cnd.FechaInicio = pd.to_datetime(cnd.FechaInicio, format='%y%m%d')
        cnd.FechaFinal = pd.to_datetime(cnd.FechaFinal, format='%y%m%d')

        cnd.fillna(value=na_values, inplace=True)

        cnd['MakerDate'] = datetime.date.today
        cnd['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        cnd.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def cartera_dirigida(self, data, user):
        """Cartera Dirigida resource Data Preparation"""

        paths = [path for path in data['file']]
        paths.sort()

        abs_dir, _, _ = self.get_path_file(paths[0])

        parse_dates = [
            'FECHA_SOLICITUD', 'FECHA_APROBACION', 'FECHA_LIQUIDACION',
            'FECHA_VENC_ORIGINAL', 'FECHA_VENC_ACTUAL', 'FECHA_REESTRUCTURACION',
            'FECHA_PRORROGA', 'FECHA_ULTIMA_RENOVACION', 'FECHA_CANCEL',
            'FECHA_VENC_ULTIMA_CUOTA_CAPITAL', 'ULTIMA_FECHA_CANCEL_CUOTA_CAPITAL',
            'FECHA_VENC_ULTIMA_CUOTA_INTERES', 'ULTIMA_FECHA_CANCEL_CUOTA_INTERES',
            'FECHA_ESTADO_FINANCIERO', 'FECHA_EMISION_FACTIBILIDAD_TECNICA',
            'FECHA_AUTENTICACION', 'FECHA_ULTIMA_INSPECCION',
            'FECHA_VENC_REGISTRO', 'Upd_Date'
        ]

        cd_agricola_gcg = pd.read_csv(paths[0], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_agricola_icg = pd.read_csv(paths[1], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_hcp = pd.read_csv(paths[2], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_hlp = pd.read_csv(paths[3], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_manufactura = pd.read_csv(paths[4], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_micro = pd.read_csv(paths[5], sep='	', low_memory=False, parse_dates=parse_dates)
        cd_turismo = pd.read_csv(paths[6], sep='	', low_memory=False, parse_dates=parse_dates)

        cd_agricola_gcg.drop(cd_agricola_gcg.columns[len(cd_agricola_gcg.columns)-1],
                             axis=1,
                             inplace=True)
        cd_agricola_icg.drop(cd_agricola_icg.columns[len(cd_agricola_icg.columns)-1],
                             axis=1,
                             inplace=True)
        cd_hlp.drop(cd_hlp.columns[len(cd_hlp.columns)-1], axis=1, inplace=True)
        cd_hcp.drop(cd_hcp.columns[len(cd_hcp.columns)-1], axis=1, inplace=True)
        cd_manufactura.drop(cd_manufactura.columns[len(cd_manufactura.columns)-1],
                            axis=1,
                            inplace=True)
        cd_micro.drop(cd_micro.columns[len(cd_micro.columns)-1], axis=1, inplace=True)
        cd_turismo.drop(cd_turismo.columns[len(cd_turismo.columns)-1], axis=1, inplace=True)

        cd_agricola_gcg['TYPE_CD'] = AGRICOLA_OTHER_ICG
        cd_agricola_icg['TYPE_CD'] = AGRICOLA_ICG
        cd_hlp['TYPE_CD'] = HLP
        cd_hcp['TYPE_CD'] = HCP
        cd_manufactura['TYPE_CD'] = MANUFACTURA
        cd_micro['TYPE_CD'] = MICROFINANCIERO
        cd_turismo['TYPE_CD'] = TURISMO

        c_d = pd.concat([cd_agricola_gcg,
                         cd_agricola_icg,
                         cd_hcp, cd_hlp,
                         cd_manufactura,
                         cd_micro, cd_turismo], ignore_index=True)
        c_d['MakerDate'] = datetime.date.today
        c_d['MakerUser'] = user

        out_path = join(abs_dir, 'RPT_STG_Dirigidas.txt')

        c_d.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def fdn(self, data, user):
        """Fecha de Nacimiento resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        parse_dates = [
            'RecordDate',
        ]

        fdn_df = pd.read_csv(path,
                             sep='~',
                             low_memory=False,
                             encoding="latin",
                             parse_dates=parse_dates)

        fdn_df.FechaNacimiento = pd.to_datetime(
            fdn_df.FechaNacimiento,
            format='%Y%m%d',
            errors='coerce'
            )
        fdn_df['MakerDate'] = datetime.date.today
        fdn_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        fdn_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def gavetas_icg(self, data, user):
        """Gavetas ICG resource Data Preparation"""

        paths = [path for path in data['file']]
        paths.sort()

        abs_dir, _, _ = self.get_path_file(paths[0])

        names = [
            'RIF', 'NombreRazonSocial', 'NumeroCredito',
            'InteresesEfectivamenteCobrados', 'PorcentajeComisionFLAT',
            'MontoComisionFLAT', 'PeriodicidadPagoEspecialCapital',
            'FechaCambioEstatusCredito',
            'FechaExigibilidadPagolaultimaCuotaPagada',
            'FechaRegistroVencidaLitigioCastigada',
            'TipoIndustria', 'TipoBeneficiarioSectorManufacturero',
            'TipoBeneficiarioSectorTurismo', 'BeneficiarioEspecial',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'TipoVivienda', 'FechaFinPeriodoGraciaPagoInteres',
            'CapitalTransferido', 'FechaCambioEstatusCapitalTransferido',
        ]

        parse_dates = [
            'FechaExigibilidadPagolaultimaCuotaPagada',
            'FechaRegistroVencidaLitigioCastigada',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'FechaFinPeriodoGraciaPagoInteres',
            'FechaCambioEstatusCapitalTransferido',
            'FechaCambioEstatusCredito'
        ]

        na_values = {
            'InteresesEfectivamenteCobrados': 0,
            'PorcentajeComisionFLAT': 0,
            'MontoComisionFLAT': 0,
            'PeriodicidadPagoEspecialCapital': 0,
            'FechaExigibilidadPagolaultimaCuotaPagada': pd.to_datetime('1900-01-01'),
            'FechaRegistroVencidaLitigioCastigada': pd.to_datetime('1900-01-01'),
            'TipoIndustria': 0,
            'TipoBeneficiarioSectorManufacturero': 0,
            'TipoBeneficiarioSectorTurismo': 0,
            'BeneficiarioEspecial': 0,
            'FechaEmisionCertificacionBeneficiarioEspecial': pd.to_datetime('1900-01-01'),
            'TipoVivienda': 0,
            'FechaFinPeriodoGraciaPagoInteres': pd.to_datetime('1900-01-01'),
            'CapitalTransferido': 0,
            'FechaCambioEstatusCapitalTransferido': pd.to_datetime('1900-01-01'),
            'FechaCambioEstatusCredito': pd.to_datetime('1900-01-01'),
        }

        g_construccion = pd.read_excel(paths[0],
                                       usecols='C:U',
                                       header=1,)
        g_agricola = pd.read_excel(paths[1],
                                   usecols='B:T',
                                   header=1,
                                   names=names,)
        g_manufactura = pd.read_excel(paths[2],
                                      usecols='B:T',
                                      names=names,)
        g_turismo = pd.read_excel(paths[3],
                                  usecols='B:T',
                                  names=names,
                                  converters={7:str, 8:str})

        # Gaveta Construccion

        cols = list(g_construccion.columns.values)
        order = [0, 1, 2, 3, 4, 5, 6, 18, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        cols = [cols[i] for i in order]

        g_construccion = g_construccion[cols].copy()
        g_construccion.columns = names
        g_construccion[parse_dates] = g_construccion[parse_dates].apply(
            lambda x: pd.to_datetime(x, format='%Y%m%d', errors='coerce'))
        g_construccion.fillna(value=na_values, inplace=True)
        g_construccion['TypeCD'] = HCP

        # Gaveta Agricola

        g_agricola[parse_dates] = g_agricola[parse_dates].apply(
            lambda x: pd.to_datetime(x, format='%Y/%m/%d', errors='coerce'))
        g_agricola.fillna(value=na_values, inplace=True)
        g_agricola['TypeCD'] = AGRICOLA_ICG

        # Gaveta Manufactura

        g_manufactura[parse_dates] = g_manufactura[parse_dates].apply(
            lambda x: pd.to_datetime(x, format='%Y/%m/%d', errors='coerce'))
        g_manufactura.fillna(value=na_values, inplace=True)
        g_manufactura['TypeCD'] = MANUFACTURA

        # Gaveta Turismo

        g_turismo[parse_dates] = g_turismo[parse_dates].apply(
            lambda x: pd.to_datetime(x, format='%Y%m%d', errors='coerce'))
        g_turismo.fillna(value=na_values, inplace=True)
        g_turismo['TypeCD'] = TURISMO

        # Concatenating Them All

        gavetas = pd.concat([g_agricola, g_construccion, g_manufactura, g_turismo],
                            ignore_index=True)

        gavetas['MakerDate'] = datetime.date.today
        gavetas['MakerUser'] = user

        out_path = join(abs_dir, 'AT04_Gavetas.txt')

        gavetas.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def lnp860(self, data, user):
        """LNP860 resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        labels = [
            'P8NOTE', 'P8TINC', 'P8FVUC', 'P8FCCC', 'P8FVUI', 'P8FCCI',
            'P8NRCV', 'P8MV30', 'P8MV60', 'P8MV90', 'P8MV12', 'P8MV18',
            'P8MV1A', 'P8MVM1', 'P8RPCV', 'P8LINT', 'P8FCTC', 'P8MOCA',
            'P8MOIN', 'P8TRXN', 'P8PRAN',
            ]

        fwidths = [11, 13, 8, 8, 8, 8, 8, 13, 13, 13, 13, 13, 13,
                   13, 13, 13, 8, 13, 13, 2, 11,]

        names = ['P8FVUC', 'P8FCCC', 'P8FVUI', 'P8FCCI', 'P8FCTC']
        fields = ['P8MV30', 'P8MV60', 'P8MV90', 'P8MV12', 'P8MV18',
                  'P8MV1A', 'P8MVM1', 'P8RPCV', 'P8LINT', 'P8MOCA',
                  'P8MOIN']

        lnp860_df = pd.read_fwf(path, widths=fwidths, names=labels)

        lnp860_df.P8FVUC = pd.to_datetime(lnp860_df.P8FVUC, format='%d%m%Y', errors='coerce')
        lnp860_df.P8FCCC = pd.to_datetime(lnp860_df.P8FCCC, format='%d%m%Y', errors='coerce')
        lnp860_df.P8FVUI = pd.to_datetime(lnp860_df.P8FVUI, format='%d%m%Y', errors='coerce')
        lnp860_df.P8FCCI = pd.to_datetime(lnp860_df.P8FCCI, format='%d%m%Y', errors='coerce')
        lnp860_df.P8FCTC = pd.to_datetime(lnp860_df.P8FCTC, format='%d%m%Y', errors='coerce')

        lnp860_df[names] = lnp860_df[names].fillna(pd.to_datetime('1900-01-01'))

        lnp860_df.P8NRCV = pd.to_numeric(lnp860_df.P8NRCV, errors='coerce')
        lnp860_df.P8NRCV.fillna(0, inplace=True)
        lnp860_df.P8NRCV = lnp860_df.P8NRCV.astype("int64")

        lnp860_df[fields] = lnp860_df[fields].apply(lambda x: x/100)
        lnp860_df.P8TINC = lnp860_df.P8TINC.apply(lambda x: x/1000000)

        lnp860_df['MakerDate'] = datetime.date.today
        lnp860_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        lnp860_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def migrate_mortgage(self, data, user):
        """Migrate Mortgage resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        converters = {
            'TypeId':str,
        }

        parse_dates = [
            'MigratedDate',
            'OrigOpenDate',
        ]

        mm_df = pd.read_csv(path,
                            sep='~',
                            low_memory=False,
                            parse_dates=parse_dates,
                            converters=converters)

        mm_df.OrigCreditLimit.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        mm_df.OrigCreditLimit = pd.to_numeric(mm_df.OrigCreditLimit, errors='coerce')
        mm_df.TypeId = pd.to_numeric(mm_df.TypeId)
        mm_df.TypeId = mm_df.TypeId.astype('int32')
        mm_df.fillna(value={'Num30':0, 'Num60':0, 'Num90':0,}, inplace=True)

        mm_df['MakerDate'] = datetime.date.today
        mm_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        mm_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def mis_provisiones(self, data, user):
        """MIS Provisiones resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        columns = [
            'Cid', 'Account', 'AccountNew', 'ProdType', 'Provision',
            'SumSaldo', 'Saldo_Provision', 'SaldoRendXcobrar',
            'SaldoRendXcobrarVenc', 'ProvisionREND',
            'Saldo_Provision_REND', 'Overdraft',
            'MaxOfCantCuotasVencidas', 'CtaLocal', 'CtaProvCap',
            'CtaProvRend', 'Riesgo', 'RiskSicri', 'Producto',
            'DescriptionType', 'RecordDate', 'HDelinquency',
            'BlockCode1Date', 'BlockCodeId1', 'BlockReason1',
            'BlockCode2Date', 'BlockCodeId2', 'BlockReason2',
            ]

        na_values = {
            'SumSaldo': 0,
            'MaxOfCantCuotasVencidas': 0,
            'HDelinquency': '',
            'BlockCode1Date': pd.to_datetime('1900-01-01'),
            'BlockCodeId1': '',
            'BlockReason1': '',
            'BlockCode2Date': pd.to_datetime('1900-01-01'),
            'BlockCodeId2': '',
            'BlockReason2': '',
            'CtaLocal': '0',
            'RiskSicri': '',
            'CtaProvRend': '0',
            'SaldoRendXcobrar': 0,
            'SaldoRendXcobrarVenc': 0,
            'ProvisionREND': 0,
            'Saldo_Provision_REND': 0,
            'Producto': '',
            'DescriptionType': '',
            'Overdraft': 0
        }

        misp_cap = pd.read_excel(path, sheet_name='Cliente Data_CAP',
                                 converters={
                                     'Account':str,
                                     'CtaLocal':str,
                                     'CtaProv':str,
                                     'Old_Acct':str,
                                     })
        misp_rend = pd.read_excel(path, sheet_name='Cliente Data_REND',
                                  converters={
                                      'Account':str,
                                      'CtaLocal':str,
                                      'Old_Acct':str,
                                      })
        misp_od = pd.read_excel(path, sheet_name='Cliente_Data_Sobregiro',
                                converters={
                                    'Acct':str,
                                    'CtaLocal':str,
                                    })

        misp_cap.rename({'CtaProv':'CtaProvCap'}, axis='columns', inplace=True)
        misp_rend.rename({'CtaLocal':'CtaProvRend'}, axis='columns', inplace=True)
        misp_od.rename({
            'Acct':'Account',
            'CtaLocal':'CtaProvCap',
            'CId':'Cid'
            }, axis='columns', inplace=True)

        misp_cap.dropna(axis=0, subset=['Account'], how="any", inplace=True)
        misp_rend.dropna(axis=0, subset=['Account'], how="any", inplace=True)
        misp_od.dropna(axis=0, subset=['Account'], how="any", inplace=True)

        misp_cap['AccountNew'] = misp_cap['Account']
        misp_rend['AccountNew'] = misp_rend['Account']
        misp_od['AccountNew'] = misp_od['Account']

        misp_cap.drop(labels=['Old_Acct'], axis=1, inplace=True)
        misp_rend.drop(labels=['Old_Acct'], axis=1, inplace=True)

        misp_cap.set_index('Account', drop=True, inplace=True)
        misp_rend.set_index('Account', drop=True, inplace=True)
        misp_od.set_index('Account', drop=True, inplace=True)

        misp = pd.merge(left=misp_cap,
                        right=misp_rend,
                        left_on='Account',
                        right_on='Account',
                        how='outer',
                        suffixes=('', '_y'))

        misp.Cid.fillna(misp.Cid_y, inplace=True)
        misp.MaxOfCantCuotasVencidas.fillna(misp.MaxOfCantCuotasVencidas_y, inplace=True)
        misp.ProdType.fillna(misp.ProdType_y, inplace=True)
        misp.Riesgo.fillna(misp.Riesgo_y, inplace=True)
        misp.RecordDate.fillna(misp.RecordDate_y, inplace=True)
        misp.AccountNew.fillna(misp.AccountNew_y, inplace=True)

        misp.drop(labels=['Cid_y',
                          'MaxOfCantCuotasVencidas_y',
                          'ProdType_y',
                          'Riesgo_y',
                          'RecordDate_y',
                          'AccountNew_y'],
                  axis=1,
                  inplace=True)

        mispf = pd.merge(left=misp,
                         right=misp_od,
                         left_on='Account',
                         right_on='Account',
                         how='outer',
                         suffixes=('', '_y'))

        mispf.Cid.fillna(mispf.Cid_y, inplace=True)
        mispf.CtaProvCap.fillna(mispf.CtaProvCap_y, inplace=True)
        mispf.Riesgo.fillna(mispf.Riesgo_y, inplace=True)
        mispf.Provision.fillna(mispf.Provision_y, inplace=True)
        mispf.Saldo_Provision.fillna(mispf.Saldo_Provision_y, inplace=True)
        mispf.RecordDate.fillna(mispf.RecordDate_y, inplace=True)
        mispf.AccountNew.fillna(mispf.AccountNew_y, inplace=True)

        mispf.drop(labels=['Cid_y',
                           'CtaProvCap_y',
                           'Riesgo_y',
                           'Provision_y',
                           'Saldo_Provision_y',
                           'RecordDate_y',
                           'AccountNew_y'],
                   axis=1,
                   inplace=True)

        mispf.fillna(value=na_values, inplace=True)

        mispf.reset_index(drop=False, inplace=True)

        mispf['MakerDate'] = datetime.date.today
        mispf['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        mispf[columns].to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def prestamo_prestaciones_hr(self, data, user):
        """Prestamos para las Prestaciones RRHH resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        names = [
            'GEID', 'IdentificacionCliente', 'NombreCliente',
            'FechaOtorgamiento', 'MontoOriginal', 'SaldoActual',
        ]

        parse_dates = [
            'FechaOtorgamiento',
        ]

        abs_dir, f_name, _ = self.get_path_file(path)

        pphr = pd.read_excel(path,
                             usecols='B:G',
                             header=3,
                             names=names,)

        pphr.dropna(axis=0, subset=['MontoOriginal'], how="any", inplace=True)

        pphr[parse_dates] = pphr[parse_dates].apply(
            lambda x: pd.to_datetime(x, format='%Y%m%d', errors='coerce'))

        pphr.insert(loc=1, column='TipoCliente', value='V')

        pphr['MakerDate'] = datetime.date.today
        pphr['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        pphr.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def rendimientos_icg(self, data, user):
        """Rendimientos ICG resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        names = [
            'Branch', 'LV', 'NombreVehiculo', 'Cuenta', 'DescripcionDeLaCuenta',
            'Grupo', 'Pal', 'pal_cat_descr', 'Prod', 'prod_cat_descr',
            'Referencia', 'Descripcion', 'A', 'FechaInicio', 'FechaFinal',
            'B', 'C', 'BCV', 'Tasa', 'Debito', 'Credito', 'Saldo', 'Type',
            'Type3dig', 'CuentaSIF', 'PorcentajeProvision', 'MontoProvision',
        ]

        rend_icg = pd.read_excel(path, names=names)

        rend_icg.FechaInicio = pd.to_datetime(rend_icg.FechaInicio, format='%y%m%d')

        rend_icg['MakerDate'] = datetime.date.today
        rend_icg['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        rend_icg.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def siif(self, data, user):
        """SIIF resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        converters = {
            'BranchId':str,
        }

        parse_dates = [
            'OpenDate', 'RecordDate', 'MaturityDate', 'CloseDate',
            'BlockCode1Date', 'OrigOpenDate', 'Fecha_Cambio_Status',
            'Fecha_Reg_Venc_Lit_cast', 'Fecha_Exigibilidad_pago_ult_cuota',
            'Fecha_Fin_Periodo_gracia_Pago_interes',
            'Fecha_cambio_Capital_Transferido'
        ]

        siif_df = pd.read_csv(path,
                              sep='	',
                              low_memory=False,
                              encoding='latin',
                              parse_dates=parse_dates,
                              converters=converters,)

        siif_df.CreditLimit.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt30DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt60DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt90DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt120DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt150DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt180DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.Amt210DPD.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.SaldoCastigado.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        siif_df.PrincipalBalance.replace(to_replace='Bs.S', value='', inplace=True, regex=True)

        siif_df.CreditLimit = pd.to_numeric(siif_df.CreditLimit, errors='coerce')
        siif_df.Amt30DPD = pd.to_numeric(siif_df.Amt30DPD, errors='coerce')
        siif_df.Amt60DPD = pd.to_numeric(siif_df.Amt60DPD, errors='coerce')
        siif_df.Amt90DPD = pd.to_numeric(siif_df.Amt90DPD, errors='coerce')
        siif_df.Amt120DPD = pd.to_numeric(siif_df.Amt120DPD, errors='coerce')
        siif_df.Amt150DPD = pd.to_numeric(siif_df.Amt150DPD, errors='coerce')
        siif_df.Amt180DPD = pd.to_numeric(siif_df.Amt180DPD, errors='coerce')
        siif_df.Amt210DPD = pd.to_numeric(siif_df.Amt210DPD, errors='coerce')
        siif_df.SaldoCastigado = pd.to_numeric(siif_df.SaldoCastigado, errors='coerce')
        siif_df.PrincipalBalance = pd.to_numeric(siif_df.PrincipalBalance, errors='coerce')

        siif_df['MakerDate'] = datetime.date.today
        siif_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        siif_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def sobregiros_consumer(self, data, user):
        """Sobregiros Consumer resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        names = [
            'BranchId', 'BranchDescription', 'CId', 'TipoPersona', 'Acct',
            'OpenDate', 'Rate', 'MinBalance', 'Producto', 'Remunerada',
            'TermDays', 'StatusId', 'StatusDescription', 'Balance', 'Overdraft',
            'Nombre', 'MaturityDate', 'TypeId', 'DescriptionType', 'Opened',
            'RecordDate', 'NA2', 'NA1', 'NTID', 'SEX', 'BDTE', 'CRCD', 'CPREF',
            'OPDT', 'ACTI', 'OCCP', 'Fecha_Cambio_Estatus_Credito',
            'Fecha_Registro_Vencida_Litigio_Castigada',
            'Fecha_Exigibilidad_Pago_ultima_cuota_pagada',
            'Capital_Transferido', 'Fecha_Cambio_Capital_Transferido',
            'Riesgo', 'Provision', 'SaldoProvision',
        ]

        na_values = {
            'MaturityDate': pd.to_datetime('1900-01-01'),
        }

        sobregiros_gcg = pd.read_excel(path, sheet_name=1, names=names)

        sobregiros_gcg.fillna(value=na_values, inplace=True)

        sobregiros_gcg['MakerDate'] = datetime.date.today
        sobregiros_gcg['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        sobregiros_gcg.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def vnp003t(self, data, user):
        """VNP003T resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        abs_dir, f_name, _ = self.get_path_file(path)

        labels = [
            'DBKA', 'DAPPNA', 'DACCTA', 'DSTATA', 'DTYPEA', 'DBRCHA', 'DOPDTA',
            'DOFFA', 'DCBALA', 'DAVBLA', 'DRATEA', 'DCPRTA', 'LNBILA', 'LNACAA',
            'LNFACA', 'LNDLRA', 'LNPDLA', 'LNMTDA', 'LNIDUA', 'LNPDTA', 'TMNXMA',
            'TMTDYA', 'LND30A', 'LND60A', 'LND90A', 'LNACTA', 'LNPMPA', 'LNF11A',
            'LNTRMA', 'LNFRTA', 'LNEONA', 'LNPAMA', 'DOY2AA', 'LNY2AA', 'TMY2AA',
            'DMMBLA', 'DMMACA', 'DMSCOA', 'LNINBA', 'LNIVAA', 'LNLFDA', 'LY2ABA',
            'LY2ACA', 'LXBI1A', 'LXBI2A', 'LXBP1A', 'LXBP2A', 'LNB12A', 'LY2ASA',
            'LNASTA', 'LNTERF', 'LNCONF', 'LXCDTA', 'LXCPBL', 'LXCCPR', 'LXTREC',
            'LXBLPR', 'LXBLIN', 'LXY2AJ', 'DXMTDA', 'LXY2AO', 'LNBLTY', 'DXDDRP',
            'DXDDRA', 'DXSCDT', 'LXRENA', 'LXREFA', 'LXREBA', 'LXREPA', 'LXREOA',
            'LXREIA', 'LXRIBA', 'VNDUEA', 'DEMPA', 'TNBFEE', 'TNCFEE', 'LXFLDO',
            'LXINGF', 'LXFECC', 'LXUSRC', 'LXINGU', 'LXFECU', 'LXUSRU', 'LXAPRA',
            'LXSALD', 'LXVAIN', 'LXADTE', 'LXAUSR', 'LXAPRU', 'LXSALU', 'LXVAIU',
            'LXADTU', 'LXAUSU',
            ]

        fwidths = [3, 2, 12, 1, 3, 3, 7, 3, 14, 14, 8, 7, 1, 15, 14, 3, 3, 6, 14,
                   2, 6, 5, 3, 3, 3, 16, 14, 14, 3, 7, 2, 16, 8, 8, 8, 12, 14, 3,
                   2, 8, 12, 8, 8, 14, 14, 14, 14, 1, 8, 3, 3, 31, 8, 14, 14, 14,
                   14, 14, 8, 14, 8, 1, 14, 14, 8, 12, 12, 12, 12, 3, 3, 3, 14, 1,
                   15, 15, 1, 14, 8, 10, 14, 8, 10, 14, 14, 14, 8, 10, 14, 14, 14, 8, 10,]

        vnp003t_df = pd.read_fwf(path, widths=fwidths, names=labels)

        vnp003t_df.TNBFEE.replace(to_replace=' ', value='', inplace=True, regex=True)

        vnp003t_df.TNBFEE = vnp003t_df.TNBFEE.astype('float64')

        vnp003t_df.DOY2AA = pd.to_datetime(vnp003t_df.DOY2AA, format='%Y%m%d', errors='coerce')
        vnp003t_df.TMY2AA = pd.to_datetime(vnp003t_df.TMY2AA, format='%Y%m%d', errors='coerce')
        vnp003t_df.DOY2AA.fillna(pd.to_datetime('1900-01-01'), inplace=True)
        vnp003t_df.TMY2AA.fillna(pd.to_datetime('1900-01-01'), inplace=True)

        vnp003t_df['MakerDate'] = datetime.date.today
        vnp003t_df['MakerUser'] = user

        out_path = join(abs_dir, f_name + '.txt')

        vnp003t_df.to_csv(
            out_path,
            sep='~', date_format='%d/%m/%Y', index=False)

        return out_path


    def call_method(self, resource_name, data, user):
        """Call the method corresponding to the resource_name provided"""

        data_path = ''

        if resource_name in RESOURCE_CHOICES:

            if resource_name == 'AH':
                data_path = self.account_history(data, user)
            elif resource_name == 'AT04CRE':
                data_path = self.at04_cre(data, user)
            elif resource_name == 'AT07':
                data_path = self.at07(data, user)
            elif resource_name == 'BBAT':
                data_path = self.bal_by_acct_transformada(data, user)
            elif resource_name == 'CND':
                data_path = self.cartera_no_dirigida(data, user)
            elif resource_name == 'CD':
                data_path = self.cartera_dirigida(data, user)
            elif resource_name == 'FDN':
                data_path = self.fdn(data, user)
            elif resource_name == 'GICG':
                data_path = self.gavetas_icg(data, user)
            elif resource_name == 'LNP860':
                data_path = self.lnp860(data, user)
            elif resource_name == 'MM':
                data_path = self.migrate_mortgage(data, user)
            elif resource_name == 'MISP':
                data_path = self.mis_provisiones(data, user)
            elif resource_name == 'PPRRHH':
                data_path = self.prestamo_prestaciones_hr(data, user)
            elif resource_name == 'RICG':
                data_path = self.rendimientos_icg(data, user)
            elif resource_name == 'SIIF':
                data_path = self.siif(data, user)
            elif resource_name == 'SC':
                data_path = self.sobregiros_consumer(data, user)
            elif resource_name == 'VNP003T':
                data_path = self.vnp003t(data, user)
            else:
                pass

            return data_path
