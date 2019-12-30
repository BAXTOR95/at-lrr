from django.db import models


# Tablas de Configuracion SB

class SB03(models.Model):
    """SB03 - Pais configuration table model"""
    Codigo_Pais = models.CharField(max_length=2, primary_key=True)
    Nombre_Pais = models.CharField(max_length=50)

    def __str__(self):
        return self.Codigo_Pais


class SB09(models.Model):
    """SB09 - Tipo_Credito configuration table model"""
    Tipo_Credito = models.IntegerField(primary_key=True)
    Nombre_Tipo_Credito = models.CharField(max_length=100)

    def __str__(self):
        return self.Tipo_Credito


class SB10(models.Model):
    """SB10 - Actividad_Economica configuration table model"""
    Actividad_Economica = models.CharField(max_length=50, primary_key=True)
    Nombre_Actividad = models.CharField(max_length=300)

    def __str__(self):
        return self.Actividad_Economica


class SB11(models.Model):
    """SB11 - Tipo_Garantia configuration table model"""
    Garantia = models.IntegerField(primary_key=True)
    NombreGarantia = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.Garantia


class SB15(models.Model):
    """SB15 - Moneda configuration table model"""
    Moneda = models.CharField(max_length=3, primary_key=True)
    Nombre_Moneda = models.CharField(max_length=50)
    Pais = models.CharField(max_length=2)
    Moneda_Secore = models.CharField(max_length=5)
    Moneda_RDWH = models.CharField(max_length=5)
    Moneda_UltraSec = models.CharField(max_length=5)

    def __str__(self):
        return self.Moneda


class SB16(models.Model):
    """SB16 - Tipo_Persona configuration table model"""
    Codigo_Tipo_Persona = models.CharField(max_length=1, primary_key=True)
    Nombre_Tipo_Persona = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Tipo_Persona


class SB19(models.Model):
    """SB19 - Clasificacion_Riesgo_Credito configuration table model"""
    Clasificacion_Riesgo = models.CharField(max_length=1, primary_key=True)
    NombreClasificacion_Riesgo = models.CharField(max_length=100)

    def __str__(self):
        return self.Clasificacion_Riesgo


class SB30(models.Model):
    """SB30 - Periodicidad configuration table model"""
    Periodicidad = models.IntegerField(primary_key=True)
    Nombre_Periodicidad = models.CharField(max_length=20)

    def __str__(self):
        return self.Periodicidad


class SB31(models.Model):
    """SB31 - Codigo_Indicador configuration table model"""
    Codigo_Indicador = models.IntegerField(primary_key=True)
    Descripcion_Codigo_Indicador = models.CharField(max_length=10)

    def __str__(self):
        return self.Codigo_Indicador


class SB34(models.Model):
    """SB34 - Estado_Credito configuration table model"""
    Codigo_Estado_Credito = models.IntegerField(primary_key=True)
    Nombre_Estado_Credito = models.CharField(max_length=30)

    def __str__(self):
        return self.Codigo_Estado_Credito


class SB35(models.Model):
    """SB35 - Situacion_Credito configuration table model"""
    Codigo_Situacion_Credito = models.IntegerField(primary_key=True)
    Nombre_Situacion_Credito = models.CharField(max_length=20)

    def __str__(self):
        return self.Codigo_Situacion_Credito


class SB59(models.Model):
    """SB59 - Genero configuration table model"""
    Genero = models.IntegerField(primary_key=True)
    Descripcion_Genero = models.CharField(max_length=10)

    def __str__(self):
        return self.Genero


class SB66(models.Model):
    """SB66 - Codigo_Uso configuration table model"""
    Codigo_Uso = models.CharField(max_length=50, primary_key=True)
    Descripcion_Codigo_Uso = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Uso


class SB67(models.Model):
    """SB67 - Medida configuration table model"""
    Codigo_Medida = models.IntegerField(primary_key=True)
    Unidad_Medida = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Medida


class SB68(models.Model):
    """SB68 - Plazo configuration table model"""
    Codigo_Plazo = models.CharField(max_length=50, primary_key=True)
    Nombre_Plazo = models.CharField(max_length=30)

    def __str__(self):
        return self.Codigo_Plazo


class SB76(models.Model):
    """SB76 - Naturaleza_Cliente configuration table model"""
    Codigo_Naturaleza = models.IntegerField(primary_key=True)
    Descripcion_Naturaleza = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Naturaleza


class SB81(models.Model):
    """SB81 - Modalidad_Microcredito configuration table model"""
    Codigo_Modalidad = models.IntegerField(primary_key=True)
    Descripcion_Modalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Modalidad


class SB82(models.Model):
    """SB82 - Uso_Financiero configuration table model"""
    Codigo_Uso_Financiero = models.IntegerField(primary_key=True)
    Uso_Financiero = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Uso_Financiero


class SB83(models.Model):
    """SB83 - Destino_Recursos_Microfinancieros configuration table model"""
    Codigo_Destino = models.IntegerField(primary_key=True)
    Descripcion_Destino = models.CharField(max_length=200)

    def __str__(self):
        return self.Codigo_Destino


class SB85(models.Model):
    """SB85 - Tipo_Proyecto configuration table model"""
    Tipo_Proyecto = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Proyecto = models.CharField(max_length=100)

    def __str__(self):
        return self.Tipo_Proyecto


class SB87(models.Model):
    """SB87 - Sector_Produccion configuration table model"""
    Codigo_Sector = models.IntegerField(primary_key=True)
    Descripcion_Sector = models.CharField(max_length=150)

    def __str__(self):
        return self.Codigo_Sector


class SB88(models.Model):
    """SB88 - Rubro configuration table model"""
    Codigo_Rubro = models.CharField(max_length=50, primary_key=True)
    Clasificacion = models.CharField(max_length=200)

    def __str__(self):
        return self.Codigo_Rubro


class SB90(models.Model):
    """SB90 - Modalidad_Hipotecaria configuration table model"""
    Codigo_Modalidad = models.IntegerField(primary_key=True)
    Descripcon_Modalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.Codigo_Modalidad


class SB92(models.Model):
    """SB92 - Destino_Manufacturero configuration table model"""
    Codigo_Destino = models.IntegerField(primary_key=True)
    Descripcion_Destino = models.CharField(max_length=250)

    def __str__(self):
        return self.Codigo_Destino


class SB100(models.Model):
    """SB100 - Tipo_Operaciones configuration table model"""
    Tipo_Operaciones = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Operaciones = models.CharField(max_length=100)

    def __str__(self):
        return self.Tipo_Operaciones


class SB101(models.Model):
    """SB101 - Codigo Segmento configuration table model"""
    Codigo_Segmento = models.IntegerField(primary_key=True)
    Descripcion_Segmento = models.CharField(max_length=20)

    def __str__(self):
        return self.Codigo_Segmento


class SB102(models.Model):
    """SB102 - Zona_Interes configuration table model"""
    Codigo_Zona = models.IntegerField(primary_key=True)
    Descripcion_Zona = models.CharField(max_length=50)

    def __str__(self):
        return self.Codigo_Zona


class SB103(models.Model):
    """SB103 - Tipo_Subsector configuration table model"""
    Tipo_Subsector = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Subsector = models.CharField(max_length=50)

    def __str__(self):
        return self.Tipo_Subsector


class SB105(models.Model):
    """SB105 - Destino_Economico configuration table model"""
    Codigo_Destino = models.IntegerField(primary_key=True)
    Descripcion_Destino = models.CharField(max_length=100)

    def __str__(self):
        return self.Codigo_Destino


class SB136(models.Model):
    """SB136 - Tipo_Industria configuration table model"""
    Codigo_Tipo_Industria = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Industria = models.CharField(max_length=50)
    Definicion_Tipo_Industria = models.CharField(max_length=300)

    def __str__(self):
        return self.Codigo_Tipo_Industria


class SB137(models.Model):
    """SB137 - Tipo_Beneficiario_Sector_Manufacturero configuration table model"""
    Codigo_Tipo_Beneficiario = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Beneficiaio = models.CharField(max_length=50)
    Definicion_Tipo_Beneficiario = models.CharField(max_length=300)

    def __str__(self):
        return self.Codigo_Tipo_Beneficiario


class SB138(models.Model):
    """SB138 - Tipo_Vivienda configuration table model"""
    Codigo_Tipo_Vivienda = models.IntegerField(primary_key=True)
    Nombre_Tipo_Vivienda = models.CharField(max_length=30)

    def __str__(self):
        return self.Codigo_Tipo_Vivienda


class SB140(models.Model):
    """SB140 - Tipo_Beneficiario_Sector_Turismo configuration table model"""
    Codigo_Tipo_Beneficiario = models.IntegerField(primary_key=True)
    Descripcion_Tipo_Beneficiaio = models.CharField(max_length=50)
    Definicion_Tipo_Beneficiario = models.CharField(max_length=300)

    def __str__(self):
        return self.Codigo_Tipo_Beneficiario
