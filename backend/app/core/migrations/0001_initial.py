# Generated by Django 3.0.2 on 2020-07-20 04:04

import core.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('soeid', models.CharField(max_length=7, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('expiresIn', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(choices=[('AT01', 'AT01 - Accionistas del Ente Supervisado'), ('AT02', 'AT02 - Bienes Recibidos en Pago'), ('AT03', 'AT03 - Contable'), ('AT04', 'AT04 - Cartera de Creditos'), ('AT05', 'AT05 - Captaciones'), ('AT06', 'AT06 - Transacciones Financieras'), ('AT07', 'AT07 - Garantias Recibidas'), ('AT08', 'AT08 - Agencias y Oficinas'), ('AT09', 'AT09 - Compra y Venta de Inversiones en Titulos Valores'), ('AT10', 'AT10 - Inversiones'), ('AT11', 'AT11 - Conformacion de las Disponibilidades, Inversiones y Custodios a Terceros'), ('AT12', 'AT12 - Consumos de Tarjetas'), ('AT13', 'AT13 - Reclamos'), ('AT14', 'AT14 - Instrumentos'), ('AT15', 'AT15 - Notificacion de Transpaso de Acciones'), ('AT16', 'AT16 - Empresas Accionistas del Ente Supervisado'), ('AT17', 'AT17 - Agricola Semanal'), ('AT18', 'AT18 - Variaciones de las tasas de Credito'), ('AT19', 'AT19 - Transacciones de Pago'), ('AT20', 'AT20 - Notas al Pie del Balance'), ('AT21', 'AT21 - Garantes'), ('AT23', 'AT23 - Personal'), ('AT24', 'AT24 - Balance General de Publicacion'), ('AT25', 'AT25 - Estado de Resultados'), ('AT26', 'AT26 - Fraude Bancario'), ('AT27', 'AT27 - Composicion Activa-Pasiva de Organismos Oficiales, P. Juridicas y Naturales'), ('AT29', 'AT29 - Gravamen'), ('AT30', 'AT30 - Adquisicion y Venta de Bienes Recibidos en Pago'), ('AT31', 'AT31 - Movimientos de credito y debito de las operaciones Activas y Pasivas'), ('AT32', 'AT32 - Fondo de Ahorro Obligatorio para la Viviendaa (FAOV)'), ('AT33', 'AT33 - Convenio Cambiario'), ('AT34', 'AT34 - Grupo Junta Directiva del Ente'), ('AT35', 'AT35 - 100 Mayores Depositantes de personas Naturales y Juridicas'), ('AT36', 'AT36 - Lineas de Credito de Utilizacion Automatica'), ('AT37', 'AT37 - Transferencias Electronicas'), ('AT38', 'AT38 - Impuesto a las Grandes Transacciones Financieras')], default='', max_length=50)),
                ('book_data', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(choices=[('AT01', 'AT01 - Accionistas del Ente Supervisado'), ('AT02', 'AT02 - Bienes Recibidos en Pago'), ('AT03', 'AT03 - Contable'), ('AT04', 'AT04 - Cartera de Creditos'), ('AT05', 'AT05 - Captaciones'), ('AT06', 'AT06 - Transacciones Financieras'), ('AT07', 'AT07 - Garantias Recibidas'), ('AT08', 'AT08 - Agencias y Oficinas'), ('AT09', 'AT09 - Compra y Venta de Inversiones en Titulos Valores'), ('AT10', 'AT10 - Inversiones'), ('AT11', 'AT11 - Conformacion de las Disponibilidades, Inversiones y Custodios a Terceros'), ('AT12', 'AT12 - Consumos de Tarjetas'), ('AT13', 'AT13 - Reclamos'), ('AT14', 'AT14 - Instrumentos'), ('AT15', 'AT15 - Notificacion de Transpaso de Acciones'), ('AT16', 'AT16 - Empresas Accionistas del Ente Supervisado'), ('AT17', 'AT17 - Agricola Semanal'), ('AT18', 'AT18 - Variaciones de las tasas de Credito'), ('AT19', 'AT19 - Transacciones de Pago'), ('AT20', 'AT20 - Notas al Pie del Balance'), ('AT21', 'AT21 - Garantes'), ('AT23', 'AT23 - Personal'), ('AT24', 'AT24 - Balance General de Publicacion'), ('AT25', 'AT25 - Estado de Resultados'), ('AT26', 'AT26 - Fraude Bancario'), ('AT27', 'AT27 - Composicion Activa-Pasiva de Organismos Oficiales, P. Juridicas y Naturales'), ('AT29', 'AT29 - Gravamen'), ('AT30', 'AT30 - Adquisicion y Venta de Bienes Recibidos en Pago'), ('AT31', 'AT31 - Movimientos de credito y debito de las operaciones Activas y Pasivas'), ('AT32', 'AT32 - Fondo de Ahorro Obligatorio para la Viviendaa (FAOV)'), ('AT33', 'AT33 - Convenio Cambiario'), ('AT34', 'AT34 - Grupo Junta Directiva del Ente'), ('AT35', 'AT35 - 100 Mayores Depositantes de personas Naturales y Juridicas'), ('AT36', 'AT36 - Lineas de Credito de Utilizacion Automatica'), ('AT37', 'AT37 - Transferencias Electronicas'), ('AT38', 'AT38 - Impuesto a las Grandes Transacciones Financieras')], default='', max_length=50)),
                ('resource_name', models.CharField(choices=[('AH', 'Account History'), ('AT04', 'AT04 Transmitido Pasado'), ('AT04CRE', 'AT04 CRE'), ('AT07', 'AT07 Actual'), ('BBAT', 'Bal By Acct Transformada'), ('CND', 'Cartera No Dirigida'), ('CC', 'Clientes Consumer'), ('CD', 'Cartera Dirigida'), ('CFGESIIFCITI', 'Tabla CFGESIIFCITI (Equivalencias Actividad Cliente)'), ('FDN', 'Fecha de Nacimiento'), ('GICG', 'Gavetas ICG'), ('LNP860', 'LNP860'), ('MM', 'Migrate Mortgage'), ('MISP', 'MIS Provisiones'), ('PPRRHH', 'Prestamos sobre Prestaciones RRHH'), ('RICG', 'Rendimientos ICG'), ('SIIF', 'SIIF'), ('SC', 'Sobregiros Consumer'), ('VNP003T', 'VNP003T')], default='', max_length=50)),
                ('file', models.FileField(upload_to=core.models.path_and_rename)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
