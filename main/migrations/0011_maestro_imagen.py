# Generated by Django 3.2.3 on 2021-05-26 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_experto_maestro'),
    ]

    operations = [
        migrations.AddField(
            model_name='maestro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
