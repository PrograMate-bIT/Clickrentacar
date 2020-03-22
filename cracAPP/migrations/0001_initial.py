# Generated by Django 3.0.4 on 2020-03-22 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(default='', max_length=30, unique=True)),
                ('contrasenia', models.CharField(default='', max_length=30)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('mail', models.EmailField(default='', max_length=50, unique=True)),
                ('telefono', models.IntegerField(verbose_name=20)),
                ('antiguedad', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=30)),
                ('pais', models.CharField(choices=[('UY', 'Uruguay'), ('AR', 'Argentina'), ('BR', 'Brasil'), ('CL', 'Chile'), ('BO', 'Bolivia'), ('CO', 'Colombia'), ('EC', 'Ecuador'), ('PY', 'Paraguay'), ('PE', 'Perú'), ('VE', 'Venezuela')], default='UY', max_length=2)),
            ],
            options={
                'unique_together': {('ciudad', 'pais')},
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('idLicencia', models.IntegerField(primary_key=True, serialize=False)),
                ('catA', models.BooleanField(default=False)),
                ('catB', models.BooleanField(default=False)),
                ('catC', models.BooleanField(default=False)),
                ('catD', models.BooleanField(default=False)),
                ('catE', models.BooleanField(default=False)),
                ('catF', models.BooleanField(default=False)),
                ('catG1', models.BooleanField(default=False)),
                ('catG2', models.BooleanField(default=False)),
                ('catG3', models.BooleanField(default=False)),
                ('catH', models.BooleanField(default=False)),
                ('vencimiento', models.DateField()),
                ('cantPasajeros', models.IntegerField(verbose_name=2)),
                ('restricciones', models.IntegerField(verbose_name=2)),
                ('observaciones', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAlquiler',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('marca', models.CharField(default='', max_length=15)),
                ('anio', models.IntegerField(default=1900)),
                ('categoria', models.CharField(choices=[('auto', 'Auto'), ('camioneta', 'Camioneta'), ('camion', 'Camion'), ('moto', 'Moto')], default='auto', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoPapeles',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ci', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(default='', max_length=30, unique=True)),
                ('contrasenia', models.CharField(default='', max_length=30)),
                ('mail', models.EmailField(default='', max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(verbose_name=20)),
                ('fechaNacimiento', models.DateField()),
                ('calle', models.CharField(max_length=50)),
                ('esquina', models.CharField(max_length=50)),
                ('numDireccion', models.IntegerField(verbose_name=4)),
                ('bizz', models.IntegerField(verbose_name=4)),
                ('antiguedad', models.DateField(auto_now_add=True)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad')),
                ('libretaConducir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Licencia')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudRegistro',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nroSolicitud', models.IntegerField()),
                ('estadoSolicitud', models.CharField(choices=[('PEN', 'Pendiente'), ('APR', 'Aprobada'), ('DEN', 'Denegada')], default='PEN', max_length=3)),
                ('fechaSolicitud', models.DateField()),
                ('horaSolicitud', models.TimeField()),
                ('fechaGestion', models.DateField()),
                ('horaGestion', models.TimeField()),
                ('comentarioAprobador', models.CharField(max_length=100)),
                ('aprobador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Administrador')),
                ('ciSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAlquiler',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaSolicitud', models.DateTimeField(auto_now_add=True)),
                ('startDate', models.DateField(blank=True)),
                ('startTime', models.TimeField(blank=True)),
                ('endDate', models.DateField(blank=True)),
                ('endTime', models.TimeField(blank=True)),
                ('usarioSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilRenta',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilAlquila',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('libreta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Licencia')),
            ],
        ),
        migrations.CreateModel(
            name='Denegacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comentarioDenegacion', models.CharField(max_length=100)),
                ('fechaDenegacion', models.DateTimeField(auto_now_add=True)),
                ('administradorDenegador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Administrador')),
                ('ciSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Usuario')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='administrador',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cracAPP.Ciudad'),
        ),
    ]
