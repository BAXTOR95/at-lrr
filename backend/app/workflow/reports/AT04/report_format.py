"""AT04 Report Format Module"""
import pandas as pd


class ReportFormat():
    """AT04 Report Formatter Class"""

    decimal_format = '{0:.2f}'.format
    rate_format = '{0:.4f}'.format
    # single_format = '{0:.0f}%'.format
    office_format = '{0:0>4}'.format
    cod_parr_format = '{0:0>6}'.format
    ci_format = '{0:0>9}'.format

    decimal_fields = [
        'MontoLineaCredito', 'MontoOriginal', 'MontoInicial',
        'MontoLiquidadoMes', 'MontoInicialTerceros', 'Saldo',
        'RendimientosCobrar', 'RendimientosCobrarVencidos',
        'RendimientosCobrarMora', 'ProvisionEspecifica',
        'ProvisionRendimientoCobrar', 'ComisionesCobrar', 'ComisionesCobradas',
        'ErogacionesRecuperables', 'MontoVencido30dias', 'MontoVencido60dias',
        'MontoVencido90dias', 'MontoVencido120dias', 'MontoVencido180dias',
        'MontoVencidoUnAno', 'MontoVencidoMasUnAno', 'MontoVencer30dias',
        'MontoVencer60dias', 'MontoVencer90dias', 'MontoVencer120dias',
        'MontoVencer180dias', 'MontoVencerUnAno', 'MontoVencerMasUnAno',
        'VentaAnuales', 'PagosEfectuadosDuranteMes', 'MontosLiquidadosFechaCierre',
        'AmortizacionesCapitalAcumuladasFecha', 'CantidadUnidades', 'IngresoFamiliar',
        'MontoLiquidadoDuranteAnoCurso', 'SaldoCredito31_12',
        'RendimientosCobrarReestructurados', 'RendimientosCobrarAfectosReporto',
        'RendimientosCobrarLitigio', 'InteresEfectivamenteCobrado', 'MontoComisionFlat',
        'MontoInteresCuentaOrden', 'CapitalTransferido', 'UnidadValoracionAT04',
    ]

    rate_fields = [
        'Sindicado', 'TipoCambioOriginal', 'TipoCambioCierreMes',
        'PorcentajeProvisionEspecifica', 'TasasInteresCobrada', 'TasasInteresActual',
        'TasaComision', 'PorcentajeProvisionEspecifica', 'PorcentajeEjecucionProyecto',
        'CantidadHectareas', 'SuperficieTotalPropiedad', 'PorcentajeComisionFlat'
    ]

    ci_fields = [
        'IdentificacionCliente', 'IdentificacionTipoClienteRIF'
    ]

    def set_format(self, dataframe):
        """Format setter"""

        # Making a copy of the original dataframe
        df_format = dataframe.copy()

        # Formatting decimal fields
        df_format[self.decimal_fields] = df_format[self.decimal_fields].astype(
            'float64').applymap(self.decimal_format)

        # Formatting rate fields
        df_format[self.rate_fields] = df_format[self.rate_fields].astype(
            'float64').applymap(self.rate_format)

        # Formatting ci fields
        df_format[self.ci_fields] = df_format[self.ci_fields].applymap(
            self.ci_format)

        # Formatting Oficina field
        df_format['Oficina'] = df_format['Oficina'].map(self.office_format)

        # Formatting CodigoParroquia field
        df_format['CodigoParroquia'] = df_format['CodigoParroquia'].map(
            self.cod_parr_format)

        # Changing decimal indicator of amount fields from dot to comma
        df_format[self.decimal_fields] = df_format[self.decimal_fields].apply(
            lambda x: x.replace(r'\.', ',', regex=True))

        df_format[self.rate_fields] = df_format[self.rate_fields].apply(
            lambda x: x.replace(r'\.', ',', regex=True))

        # returning new dataframe
        return df_format
