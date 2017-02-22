# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-22 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergenos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alergeno', models.CharField(max_length=255, verbose_name='Nombre del Alérgeno')),
            ],
            options={
                'verbose_name_plural': 'Alérgenos',
                'verbose_name': 'Alérgeno',
            },
        ),
        migrations.CreateModel(
            name='Alergicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observaciones')),
                ('alergeno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.Alergenos', verbose_name='Alérgeno')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
            ],
            options={
                'verbose_name_plural': 'Alérgicos',
                'verbose_name': 'Alérgico',
            },
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Institución')),
            ],
            options={
                'verbose_name_plural': 'Clínicas',
                'verbose_name': 'Clínica',
            },
        ),
        migrations.CreateModel(
            name='CoberturaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroAfiliado', models.CharField(max_length=11, unique=True, verbose_name='Número de Afiliado')),
                ('fechaInicio', models.DateField(null=True, verbose_name='Fecha de Inicio de Cobertura')),
                ('fechaFin', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización de Cobertura')),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observaciones')),
                ('bombero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Bombero', verbose_name='Bombero')),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.Clinica', verbose_name='Clínica')),
            ],
            options={
                'verbose_name_plural': 'Coberturas Médicas',
                'verbose_name': 'Cobertura Médica',
            },
        ),
        migrations.CreateModel(
            name='MedicoCabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroMatricula', models.CharField(max_length=11, unique=True, verbose_name='Número de Matrícula')),
                ('persona', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name='Persona')),
            ],
            options={
                'verbose_name_plural': 'Médicos de Cabecera',
                'verbose_name': 'Médico de Cabecera',
            },
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personas.Institucion', verbose_name='Institución')),
            ],
            options={
                'verbose_name_plural': 'Obras Sociales',
                'verbose_name': 'Obra Social',
            },
        ),
        migrations.CreateModel(
            name='PlanMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=255, verbose_name='Descripción')),
                ('obraSocial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obraSocial', to='salud.ObraSocial', verbose_name='Obra Social')),
            ],
            options={
                'verbose_name_plural': 'Planes Médicos',
                'verbose_name': 'Plan Médico',
            },
        ),
        migrations.AddField(
            model_name='coberturamedica',
            name='medicoCabecera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.MedicoCabecera', verbose_name='Médico de Cabecera'),
        ),
        migrations.AddField(
            model_name='coberturamedica',
            name='planMedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salud.PlanMedico', verbose_name='Plan Médico'),
        ),
        migrations.AlterUniqueTogether(
            name='medicocabecera',
            unique_together=set([('persona', 'nroMatricula')]),
        ),
        migrations.AlterUniqueTogether(
            name='coberturamedica',
            unique_together=set([('bombero', 'planMedico')]),
        ),
        migrations.AlterUniqueTogether(
            name='alergicos',
            unique_together=set([('bombero', 'alergeno')]),
        ),
    ]