# Generated by Django 2.1.2 on 2018-10-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181024_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activa',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]
