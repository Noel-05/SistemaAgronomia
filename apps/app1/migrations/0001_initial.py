# Generated by Django 2.2.6 on 2020-09-23 05:14

import apps.app1.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsesorExterno',
            fields=[
                ('dui_asesor_externo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_asesor_externo', models.CharField(max_length=50)),
                ('apellido_asesor_externo', models.CharField(max_length=50)),
                ('cargo_asesor_externo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('codigo_carrera', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('codigo_ciclo', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_ciclo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EntidadExterna',
            fields=[
                ('codigo_entidad', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_entidad', models.CharField(max_length=100)),
                ('direccion_entidad', models.CharField(max_length=250)),
                ('telefono_entidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('carnet_estudiante', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre_estudiante', models.CharField(max_length=50)),
                ('apellido_estudiante', models.CharField(max_length=50)),
                ('sexo_estudiante', models.CharField(max_length=1)),
                ('telefono_estudiante', models.IntegerField()),
                ('correo_estudiante', models.CharField(max_length=100)),
                ('direccion_estudiante', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('codigo_proyecto', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('descripcion_proyecto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('nombre_rol', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('descripcion_rol', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('carnet_estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.Estudiante')),
                ('horas_semana', models.IntegerField()),
                ('dias_semana', models.IntegerField()),
                ('modalidad', models.CharField(max_length=30)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(null=True)),
                ('codigo_entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.EntidadExterna')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('carnet_docente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_docente', models.CharField(max_length=50)),
                ('apellido_docente', models.CharField(max_length=50)),
                ('nombre_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Rol')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivosEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(blank=True, null=True, upload_to=apps.app1.models.crear_subcarpeta)),
                ('carnet_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoSolicitud',
            fields=[
                ('carnet_estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.Solicitud')),
                ('aceptado', models.CharField(max_length=30)),
                ('motivo', models.CharField(blank=True, max_length=200, null=True)),
                ('observaciones', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstudioUniversitario',
            fields=[
                ('carnet_estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.Estudiante')),
                ('porc_carrerar_aprob', models.IntegerField()),
                ('unidades_valorativas', models.IntegerField()),
                ('experiencia_areas_conoc', models.CharField(max_length=200)),
                ('codigo_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Carrera')),
                ('codigo_ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='ServicioSocial',
            fields=[
                ('carnet_estudiante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.Solicitud')),
                ('carnet_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Docente')),
                ('codigo_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Proyecto')),
                ('dui_asesor_externo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.AsesorExterno')),
            ],
        ),
    ]
