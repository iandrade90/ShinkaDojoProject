# Generated by Django 3.2.3 on 2021-05-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_programa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_uno', models.CharField(max_length=30)),
                ('enfasis_uno', models.CharField(max_length=30)),
                ('titulo_dos', models.CharField(max_length=30)),
                ('enfasis_dos', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=200)),
            ],
        ),
    ]
