# Generated by Django 2.1.1 on 2018-12-04 19:19

from django.db import migrations, models
import encurtador.validators


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0005_auto_20181204_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=220, validators=[encurtador.validators.validar_url]),
        ),
    ]