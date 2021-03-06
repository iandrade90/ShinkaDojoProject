# Generated by Django 3.2.3 on 2021-05-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('enfasis', models.CharField(max_length=30)),
                ('contenido', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=250)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
