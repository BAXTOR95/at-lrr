import datetime

from os.path import join
from django.conf import settings

import pandas as pd
import numpy as np


HLP = 6 # Hipotecario Largo Plazo
HCP = 7 # Hipotecario Corto Plazo
TURISMO = 8 # Turismo
MICROFINANCIERO = 9 # Microfinanciero
MANUFACTURA = 10 # Manufactura
AGRICOLA_ICG = 11 # Agricola ICG
AGRICOLA_OTHER_ICG = 12 # Agricola Other ICG

class DataPreparation():
    """Data Preparation Class for every resource file"""

    def account_history(self, data, user):
        """Account History resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

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

        a_h.to_csv(
            path, sep='~', date_format='%d/%m/%Y', index=False)

    def at04_cre(self, data, user):
        """AT04CRE resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        labels = [
            'BRANCH',
            'REFERNO',
            'LIQUFECHA',
            'SOLIFECHA',
            'APROFECHA',
            'VCTOFECHA',
            'VCTOULTINTER',
            'VCTOULTPRINC',
            'ORIGFECHA',
            'PGTOULTCAPITAL',
            'PGTOULTINTERES',
            'BASECLI',
            'RIFCLI',
            'NOMECLI',
            'SICVENCLI',
            'SICUSACLI',
            'NACICLI',
            'DOMICLI',
            'FECHACLI',
            'LIABICLI',
            'LIABNOMCLI',
            'RIESGOCLI',
            'ADDRESS1',
            'ADDRESS2',
            'ADDRESS3',
            'ADDRESS4',
            'ADDRESS5',
            'ADDRESS6',
            'ADDRESSEXTRA',
            'CTRORG',
            'QTDREN',
            'MONEDA',
            'PRODCAT',
            'LV',
            'STATUS',
            'PLAZO',
            'GENLEDGER',
            'CREDITLINE',
            'INTORIGTASA',
            'CAMBIOTASA',
            'COMISTASA',
            'ORIGIMONTO',
            'PAGOMESMONTO',
            'PAGOTOTAL',
            'SALDOMONTO',
            'TOTALCUOTAS',
            'PAGASCUOTAS',
            'VENCIDACUOTAS',
            'N030DMONTOVENCIDO',
            'N060DMONTOVENCIDO',
            'N090DMONTOVENCIDO',
            'N120DMONTOVENCIDO',
            'N180DMONTOVENCIDO',
            'N360DMONTOVENCIDO',
            'MA1AMONTOVENCIDO',
            'N030DMONTOAVENCER',
            'N060DMONTOAVENCER',
            'N090DMONTOAVENCER',
            'N120DMONTOAVENCER',
            'N180DMONTOAVENCER',
            'N360DMONTOAVENCER',
            'MA1AMONTOAVENCER',
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

        # TODO: Make it so the file is always saved as .txt
        at04cre.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)

    def at07(self, data, user):
        """AT07 resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

        names = [
            'NumeroCredito',
            'CodigoBien',
            'FechaLiquidacion',
            'CodigoContable',
            'ClaseBien',
            'TipoCliente',
            'IdentificacionCliente',
            'NombreRazonSocial',
            'SituacionGarante',
            'MontoInicial',
            'MontoActual',
            'MontoAvaluo',
            'ValorMercado',
            'FechaUltimoAvaluo',
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

        at07_df.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)

    def bal_by_acct_transformada(self, data, user):
        """BalByAcct Transformada resource Data Preparation"""

        path = join(settings.WEB_ROOT, data['file'])

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

        bbat.to_csv(path, sep='~', index=False)

    def cartera_no_dirigida(self, data, user):
        """Cartera No Dirigida resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        path = join(settings.WEB_ROOT, data['file'])

        names = [
            'Branch',
            'LV',
            'NombreVehiculo',
            'Cuenta',
            'Grupo',
            'Pal',
            'Pal_cat_descr',
            'Prod',
            'Prod_cat_descr',
            'Referencia',
            'Descripcion',
            'ClasificacionRiesgo',
            'Provision',
            'A',
            'FechaInicio',
            'FechaFinal',
            'B',
            'C',
            'BCV',
            'Tasa',
            'Debito',
            'Credito',
            'Saldo',
            'Type',
            'Type3dig',
            'CuentaSIF',
            'RendimientosCobrarReestructurados',
            'RendimientosCobrarEfectosReporto',
            'RendimientosCobrarLitigio',
            'InteresesEfectivamenteCobrados',
            'PorcentajeComisionFLAT',
            'MontoComisionFLAT',
            'PeriodicidadPagoEspecialCapital',
            'FechaCambioEstatusCredito',
            'FechaRegistroVencidaLitigioCastigada',
            'FechaExigibilidadPagoUltimaCuotaPagada',
            'CuentaContableProvisionEspecifica',
            'CuentaContableProvisionRendimiento',
            'CuentaContableInteresCuentaOrden',
            'MontoInteresCuentaOrden',
            'TipoBeneficiarioSectorManufacturero',
            'TipoBeneficiarioSectorTurismo',
            'BeneficiarioEspecial',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'TipoVivienda',
            'FechaFinPeriodoGraciaPagoInteres',
            'CapitalTransferido',
            'FechaCambioEstatusCapitalTransferido',
            'SaldoProvision',
            'ActividadCliente',
            'TipoGarantiaPrincipal',
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

        # TODO: Make it so the file is always saved as .txt
        cnd.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)


    def cartera_dirigida(self, data, user):
        """Cartera Dirigida resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        paths = [path for path in data['file']]
        paths.sort()

        parse_dates = [
            'FECHA_SOLICITUD',
            'FECHA_APROBACION',
            'FECHA_LIQUIDACION',
            'FECHA_VENC_ORIGINAL',
            'FECHA_VENC_ACTUAL',
            'FECHA_REESTRUCTURACION',
            'FECHA_PRORROGA',
            'FECHA_ULTIMA_RENOVACION',
            'FECHA_CANCEL',
            'FECHA_VENC_ULTIMA_CUOTA_CAPITAL',
            'ULTIMA_FECHA_CANCEL_CUOTA_CAPITAL',
            'FECHA_VENC_ULTIMA_CUOTA_INTERES',
            'ULTIMA_FECHA_CANCEL_CUOTA_INTERES',
            'FECHA_ESTADO_FINANCIERO',
            'FECHA_EMISION_FACTIBILIDAD_TECNICA',
            'FECHA_AUTENTICACION',
            'FECHA_ULTIMA_INSPECCION',
            'FECHA_VENC_REGISTRO',
            'Upd_Date'
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

        # TODO: Make so it saves the new file on the same path but with different name and extention
        c_d.to_csv(paths[0], sep='~', date_format='%d/%m/%Y', index=False)


    def fdn(self, data, user):
        """Fecha de Nacimiento resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        path = join(settings.WEB_ROOT, data['file'])

        parse_dates = [
            'RecordDate',
        ]

        fdn_df = pd.read_csv(path,
                             sep='~',
                             low_memory=False,
                             encoding = "latin",
                             parse_dates=parse_dates)

        fdn_df.FechaNacimiento = pd.to_datetime(
            fdn_df.FechaNacimiento,
            format='%Y%m%d',
            errors='coerce'
            )
        fdn_df['MakerDate'] = datetime.date.today
        fdn_df['MakerUser'] = user

        fdn_df.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)


    def gavetas_icg(self, data, user):
        """Gavetas ICG resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        paths = [path for path in data['file']]
        paths.sort()

        names = [
            'RIF',
            'NombreRazonSocial',
            'NumeroCredito',
            'InteresesEfectivamenteCobrados',
            'PorcentajeComisionFLAT',
            'MontoComisionFLAT',
            'PeriodicidadPagoEspecialCapital',
            'FechaCambioEstatusCredito',
            'FechaExigibilidadPagolaultimaCuotaPagada',
            'FechaRegistroVencidaLitigioCastigada',
            'TipoIndustria',
            'TipoBeneficiarioSectorManufacturero',
            'TipoBeneficiarioSectorTurismo',
            'BeneficiarioEspecial',
            'FechaEmisionCertificacionBeneficiarioEspecial',
            'TipoVivienda',
            'FechaFinPeriodoGraciaPagoInteres',
            'CapitalTransferido',
            'FechaCambioEstatusCapitalTransferido',
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

        # TODO: Make so it saves the new file on the same path but with different name and extention
        gavetas.to_csv(paths[0], sep='~', date_format='%d/%m/%Y', index=False)


    def lnp860(self, data, user):
        """LNP860 resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        path = join(settings.WEB_ROOT, data['file'])

        labels = [
            'P8NOTE',
            'P8TINC',
            'P8FVUC',
            'P8FCCC',
            'P8FVUI',
            'P8FCCI',
            'P8NRCV',
            'P8MV30',
            'P8MV60',
            'P8MV90',
            'P8MV12',
            'P8MV18',
            'P8MV1A',
            'P8MVM1',
            'P8RPCV',
            'P8LINT',
            'P8FCTC',
            'P8MOCA',
            'P8MOIN',
            'P8TRXN',
            'P8PRAN',
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

        lnp860_df[fields] = lnp860_df[fields].apply(lambda x:x/100)
        lnp860_df.P8TINC = lnp860_df.P8TINC.apply(lambda x:x/1000000)

        lnp860_df['MakerDate'] = datetime.date.today
        lnp860_df['MakerUser'] = user

        # TODO: Make it so the file is always saved as .txt
        lnp860_df.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)


    def migrate_mortgage(self, data, user):
        """Migrate Mortgage resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        path = join(settings.WEB_ROOT, data['file'])

        converters = {
            'TypeId':str,
        }

        parse_dates = [
            'MigratedDate',
            'OrigOpenDate',
        ]

        mm = pd.read_csv(path,
                         sep='~',
                         low_memory=False,
                         parse_dates=parse_dates,
                         converters=converters)

        mm.OrigCreditLimit.replace(to_replace='Bs.S', value='', inplace=True, regex=True)
        mm.OrigCreditLimit = pd.to_numeric(mm.OrigCreditLimit, errors='coerce')
        mm.TypeId = pd.to_numeric(mm.TypeId)
        mm.TypeId = mm.TypeId.astype('int32')
        mm.fillna(value={'Num30':0, 'Num60':0, 'Num90':0,}, inplace=True)

        mm['MakerDate'] = datetime.date.today
        mm['MakerUser'] = user

        # TODO: Make it so the file is always saved as .txt
        mm.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)


    def mis_provisiones(self, data, user):
        """MIS Provisiones resource Data Preparation"""

        # TODO: Add a function that substracts the path, file name and extension of the path given
        path = join(settings.WEB_ROOT, data['file'])

        columns = ['Cid',
                   'Account',
                   'AccountNew',
                   'ProdType',
                   'Provision',
                   'SumSaldo',
                   'Saldo_Provision',
                   'SaldoRendXcobrar',
                   'SaldoRendXcobrarVenc',
                   'ProvisionREND',
                   'Saldo_Provision_REND',
                   'Overdraft',
                   'MaxOfCantCuotasVencidas',
                   'CtaLocal',
                   'CtaProvCap',
                   'CtaProvRend',
                   'Riesgo',
                   'RiskSicri',
                   'Producto',
                   'DescriptionType',
                   'RecordDate',
                   'HDelinquency',
                   'BlockCode1Date',
                   'BlockCodeId1',
                   'BlockReason1',
                   'BlockCode2Date',
                   'BlockCodeId2',
                   'BlockReason2',
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

        # TODO: Make so it saves the new file on the same path but with different name and extention
        mispf[columns].to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)
