# Generated by Django 3.2.3 on 2021-05-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_maestro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
