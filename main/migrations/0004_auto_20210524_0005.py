# Generated by Django 3.1.5 on 2021-05-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_acerca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acerca',
            old_name='titulo_programa',
            new_name='titulo_programa_dos',
        ),
        migrations.AddField(
            model_name='acerca',
            name='titulo_programa_uno',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
