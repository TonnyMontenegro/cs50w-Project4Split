# Generated by Django 4.0 on 2021-12-18 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0008_auto_20211214_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumo',
            name='monto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16, null=True),
        ),
        migrations.AddField(
            model_name='consumo',
            name='monto_iva',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=16, null=True),
        ),
    ]