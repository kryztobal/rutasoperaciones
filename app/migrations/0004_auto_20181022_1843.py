# Generated by Django 2.1.2 on 2018-10-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181022_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activa',
            name='servicio',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]