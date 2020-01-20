from os.path import join
from django.conf import settings

import pandas as pd
import numpy as np
import datetime


class DataPreparation():
    """Data Preparation Class for every resource file"""

    def account_history(self, file_path, user):
        """Account History resource Data Preparation"""

        path = join(settings.WEB_ROOT, file_path)

        a_h = pd.read_csv(path, sep='~', low_memory=False)

        a_h.loc[a_h.PrincipalBalance.sort_values(
            ascending=False).index]

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

    def at04_cre(self, file_path, user):
        """AT04CRE resource Data Preparation"""

        path = join(settings.WEB_ROOT, file_path)

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

        # TODO: Make it so the file is always saved as .txt
        at04cre.to_csv(path, sep='~', date_format='%d/%m/%Y', index=False)
