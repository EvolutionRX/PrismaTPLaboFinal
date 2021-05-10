# Generated by Django 3.1.7 on 2021-05-10 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, unique=True, verbose_name='nombre_categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20, unique=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
            },
        ),
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unidad_de_medida', models.CharField(max_length=10, unique=True, verbose_name='tipo_de_unidad')),
            ],
            options={
                'verbose_name': 'unidad_de_medida',
                'verbose_name_plural': 'unidades_de_medida',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre')),
                ('precio', models.FloatField(blank=True, null=True, verbose_name='Precio')),
                ('stockMinimo', models.IntegerField(default=0, verbose_name='Stock Minimo')),
                ('stockSeguridad', models.IntegerField(default=1, verbose_name='Stock de Seguridad')),
                ('ubicacion', models.CharField(blank=True, max_length=40, null=True, verbose_name='Ubicación')),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.categoria')),
                ('estado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.estado')),
                ('unidad_de_medida', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='item.unidaddemedida')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
            },
        ),
    ]
