# Generated by Django 3.1.7 on 2021-06-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20210531_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='solicitado',
            field=models.IntegerField(default=67, verbose_name='Solicitado 67'),
        ),
    ]
